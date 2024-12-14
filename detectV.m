function [swa, sto, t_max, t_min] = detectV(signal)
%DETECTV Summary of this function goes here
%   This function detects ABR signal's fifth wave

persistent iter

if(isempty(iter))
    iter = 1;
else
    iter = iter + 1;
end

[swa,swd] = swt(signal,6,'bior5.5');

swa = swa(6, :);


fig_proc = figure;
plot(swa)
title('SWA after preprocessing')


[max, idx_max] = findpeaks(swa);
localmins = islocalmin(swa);
min = swa(localmins);
idx_min = find(localmins == 1);

min_range = 550 + int16(iter/5) * 10;
max_range = 700 + int16(iter/5) * 10;

idx_V = find(idx_max > min_range & idx_max < max_range);
V_max = max(idx_V(1));
t_max = idx_max(idx_V(1));

idx_V_min = find(idx_min > idx_max(idx_V(1)));
idx_V_min = idx_V_min(1);
V_min = min(idx_V_min);
t_min = idx_min(idx_V_min);

V_pp = V_max - V_min;
V_mean = abs(mean(swa));

sto = V_pp / V_mean;

close(fig_proc)
end

