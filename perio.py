import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import simpson

def interpol(t,y,samples):
    interp = interp1d(t, y, kind='linear')
    t_new = np.linspace(0, t[-1], samples)
    y_new = interp(t_new)
    f = np.linspace(0, 1/(t_new[1] - t_new[0]), samples)
    return t_new, y_new, f

def per(t_new, y_new, f, samples):
    p = [1/samples * ( (np.sum(y_new * np.cos(2 * np.pi * f[i] * t_new)))**2 + ((np.sum(y_new * np.sin(2 * np.pi * f[i] * t_new)))**2) )  for i in range(samples)]
    return np.array(p)

def per_ls(t_new_ls, y_ls, f, samples):
    tau = [1 / (4 * np.pi * f[i]) * np.arctan(np.sum(np.sin(4 * np.pi * f[i] * t_new_ls)) / np.sum(np.cos(4 * np.pi * f[i] * t_new_ls))) for i in range(1, samples)]
    cos_part = np.array([np.sum(y_ls * np.cos(2 * np.pi * f[i] * (t_new_ls - tau)))**2 / np.sum(np.cos(2 * np.pi * f[i] * (t_new_ls - tau))**2) for i in range(1, samples)])
    sin_part = np.array([np.sum(y_ls * np.sin(2 * np.pi * f[i] * (t_new_ls - tau)))**2 / np.sum(np.sin(2 * np.pi * f[i] * (t_new_ls - tau))**2) for i in range(1, samples)])
    p_ls = 1/2 * (cos_part + sin_part)
    return p_ls


def bandpower(frequencies, power_spectrum, freq_range):
    idx_band = np.logical_and(frequencies >= freq_range[0], frequencies <= freq_range[1])
    # print(type(idx_band))
    band_power = simpson(power_spectrum[idx_band], x=frequencies[idx_band])
    return band_power