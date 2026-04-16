clear; clc; close all;

%% ===================== INPUT =====================
filename = 'coarse_mesh_1000.inp';
k = 1;                          % conductivity (Laplace)
D = k * eye(2);

plot_mesh  = 'yes';
plot_phi   = 'yes';
plot_flux  = 'yes';

%% ===================== READ ABAQUS MESH =====================
[nodeIds, nodeCoords, elemIds, elemConn] = readAbaqusInp(filename);

[~, elemConnIdx] = ismember(elemConn, nodeIds);
IEN = elemConnIdx';                 % 3 x nel
x   = nodeCoords(:,1);
y   = nodeCoords(:,2);

nnp = length(x);
nel = size(IEN,2);
neq = nnp;

%% ===================== INITIALIZE =====================
K = zeros(neq);
f = zeros(neq,1);
phi = zeros(neq,1);
flags = zeros(neq,1);
e_bc  = zeros(neq,1);

%% ===================== ASSEMBLY =====================
for e = 1:nel
    sctr = IEN(:,e);
    [ke] = elemStiff_T3(sctr, x, y, D);
    K(sctr,sctr) = K(sctr,sctr) + ke;
end

%% 
%% ===================== EXTRACT BOUNDARY EDGES =====================
edges = sort([IEN([1 2],:), IEN([2 3],:), IEN([3 1],:) ]',2);
[ue,~,ic] = unique(edges,'rows');
counts = accumarray(ic,1);
bedges = ue(counts==1,:);     % boundary edges only

tol = 1e-6;
xmin = min(x); xmax = max(x);

% Neumann flux values
qin  = -1;    % AB
qout =  1;    % DC

for i = 1:size(bedges,1)
    n1 = bedges(i,1);
    n2 = bedges(i,2);

    xm = 0.5*(x(n1)+x(n2));

    if abs(xm - xmin) < tol
        f = applyFluxEdge(f,n1,n2,x,y,qin);
    elseif abs(xm - xmax) < tol
        f = applyFluxEdge(f,n1,n2,x,y,qout);
    end
end

%% ===================== DIRICHLET BC //Essential BC=====================
refNode = find(abs(x - xmax) < tol & abs(y - min(y)) < tol, 1);
flags(refNode) = 1;
e_bc(refNode) = 0;



%% ===================== SOLVE =====================
for i = 1:neq
    if flags(i)==1
        f = f - K(:,i)*e_bc(i);
        K(:,i) = 0;
        K(i,:) = 0;
        K(i,i) = 1;
        f(i) = e_bc(i);
    end
end

phi = K\f;

%% ===================== POSTPROCESS =====================
if strcmpi(plot_mesh,'yes')
    figure; triplot(IEN',x,y,'k');
    axis equal; title('Coarse Mesh');
end

if strcmpi(plot_phi,'yes')
    figure; hold on;
    for e = 1:nel
        n = IEN(:,e);
        patch(x(n), y(n), phi(n), ...
              'EdgeColor','k');
    end
    axis equal tight;
    colorbar;
    title('Velocity Potential \phi');
    xlabel('X'); ylabel('Y');
end
if strcmpi(plot_flux,'yes')
    figure; hold on;

    for e = 1:nel
        n = IEN(:,e);
        C = [x(n) y(n)];

        [B,~] = Bmat_T3_direct(C);
        gradphi = B * phi(n);   % <-- FIXED

        xc = mean(x(n));
        yc = mean(y(n));

        % Normalize velocity for visualization
        Vmag = norm(gradphi);
        if Vmag > 0
            u = gradphi / Vmag;
        else
            u = [0;0];
        end

        quiver(xc, yc, u(1), u(2), 0.03, 'k');
    end

    axis equal tight;
    title('Velocity Field-Coarse Mesh');
    xlabel('X'); ylabel('Y');
end

function [nodeIds, nodeCoords, elemIds, elemConn] = readAbaqusInp(filename)
fid = fopen(filename,'r');
nodeIds=[]; nodeCoords=[]; elemIds=[]; elemConn=[];
inNode=false; inElem=false;

while true
    tline=fgetl(fid);
    if ~ischar(tline), break; end
    tline=strtrim(tline);
    if isempty(tline)||startsWith(tline,'**'), continue; end

    if startsWith(tline,'*')
        inNode=false; inElem=false;
        if startsWith(upper(tline),'*NODE'), inNode=true; end
        if startsWith(upper(tline),'*ELEMENT'), inElem=true; end
        continue
    end

    parts=regexp(tline,',','split');
    if inNode
        nodeIds(end+1)=str2double(parts{1});
        nodeCoords(end+1,:) = cellfun(@str2double,parts(2:end));
    elseif inElem
        elemIds(end+1)=str2double(parts{1});
        elemConn(end+1,:) = cellfun(@str2double,parts(2:end));
    end
end
fclose(fid);
end


function ke = elemStiff_T3(sctr,x,y,D)

C = [x(sctr) y(sctr)];
[B, A] = Bmat_T3_direct(C);

ke = B' * D * B * A;
end


function [B, A] = Bmat_T3_direct(C)
% C = [x1 y1; x2 y2; x3 y3]

x1 = C(1,1); y1 = C(1,2);
x2 = C(2,1); y2 = C(2,2);
x3 = C(3,1); y3 = C(3,2);

% Element area
A = 0.5 * det([1 x1 y1;
               1 x2 y2;
               1 x3 y3]);

% b and c coefficients
b = [y2 - y3;
     y3 - y1;
     y1 - y2];

c = [x3 - x2;
     x1 - x3;
     x2 - x1];

% B matrix
B = 1/(2*A) * [b'; 
               c'];
end


function f = applyFluxEdge(f,n1,n2,x,y,qn)
L = hypot(x(n2)-x(n1),y(n2)-y(n1));
f(n1) = f(n1) + qn*L/2;
f(n2) = f(n2) + qn*L/2;
end

%% ===================== MESH + BOUNDARY CONDITIONS =====================
figure; hold on;

% Plot mesh
triplot(IEN',x,y,'k');
axis equal

% Plot boundary edges
for i = 1:size(bedges,1)
    n1 = bedges(i,1);
    n2 = bedges(i,2);
    xm = 0.5*(x(n1)+x(n2));

    if abs(xm-xmin)<tol
        plot(x([n1 n2]),y([n1 n2]),'b','LineWidth',2);   % inlet
    elseif abs(xm-xmax)<tol
        plot(x([n1 n2]),y([n1 n2]),'r','LineWidth',2);   % outlet
    else
        plot(x([n1 n2]),y([n1 n2]),'g','LineWidth',1.5); % walls/airfoil
    end
end

% Reference node
plot(x(refNode),y(refNode),'ko','MarkerFaceColor','y');

legend('Mesh','Inlet AB','Outlet DC','Airfoil','Ref Node');
title('Coarse Mesh with Boundary Conditions');
xlabel('X'); ylabel('Y');

function phiLine = samplePhiAlongLine(x,y,phi,xl,yl)
phiLine = griddata(x,y,phi,xl,yl,'linear');
end

%% COde:
%% ===================== PRESSURE FIELD (MESH-BASED) =====================
rho  = 1;
Uinf = 1;

p_elem = zeros(nel,1);

for e = 1:nel
    n = IEN(:,e);
    C = [x(n) y(n)];

    [B,~] = Bmat_T3_direct(C);
    gradphi = B * phi(n);

    V2 = dot(gradphi, gradphi);
    p_elem(e) = 0.5 * rho * (Uinf^2 - V2);
end

figure; hold on;

for e = 1:nel
    n = IEN(:,e);
    patch(x(n), y(n), ...
          p_elem(e) * ones(3,1), ...
          'EdgeColor','none');
end

axis equal tight;
colorbar;
title('Pressure Field (Bernoulli)-Coarse Mesh');
xlabel('X'); ylabel('Y');


%% ===================== AHBW COMPUTATION =====================
[row,col] = find(K);
bw = abs(row-col);
AHBW = mean(bw);

fprintf('\nAverage Half Band Width (AHBW) for Coarse Mesh = %.2f\n',AHBW);

%%
% ---------------- POINT DEFINITIONS ----------------
E = [-0.5, 0];
F = [ 0.0, 0];
G = [ 0.4, 0.15606];
H = [ 1.0, 0];
I = [ 1.5, 0];

J = [0.21142, -0.08416];

function [s, phiLine] = samplePhiAlongPolyline(x,y,phi,pts,npts_per_seg)

s = [];
phiLine = [];
s_accum = 0;

for k = 1:size(pts,1)-1
    p1 = pts(k,:);
    p2 = pts(k+1,:);
    
    xs = linspace(p1(1), p2(1), npts_per_seg);
    ys = linspace(p1(2), p2(2), npts_per_seg);
    
    phi_seg = griddata(x,y,phi,xs,ys,'linear');
    
    ds = hypot(diff(xs), diff(ys));
    s_seg = [0, cumsum(ds)] + s_accum;
    s_accum = s_seg(end);
    
    s = [s, s_seg];
    phiLine = [phiLine, phi_seg];
end

end

% ---------------- PATH DEFINITIONS ----------------
pts_EFGHI = [E; F; G; H; I];
pts_EFJHI = [E; F; J; H; I];

npts = 50;   % points per segment
[s1, phi_EFGHI] = samplePhiAlongPolyline(x,y,phi,pts_EFGHI,npts);
[s2, phi_EFJHI] = samplePhiAlongPolyline(x,y,phi,pts_EFJHI,npts);

% Normalize arc-length for comparison
s1 = s1 / max(s1);
s2 = s2 / max(s2);

figure; hold on;

plot(s1, phi_EFGHI, 'b-', 'LineWidth', 2);
plot(s2, phi_EFJHI, 'r--', 'LineWidth', 2);

grid on;
xlabel('Normalized distance along line');
ylabel('Velocity Potential \phi');
title('Velocity Potential \phi Along EFGHI and EFJHI');

legend('EFGHI','EFJHI','Location','best');
