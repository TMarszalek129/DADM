import numpy as np
import matplotlib.pyplot as plt

def differential(N, x, plot=False):
    n = np.arange(2, N-2)
    diff = 1/8 * (-x[n-2] - 2*x[n-1] + 2*x[n+1] + x[n+2])
    
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