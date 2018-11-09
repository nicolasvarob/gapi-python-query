import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.pylab as plt

def visualize(dataframe):
    x = dataframe
    plt.plot(x, np.sin(x))
    plt.show()