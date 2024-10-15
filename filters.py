import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def low_filter_design(N, f_c, f_p, plot=False):
    
    f = (f_c / f_p) / 2  
    n = np.arange(0, N)
    mid = int(np.floor(N / 2))
    t_down = np.arange(-mid, 0)
    t_up = np.arange(1, mid+1)
    
    f_l = np.sin(2 * np.pi * f * t_down) / (np.pi * t_down)
    f_0 = 2 * f
    f_r = np.sin(2 * np.pi * f * t_up) / (np.pi * t_up)
    
    f_val = np.hstack((f_l, f_0, f_r))
    
    hamm_win = 0.54 - 0.46 * np.cos(2 * np.pi * n / N - 1).ravel()

    f_val_win = hamm_win * f_val
    
    if(plot):
        w, h = freqz(f_val_win, fs=f_p)
        magnitude = 20 * np.log10(np.abs(h))
        phase = np.unwrap(np.angle(h))
        
        plt.figure()
        plt.plot(w, magnitude)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Magnitude [dB]')
        plt.title('Magnitude of low-pass filter')
        plt.show()
        plt.figure()
        plt.plot(w, phase)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Phase [radians]')
        plt.title('Phase of low-pass filter')
        plt.show()
    
    return f_val_win

def high_filter_design(N, f_c, f_p, plot=False):
    
    f = (f_c / f_p) / 2 
    n = np.arange(0, N)
    mid = int(np.floor(N / 2))
    t_down = np.arange(-mid, 0)
    t_up = np.arange(1, mid+1)
    
    f_l = -np.sin(2 * np.pi * f * t_down) / (np.pi * t_down)
    f_0 = 1 - 2 * f
    f_r = -np.sin(2 * np.pi * f * t_up) / (np.pi * t_up)
    
    f_val = np.hstack((f_l, f_0, f_r))
    hamm_win = 0.54 - 0.46 * np.cos(2 * np.pi * n / N - 1).ravel()

    f_val_win = hamm_win * f_val
    
    if(plot):
        w, h = freqz(f_val_win, fs=f_p)
        magnitude = 20 * np.log10(np.abs(h))
        phase = np.unwrap(np.angle(h))
        
        plt.figure()
        plt.plot(w, magnitude)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Magnitude [dB]')
        plt.title('Magnitude of high-pass filter')
        plt.show()
        
        plt.figure()
        plt.plot(w, phase)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Phase [radians]')
        plt.title('Phase of high-pass filter')
        plt.show()

    return f_val_win