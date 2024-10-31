import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

samples = 128
f_0 = 0.1

t = np.concatenate(([0], np.cumsum(np.random.rand(samples-1))))
y = np.sin(2 * np.pi * f_0 * t)

interp = interp1d(t, y, kind='linear')
t_new = np.linspace(0, t[-1], samples)
y_new = interp(t_new)

f = np.linspace(0, 1/(t_new[1] - t_new[0]), samples)
p = [1/samples * ( (np.sum(y_new * np.cos(2 * np.pi * f[i] * t_new)))**2 + ((np.sum(y_new * np.sin(2 * np.pi * f[i] * t_new)))**2) )  for i in range(samples)]

t_new_ls = t_new[1:]
y_ls = y[1:]
tau = [1 / (4 * np.pi * f[i]) * np.atan(np.sum(np.sin(4 * np.pi * f[i] * t_new_ls)) / np.sum(np.cos(4 * np.pi * f[i] * t_new_ls))) for i in range(1, samples)]
cos_part = np.array([np.sum(y_ls * np.cos(2 * np.pi * f[i] * (t_new_ls - tau)))**2 / np.sum(np.cos(2 * np.pi * f[i] * (t_new_ls - tau))**2) for i in range(1, samples)])
sin_part = np.array([np.sum(y_ls * np.sin(2 * np.pi * f[i] * (t_new_ls - tau)))**2 / np.sum(np.sin(2 * np.pi * f[i] * (t_new_ls - tau))**2) for i in range(1, samples)])
p_ls = 1/2 * (cos_part + sin_part)


plt.figure()
plt.plot(t, y)
plt.plot(t_new, y_new)
plt.title("Signal")
plt.show()

plt.figure()
plt.plot(f, p)
plt.title("Periodogram")
plt.show()

plt.figure()
plt.plot(f[1:], p_ls)
plt.title("Periodogram Lomb-Scargle")
plt.show()