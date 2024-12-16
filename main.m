clear, clc
clear detectV
path_2 = "abr_signal2.mat";
path_3 = "abr_signal3.mat";
path_4 = "abr_signal4.mat";

abr2 = load(path_2);
abr3 = load(path_3);
abr4 = load(path_4);
%% Data:
data2 = abr2.abr_signal2;
data3 = abr3.abr_signal3;
data4 = abr4.abr_signal4;

fp = 100000;
sto_arr = [];
DATA_NUM = data4; % data2 or data3 or data4

%% Process loop:

for i = 1:length(DATA_NUM)
    db = DATA_NUM{i}.dB;
    signal = DATA_NUM{i}.data;
    TIME_I5 = 100*DATA_NUM{i}.l5;

    ones_arr = transpose(signal(length(signal)-1)*ones(1,24));
    signal = [signal; ones_arr];

    t = 0:(1/fp):(length(signal)-1)*(1/fp);
    t = t * fp;

    [swa, sto, t_max, t_min] = detectV(signal, db);
    sto_arr(i) = sto;

    if(sto)
        sprintf("V_pp/V_mean for %f Hz = %f", db, sto)
    
        figure
        plot(t, swa)
        hold on
        plot(t_max, swa(t_max), 'r*')
        plot(t_min, swa(t_min), 'b*')
        y_limits = ylim; 
        plot([TIME_I5 TIME_I5], y_limits, 'r--', 'LineWidth', 2);
        title(['SWA ', num2str(db), ' Hz'])
    end
end

