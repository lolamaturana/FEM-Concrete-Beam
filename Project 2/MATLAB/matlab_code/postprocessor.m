% plot temperature and flux
% plot temperature and flux (T3 elements)
function postprocess_T3(d)
include_flags

% ---- Plot temperature field ----
if strcmpi(plot_temp,'yes') == 1
    figure(2); clf; hold on;
    
    for e = 1:nel
        
        n1 = IEN(1,e);
        n2 = IEN(2,e);
        n3 = IEN(3,e);
        
        XX = [x(n1) x(n2) x(n3)];
        YY = [y(n1) y(n2) y(n3)];
        dd = [d(n1) d(n2) d(n3)];
        
        patch(XX,YY,dd,'EdgeColor','k');
    end
    
    axis equal
    title('Temperature distribution');
    xlabel('X'); ylabel('Y');
    colorbar
end

% ---- Compute flux (constant per T3 element) ----
if strcmpi(compute_flux,'yes') == 1
    fprintf('\n                     Heat Flux (T3 elements)\n')
    fprintf('-------------------------------------------------------------\n')
    
    for e = 1:nel
        fprintf('Element %d\n', e)
        fprintf('------------\n')
        get_flux_T3(d,e);
    end
end

