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

    #C = int(0.150 * 360) # 360 to fs a 0.150 nie wiem skąd chat wziął xd
    C = int(N/360)
    inte = np.convolve(x, np.ones(C)/C, mode='same')
    
    if(plot):    
        plt.figure()
        plt.title("Integral")
        plt.plot(inte)
        plt.show()

    return inte