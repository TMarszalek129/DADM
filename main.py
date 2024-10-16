import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from filters import low_filter_design, high_filter_design
from differ import differential, integral, power
from derivative import detect_maxima

#file_path = '../data/data/100_MLII.dat'
file_path="C:/Users/bartl/Downloads/data/data/100_MLII.dat"
ecg = pd.read_csv(file_path, delimiter='\t').values.ravel()
ecg = ecg[2000:7001]
            
f_down = 5
f_up = 15
f_p = 360
t = np.arange(0, len(ecg) / f_p, 1 / f_p)
print(t[1:5])
l_filter = low_filter_design(len(ecg)/5, f_up, f_p, False)
h_filter = high_filter_design(len(ecg)/5, f_down, f_p, False)
ecg_filtered = np.convolve(l_filter, ecg, 'same')
ecg_filtered = np.convolve(h_filter, ecg_filtered, 'same')
diff = differential(len(ecg_filtered), ecg_filtered, False)
p = power(len(diff),diff, False)
inte = integral(len(p), p, False)
x,y = detect_maxima(inte, t, True)

plt.figure()
plt.title("EKG")
plt.plot(ecg)
plt.plot(ecg_filtered)
plt.show()

print('DONE')
