import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

path = '../../data1.mat'

data = loadmat(path)
data = data['data1']

x = data[0, :]
y = data[1, :]

indices = np.arange(len(data[0]))
samples = np.random.choice(indices, 2)
x_values = data[0, samples]
y_values = data[1, samples]

X = np.array([np.ones(len(x_values)), x_values]).T
Y = y_values.T

betas = np.linalg.inv(X.T @ X) @ X.T @ Y
yn = np.array([np.ones(len(x)), x]).T @ betas

thr = 0.2
y_min = yn - thr * np.mean(yn)
y_max = yn + thr * np.mean(yn)

good_indices = []
for i in range(len(y)):
    min_val = y_min[i]
    max_val = y_max[i]
    if y[i] > min_val and y[i] < max_val:
        good_indices.append(i)

print('Good indices is ', len(good_indices) / len(y) * 100, '%')

X = np.array([np.ones(len(good_indices)),x[good_indices]]).T
Y = np.array(y[good_indices]).T

betas = np.linalg.inv(X.T @ X) @ X.T @ Y
yn_good = np.array([np.ones(len(x[good_indices])), x[good_indices]]).T @ betas



plt.figure()
plt.plot(data[0, :],data[1, :], 'r*')
plt.plot(x_values, y_values, 'ko')
plt.plot(x, yn, 'g-')
plt.plot(x, y_min, 'b-')
plt.plot(x, y_max, 'b-')
plt.plot(x[good_indices], yn_good, 'k-')
plt.show()
