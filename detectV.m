function [swa, sto, t_max, t_min] = detectV(signal, db)
%DETECTV Summary of this function goes here
%   This function detects ABR signal's fifth wave

persistent min_range
persistent max_range

[swa,swd] = swt(signal,6,'bior5.5');

swa = swa(6, :);
sto = 0;
t_min = 0;
t_max = 0;

fig_proc = figure;
plot(swa)
title('SWA after preprocessing')

[max, idx_max] = findpeaks(swa)
localmins = islocalmin(swa, 'FlatSelection','first');
min = swa(localmins);
idx_min = find(localmins == 1);

if(isempty(min_range) & isempty(max_range))
    min_range = 550;
    max_range = 700;
else
    min_range = min_range + (120 - db)/2;
    max_range = max_range + (120 - db)/2;
end

if (min_range >= 800)
    warning("%f Hz sound is inaudible", db)
    close(fig_proc)
    return;
end

idx_V = find(idx_max > min_range & idx_max < max_range);
%sprintf("Start min value: %f", min_range)
while isempty(idx_V)
    if (min_range >= 800)
        warning("%f Hz sound is inaudible", db)
        close(fig_proc)
        return;
    end

    sprintf("Min value of range: %f", min_range)
    sprintf("Max value of range: %f", max_range)

    min_range = min_range + 10;
    max_range = max_range + 10;

    idx_V = find(idx_max > min_range & idx_max < max_range);

end

V_max = max(idx_V(1));
t_max = idx_max(idx_V(1));

idx_V_min = find(idx_min > idx_max(idx_V(1)));
try
    idx_V_min = idx_V_min(1);
    V_min = min(idx_V_min);
    t_min = idx_min(idx_V_min);
   
    V_pp = V_max - V_min;
    V_mean = abs(mean(swa));
    
    sto = V_pp / V_mean;
  
catch
    warning("%f Hz sound is inaudible", db)
end

close(fig_proc)
end

