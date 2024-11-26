import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from model import ransac, ols

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


ransac(x_values, y_values, x, y, data, True)
ols(x, y, data, True)

