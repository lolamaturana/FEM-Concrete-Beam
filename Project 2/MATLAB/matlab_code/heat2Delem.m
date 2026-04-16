 function [ke, fe] = heat2Delem_T3(e)

include_flags;

ke = zeros(3,3);    % T3 has 3 nodes
fe = zeros(3,1);

% Element connectivity
je = IEN(:,e);      % 3×1
C  = [x(je); y(je)]';   % 3×2

% ---- Shape function gradients (constant) ----
[B, detJ] = BmatHeat2D_T3(C);

% ---- Element stiffness matrix ----
ke = D * (B' * B) * detJ / 2;

% ---- Source term (constant s) ----
if exist('s','var')
    Nbar = [1/3 1/3 1/3];    % centroid values
    se   = Nbar * s(:,e);
    fe   = Nbar' * se * detJ / 2;
end





