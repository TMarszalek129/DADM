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

%% Process loop:

for i = 1:length(data2)
    db = data2{i}.dB;
    signal = data2{i}.data;

    ones_arr = transpose(signal(length(signal)-1)*ones(1,24));
    signal = [signal; ones_arr];

    t = 0:1/fp:(length(signal)-1)*(1/fp);
    t = t * 1000;

    [swa, sto, t_max, t_min] = detectV(signal);

    sprintf("V_pp/V_mean for %f Hz = %f", db, sto)

    figure
    plot(swa)
    hold on
    plot(t_max, swa(t_max), 'r*')
    plot(t_min, swa(t_min), 'b*')
    title(['SWA ', num2str(i)])
end

