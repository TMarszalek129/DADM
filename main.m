path_2 = "abr_signal2.mat";
path_3 = "abr_signal3.mat";
path_4 = "abr_signal4.mat";

abr2 = load(path_2);
abr3 = load(path_3);
abr4 = load(path_4);
%% 
data2 = abr2.abr_signal2
data3 = abr3.abr_signal3
data4 = abr4.abr_signal4

db = data{2}.dB
signal = data{1}.data;