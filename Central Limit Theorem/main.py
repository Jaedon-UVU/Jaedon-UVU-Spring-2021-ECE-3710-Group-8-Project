# Libraries
import graph
import numpy as np
import cmath as cm
import random as rn
import sys
import time

"""
    Create a computer simulation of four non-normal random variables. Allowing the user to input the parameters for each
distribution.
    > Exponential
    > Weibull
    > Uniform
    > Inverse Triangle
    
    Use pre-made random number generators with the correlating distributions. Generate 50,000 random values.
    Each distribution should have 4 graphs (Histograms)
"""


# Exponential
def exp_dist():
    rng = np.random.exponential(size=50000)
    rng_5 = []
    rng_30 = []
    rng_100 = []
    i = 0
    while i < 50000:
        rng_5.append(sum(rng[i:i+5])/5)
        i += 5
    i = 0
    while i < 50000:
        rng_30.append(sum(rng[i:i+30])/30)
        i += 30
    i = 0
    while i < 50000:
        rng_100.append(sum(rng[i:i+100])/100)
        i += 100

    graph.create_hist(rng, 20)
    graph.create_hist(rng_5, 20)
    graph.create_hist(rng_30, 20)
    graph.create_hist(rng_100, 20)


# Weibull
def weibull_dist():
    rng = np.random.weibull(size=50000)
    pass


# Uniform
def uni_dist():
    rng = np.random.uniform(size=50000)
    rng_5 = []
    rng_30 = []
    rng_100 = []
    i = 0
    while i < 50000:
        rng_5.append(sum(rng[i:i + 5]) / 5)
        i += 5
    i = 0
    while i < 50000:
        rng_30.append(sum(rng[i:i + 30]) / 30)
        i += 30
    i = 0
    while i < 50000:
        rng_100.append(sum(rng[i:i + 100]) / 100)
        i += 100

    graph.create_hist(rng, 20)
    graph.create_hist(rng_5, 20)
    graph.create_hist(rng_30, 20)
    graph.create_hist(rng_100, 20)


# Inverse Triangle
def inv_dist():
    rng = []
    for x in np.random.uniform(size=50000):
        if x < 0.5:
            rng.append(-2*((-2*x + 1)**(1/2)) - 2)
        else:
            rng.append(2*((2*x - 1)**(1/2)) + 2)
    rng_5 = []
    rng_30 = []
    rng_100 = []
    i = 0
    while i < 50000:
        rng_5.append(sum(rng[i:i + 5]) / 5)
        i += 5
    i = 0
    while i < 50000:
        rng_30.append(sum(rng[i:i + 30]) / 30)
        i += 30
    i = 0
    while i < 50000:
        rng_100.append(sum(rng[i:i + 100]) / 100)
        i += 100

    graph.create_hist(rng, 100)
    graph.create_hist(rng_5, 100)
    graph.create_hist(rng_30, 100)
    graph.create_hist(rng_100, 100)

#exp_dist()
inv_dist()