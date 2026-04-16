function [nodeIds, nodeCoords, elemIds, elemConn] = readAbaqusInp(filename)
%READABAQUSINP Read nodes and elements from an Abaqus .inp mesh file.
%
%   [nodeIds, nodeCoords, elemIds, elemConn] = readAbaqusInp('Mesh_1000.inp')
%
%   nodeIds   : (nNodes x 1)  node numbers
%   nodeCoords: (nNodes x nd) node coordinates (nd = 2 or 3, etc.)
%   elemIds   : (nElem  x 1)  element numbers
%   elemConn  : (nElem  x nen) connectivity (node numbers for each element)

    fid = fopen(filename, 'r');
    if fid < 0
        error('Could not open file: %s', filename);
    end

    nodeIds   = [];
    nodeCoords = [];
    elemIds   = [];
    elemConn  = [];

    inNode = false;
    inElem = false;

    while true
        tline = fgetl(fid);
        if ~ischar(tline)
            break;  % end of file
        end

        tline = strtrim(tline);

        % Skip empty lines
        if isempty(tline)
            continue;
        end

        % Skip comment lines
        if startsWith(tline, '**')
            continue;
        end

        % Section headers
        if startsWith(tline, '*')
            % leaving any current data section
            inNode = false;
            inElem = false;

            tupper = upper(tline);
            if startsWith(tupper, '*NODE')
                inNode = true;
            elseif startsWith(tupper, '*ELEMENT')
                inElem = true;
            end
            continue;
        end

        % Node data
        if inNode
            % Lines like: "1, 0.997151732, 0.00958249718"
            parts = regexp(tline, '\s*,\s*', 'split');

            id = str2double(parts{1});
            coords = cellfun(@str2double, parts(2:end));

            nodeIds(end+1,1) = id; %#ok<AGROW>

            % ensure enough columns in nodeCoords
            if isempty(nodeCoords)
                nodeCoords = zeros(0, numel(coords));
            end
            nodeCoords(end+1,1:numel(coords)) = coords; %#ok<AGROW>
        end

        % Element data
        if inElem
            % Lines like: "1, 130, 118, 124"
            parts = regexp(tline, '\s*,\s*', 'split');

            id = str2double(parts{1});
            conn = cellfun(@str2double, parts(2:end));

            elemIds(end+1,1) = id; %#ok<AGROW>

            if isempty(elemConn)
                elemConn = zeros(0, numel(conn));
            end
            elemConn(end+1,1:numel(conn)) = conn; %#ok<AGROW>
        end
    end

    fclose(fid);

    % Optional: sort by IDs
    [nodeIds, idxN] = sort(nodeIds);
    nodeCoords = nodeCoords(idxN, :);

    [elemIds, idxE] = sort(elemIds);
    elemConn = elemConn(idxE, :);
end
