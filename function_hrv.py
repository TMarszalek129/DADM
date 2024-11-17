import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def interval_hrv (hrv_intervals, time_intervals ):

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

    return results

def log_interval_hrv(log_n, log_Fn):

    betas = []
    results = []
    for i in range(len(log_Fn)):
        y = np.array(log_Fn).T
        X = np.array([np.ones(len(log_n[i])), log_n[i]]).T
        out = np.linalg.inv(X.T @ X) @ X.T @ y
        yn = X @ np.array(out)
        results.append(yn)
        betas.append(out)
    results = np.array(results)

    return results
