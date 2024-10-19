import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from filters import low_filter_design, high_filter_design
from differ import differential, integral, power
from derivative import detect_maxima

file_path = '../data/data/100_MLII.dat'
# file_path="C:/Users/bartl/Downloads/data/data/100_MLII.dat"
ecg = pd.read_csv(file_path, delimiter='\t').values.ravel()
ecg = ecg[2000:20000]
            
f_down = 5
f_up = 15
f_p = 360
t = np.arange(0, len(ecg) / f_p, 1 / f_p)
# print(t[1:5])
l_filter = low_filter_design(len(ecg)/5, f_up, f_p, False)
h_filter = high_filter_design(len(ecg)/5, f_down, f_p, False)
ecg_filtered = np.convolve(l_filter, ecg, 'same')
ecg_filtered = np.convolve(h_filter, ecg_filtered, 'same')
diff = differential(len(ecg_filtered), ecg_filtered, False)
p = power(len(diff),diff, False)
inte = integral(len(p), p, False)
times,values = detect_maxima(inte, t, False)

refr = 0.2
SPKI = 0.0001
NPKI = 0.000001
t1 = NPKI + 0.25 * (SPKI - NPKI)
t2 = 0.5 * t1
thr = [t1, t2]
s_peaks, n_peaks = [], []
s_times, n_times = [], []

for ind in (0, 1):
    t_actual = thr[ind]
    for i in range(len(values)):

        if values[i] > t_actual:
            if (times[i] - times[i-1]) < refr:
                if values[i] > values[i-1]:
                    if times[i-1] in s_times:
                        s_times.pop()
                        s_peaks.pop()
                        if times[i-1] not in n_times:
                            n_times.append(times[i-1])
                            n_peaks.append(values[i-1])
                            NPKI = 0.125 * values[i] + 0.875 * NPKI
                    if times[i] not in s_times:
                        s_peaks.append(values[i])
                        s_times.append(times[i])
                        SPKI = 0.125 * values[i] + 0.875 * SPKI
                else:
                    if times[i] not in n_times:
                        n_peaks.append(values[i])
                        n_times.append(times[i])
                        NPKI = 0.125 * values[i] + 0.875 * NPKI
            else:
                if times[i] not in s_times:
                    s_peaks.append(values[i])
                    s_times.append(times[i])
                    SPKI = 0.125 * values[i] + 0.875 * SPKI
        else:
            if times[i] not in n_times:
                n_peaks.append(values[i])
                n_times.append(times[i])
                NPKI = 0.125 * values[i] + 0.875 * NPKI

        thr[0] = NPKI + 0.25 * (SPKI - NPKI)
        thr[1] = 0.5 * t1

plt.figure()
plt.title("EKG")
# plt.plot(t, ecg)
plt.plot(t, inte)
plt.plot(s_times, s_peaks, 'r*')
# plt.xlim(1000, 1250)
plt.show()

