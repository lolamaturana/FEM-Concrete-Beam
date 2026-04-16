filename = 'fine_mesh_1500.inp';

%global nodeCoords elemIds elemConn nodeIds

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
% Display node coordinates on the plot
%hold on;
%plot(nodeCoords(:,1), nodeCoords(:,2), 'ro', 'MarkerFaceColor', 'r');
%hold off;
% Display Ids nodes on plot
hold on;
plot(nodeCoords(:,1), nodeCoords(:,2), 'ro', 'MarkerFaceColor', 'r');
text(nodeCoords(:,1), nodeCoords(:,2), num2str(nodeIds), 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
hold off;
x = nodeCoords(:,1);
display(x);
