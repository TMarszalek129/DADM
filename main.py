import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = "../../chf206.dat"
hrv = pd.read_csv(file_path, delimiter='\t').values.ravel()
hrv = hrv

hrv_mean_out = hrv - np.mean(hrv)
time = np.cumsum(hrv)

hrv_intervals = []
time_intervals = []
interval = []
LEN = 4
counter = 0

for i in range(0, len(hrv_mean_out), 4):
    hrv_intervals.append(hrv_mean_out[i:i+4])
    time_intervals.append(time[i:i+4])

if(len(hrv_intervals[-1]) != 4):
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

plt.figure()
plt.plot(time, hrv_mean_out)
plt.show()

plt.figure()
plt.plot(time_intervals[1], hrv_intervals[1], "r*")
plt.plot(time_intervals[1], results[1])
plt.xlim([0, 10])
plt.ylim([-0.1, 0.1])
plt.show()
