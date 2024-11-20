import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

path = '../../data1.mat'

data = loadmat(path)
data = data['data1']

plt.figure()
plt.plot(data[0, :])
plt.show()
