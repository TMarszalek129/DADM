import numpy as np
import matplotlib.pyplot as plt

def differential(N, x, plot=False):
    n_c = np.arange(2, N-2)
    n_f = np.arange(0, 2)
    n_b = np.arange(N-2, N)
    h=1
    diff_c = 1/8 * (-x[n_c-2] - 2*x[n_c-1] + 2*x[n_c+1] + x[n_c+2])
    diff_f = (x[n_f + h] - x[n_f]) / 2*h
    diff_b = (x[n_b] - x[n_b - h]) / 2*h
    diff = np.concatenate([diff_f, diff_c, diff_b])
    
    if(plot):    
        plt.figure()
        plt.title("Diff")
        plt.plot(diff)
        plt.show()

    return diff

def power(N, x, plot=False):
    n = np.arange(0, N)
    p = (x[n])**2
    
    if(plot):    
        plt.figure()
        plt.title("Power")
        plt.plot(p)
        plt.show()

    return p

def integral(N, x, plot=False):
    C = 30
    inte = np.convolve(np.ones(C)/C, x, mode='same')
    
    if(plot):    
        plt.figure()
        plt.title("Integral")
        plt.plot(inte)
        plt.show()

    return inte