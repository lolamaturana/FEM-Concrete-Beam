% B matrix function
function [B, detJ] = BmatHeat2D(C)
      
     % Calculate the Grad(N) matrix
       % Derivatives of shape functions wrt natural coords
    GN = [ -1   1   0;
           -1   0   1 ];

    % Jacobian
    J    = GN * C;
    detJ = det(J);

    % B matrix (dN/dx, dN/dy)
    B = J \ GN;
end
