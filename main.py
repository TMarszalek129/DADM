import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = './data/data/100_MLII.dat'
ecg = pd.read_csv(file_path, delimiter='\t')
ecg = ecg.values

def low_filter(data, f):
    
    mid = int(np.floor(len(data) / 2))
    
    f_value_l = [(np.sin(2 * np.pi * f * M)) / (np.pi * M) for M in range(-mid, 0)]
    print(len(f_value_l))
    f_value_0 = 2 *f
    f_value_r = [(np.sin(2 * np.pi * f * M)) / (np.pi * M) for M in range(1, mid+1)]
    print(len(f_value_r))
    f_value = [f_value_l, f_value_r]
    
    
    return f_value
        
    

f_down = 5
f_up = 15
f_p = 360
f_down_norm = (f_down / f_p) / 2  
f_up_norm = (f_up / f_p) / 2


#N = 2 M + 1

ecg_low = low_filter(ecg, f_down_norm)

#plt.plot(ecg[1000:5000])
plt.plot(ecg_low)
