import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from function_hrv import interval_hrv
from fluctuation import fluct_mean

file_path = "../../chf206.dat"
# file_path = "C:/Users/bartl/Downloads/chf206.dat"
hrv = pd.read_csv(file_path, delimiter='\t').values.ravel()
hrv = hrv
mean_hrv = np.mean(hrv)
hrv_mean_out = np.cumsum(hrv - mean_hrv)
time = np.cumsum(hrv)

hrv_intervals = []
time_intervals = []
hrv_intervals_temp = []
time_intervals_temp = []
interval = []
results = []
LEN_B = 4
LEN_E = 65

for j in range(LEN_B,LEN_E):
    for i in range(0, len(hrv_mean_out), j):
        hrv_intervals_temp.append(hrv_mean_out[i:i+j])
        time_intervals_temp.append(time[i:i+j])

    if(len(hrv_intervals_temp[-1]) != j):
        hrv_intervals_temp.pop(len(hrv_intervals_temp) - 1)
        time_intervals_temp.pop(len(time_intervals_temp) - 1)

    hrv_intervals_temp = np.array(hrv_intervals_temp)
    time_intervals_temp = np.array(time_intervals_temp)

    hrv_intervals.append(hrv_intervals_temp)
    time_intervals.append(time_intervals_temp)
    results.append(interval_hrv(hrv_intervals_temp, time_intervals_temp))

    hrv_intervals_temp.tolist()
    time_intervals_temp.tolist()
    hrv_intervals_temp = []
    time_intervals_temp = []

# time_intervals = np.array(time_intervals)
# hrv_intervals = np.array(hrv_intervals)
# results = np.array(results)

F = fluct_mean(hrv_intervals, results)

plt.figure()
plt.plot(time, hrv)
plt.grid()
plt.xlabel('Time[s]')
plt.ylabel('HRV [s]')
plt.show()

plt.figure()
plt.plot(time, hrv_mean_out)
# plt.ylim(-0.5, 0.5)
plt.grid()
plt.xlabel('Time[s]')
plt.ylabel('Integrated HRV [s]')
plt.title('Integrated HRV')
plt.show()

plt.figure()
plt.plot(time_intervals[0], hrv_intervals[0], "r*")
for i in range(len(time_intervals[0])):
    plt.plot(time_intervals[0][i], results[0][i])
plt.xlim([0, 10])
plt.ylim([-0.5, 0.5])
plt.grid()
plt.xlabel('$x_{t}$[s]')
plt.ylabel('y[s]')
plt.title('n=' + str(LEN_B))
plt.show()
