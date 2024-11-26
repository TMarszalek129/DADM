import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from model import ransac, ols, ransac_eng, ols_eng, detect_extrema
"""
#path = '../../data1.mat'
path = 'C:/Users/bartl/Downloads/data1.mat'

data = loadmat(path)
data = data['data1']

x = data[0, :]
y = data[1, :]

indices = np.arange(len(data[0]))
samples = np.random.choice(indices, 2)
x_values = data[0, samples]
y_values = data[1, samples]

print(x_values, y_values)
ransac(x_values, y_values, x, y, data, True)
ols(x, y, True)
"""
path_eng = 'C:/Users/bartl/Downloads/eng_signals.mat'

data_eng = loadmat(path_eng)
data_eng = data_eng['eng_signal1']

f_p = 100
t = np.arange(0, len(data_eng) / f_p, 1 / f_p)

max, min = detect_extrema(data_eng.ravel(), t, True)
ransac_eng(max[:-1], min[1:], t, data_eng, True)
#ols_eng(max[:-1], min[1:], t, data_eng, False)
