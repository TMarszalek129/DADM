import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = "../../chf206.dat"
hrv = pd.read_csv(file_path, delimiter='\t').values.ravel()
hrv = hrv
mean_hrv = np.mean(hrv)
hrv_mean_out = np.cumsum(hrv - mean_hrv)
time = np.cumsum(hrv)

hrv_intervals = []
time_intervals = []
interval = []
LEN = 4
counter = 0

for i in range(0, len(hrv_mean_out), LEN):
    hrv_intervals.append(hrv_mean_out[i:i+LEN])
    time_intervals.append(time[i:i+LEN])

if(len(hrv_intervals[-1]) != LEN):
    hrv_intervals.pop(len(hrv_intervals) - 1)
    time_intervals.pop(len(time_intervals) - 1)

hrv_intervals = np.array(hrv_intervals)
time_intervals = np.array(time_intervals)
betas = []
results = []
for i in range(len(hrv_intervals)):
    y = np.array(hrv_intervals[i]).T
    X = np.array([np.ones(len(time_intervals[i])), time_intervals[i]]).T
    out = np.linalg.inv(X.T @ X) @ X.T @ y
    yn = X @ np.array(out)
    results.append(yn)
    betas.append(out)
results = np.array(results)

plt.figure()
plt.plot(time, hrv_mean_out)
# plt.ylim(-0.5, 0.5)
plt.grid()
plt.xlabel('Time[s]')
plt.ylabel('Integrated HRV signal [s]')
plt.title('Integrated HRV')
plt.show()

plt.figure()
plt.plot(time_intervals, hrv_intervals, "r*")
for i in range(len(time_intervals)):
    plt.plot(time_intervals[i], results[i])
plt.xlim([0, 10])
plt.ylim([-0.5, 0.5])
plt.grid()
plt.xlabel('$x_{t}$[s]')
plt.ylabel('y[s]')
plt.title('n=' + str(LEN))
plt.show()
