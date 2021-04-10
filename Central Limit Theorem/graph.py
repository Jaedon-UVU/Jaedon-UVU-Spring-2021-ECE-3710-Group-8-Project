import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def create_hist(x, bin):
    plt.hist(x, bin)
    plt.show()

