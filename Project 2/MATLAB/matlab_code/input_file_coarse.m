% Input Data for fine mesh

% material property
k  = 1;        % thermal conductivity
D  = k*eye(2); % conductivity matrix 


% mesh specifications
nsd  = 2;         % number of space dimensions
ndof = 1;         % degrees-of-freedom per node

nnp = size(nodeCoords, 1);
nel = size(elemConnIdx, 1);
nen = 3; % bc triangles
neq = nnp*ndof;


IEN = elemConnIdx.';

K = zeros(neq);        % initialize stiffness matrix
f = zeros(neq,1);      % initialize nodal source vector
d = zeros(neq,1);      % initialize nodal temperature vector

flags = zeros(neq,1);  % array to set B.C flags 
e_bc  = zeros(neq,1);  % essential B.C array
n_bc  = zeros(neq,1);  % natural B.C array
P     = zeros(neq,1);   % initialize point source defined at a node

s     = ones(nen,nel);  % heat source

% gauss Integration
ngp    = 2;                          % number of gauss points

% boundary conditions and point forces
nd =  1;     % number of nodes on essential boundary

% essential B.C.

% plots
compute_flux = 'yes';
plot_mesh    = 'yes';
plot_nod     = 'yes';
plot_temp    = 'yes';
plot_flux    = 'yes';


% natural B.C  - defined on edges positioned on natural boundary
flags(35)=2;
e_bc(35)     = 0.0;  %essential boundary condition

        
function n_bc = build_nbc_xmin_xmax(nodeIds, nodeCoords, elemConn, qLeft, qRight, tol)
%BUILD_NBC_XMIN_XMAX Create natural BC array n_bc using x-coordinates.
%
% n_bc is 4 x nseg:
%   row 1: first node id of boundary edge
%   row 2: second node id of boundary edge
%   row 3: q at first node
%   row 4: q at second node
%
% Boundary edges are detected as edges that belong to only one element.

    if nargin < 4, qLeft  = -1; end
    if nargin < 5, qRight = +1; end
    x =zeros(nodeCoords(:,1));

    x = nodeCoords(:,1);
    xmin = min(x);
    xmax = max(x);

    if nargin < 6 || isempty(tol)
        Lx  = xmax - xmin;
        tol = max(1e-10, 1e-8*Lx);   % robust default tolerance
    end

    % ---- 1) Build list of ALL element edges (assumes elemConn is ordered around the element)
    nel = size(elemConn,1);
    nen = size(elemConn,2);

    % edges per element: connect consecutive nodes + last-first
    allEdges = zeros(nel*nen, 2);
    c = 0;
    for e = 1:nel
        conn = elemConn(e,:);
        for a = 1:nen
            b = a + 1;
            if b > nen, b = 1; end
            n1 = conn(a);
            n2 = conn(b);
            c = c + 1;
            allEdges(c,:) = [n1 n2];
        end
    end

    % For boundary detection, sort each edge so [min max]
    eSorted = sort(allEdges, 2);

    % ---- 2) Find boundary edges = edges that appear only once
    [uEdges, ~, ic] = unique(eSorted, 'rows');
    counts = accumarray(ic, 1);
    isBoundary = counts(ic) == 1;

    bEdges = allEdges(isBoundary,:);   % keep original orientation (not essential here)

    % ---- 3) Select boundary edges on xmin and xmax (both nodes must lie on that x)
    x1 = x(bEdges(:,1));
    x2 = x(bEdges(:,2));

    onLeft  = (abs(x1 - xmin) < tol) & (abs(x2 - xmin) < tol);
    onRight = (abs(x1 - xmax) < tol) & (abs(x2 - xmax) < tol);

    leftEdges  = bEdges(onLeft,:);
    rightEdges = bEdges(onRight,:);

    % ---- 4) Order edges consistently along the boundary (optional but nice)
    % Sort by average y (so 's' runs bottom->top). Change if you want top->bottom.
    y =zeros(nodeCoords(:,2));
    y = nodeCoords(:,2);
    if ~isempty(leftEdges)
        yavgL = 0.5*(y(leftEdges(:,1)) + y(leftEdges(:,2)));
        [~, pL] = sort(yavgL, 'ascend');
        leftEdges = leftEdges(pL,:);
    end
    if ~isempty(rightEdges)
        yavgR = 0.5*(y(rightEdges(:,1)) + y(rightEdges(:,2)));
        [~, pR] = sort(yavgR, 'ascend');
        rightEdges = rightEdges(pR,:);
    end

    % ---- 5) Build n_bc (store NODE IDS, but edges were FOUND by coordinates)
    nsegL = size(leftEdges,1);
    nsegR = size(rightEdges,1);

    n_bc = zeros(4, nsegL + nsegR);

    if nsegL > 0
        n_bc(1,1:nsegL) = nodeIds(leftEdges(:,1));
        n_bc(2,1:nsegL) = nodeIds(leftEdges(:,2));
        n_bc(3,1:nsegL) = qLeft;
        n_bc(4,1:nsegL) = qLeft;
    end

    if nsegR > 0
        idx = nsegL + (1:nsegR);
        n_bc(1,idx) = nodeIds(rightEdges(:,1));
        n_bc(2,idx) = nodeIds(rightEdges(:,2));
        n_bc(3,idx) = qRight;
        n_bc(4,idx) = qRight;
    end
end



n_bc = build_nbc_xmin_xmax(nodeIds, nodeCoords, elemConn, -2.0, 3.0);

[m,n]=size(n_bc);
%flags(35)=2;
e_bc(35)     = 0.0;  %essential boundary condition
nbe = n;


% mesh generation
 mesh2d;

