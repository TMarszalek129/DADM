import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from filters import low_filter_design, high_filter_design

file_path = '../data/data/100_MLII.dat'
ecg = pd.read_csv(file_path, delimiter='\t').values.ravel()
ecg = ecg[2000:7001]
            
f_down = 5
f_up = 15
f_p = 360

l_filter = low_filter_design(len(ecg), f_up, f_p, False)
h_filter = high_filter_design(len(ecg), f_down, f_p, False)
ecg_filtered = np.convolve(l_filter, ecg, 'same')
ecg_filtered = np.convolve(h_filter, ecg_filtered, 'same')

plt.figure()
plt.plot(ecg)
plt.plot(ecg_filtered)

print('DONE')
