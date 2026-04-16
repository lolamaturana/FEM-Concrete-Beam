filename = 'Mesh_1000.inp';

[nodeIds, nodeCoords, elemIds, elemConn] = readAbaqusInp(filename);

[~, elemConnIdx] = ismember(elemConn, nodeIds);
if any(elemConnIdx(:) == 0)
    error('Some element connectivity references node IDs that were not found in nodeIds.');
end

% 2D triangular mesh plot
figure;
triplot(elemConnIdx, nodeCoords(:,1), nodeCoords(:,2));
axis equal;
xlabel('X');
ylabel('Y');
title('Finite Element Mesh');