# Libraries
import numpy as np
import cmath as cm
import random as rn
import sys
import time

# Functions

# Global Variables
sample_size = 0
uniform_random_data = []
exponential_random_data = []
weibull_random_data = []
inverse_pyramid_random_data = []


# Executable Code
if __name__ == '__main__':
    # Random Data Generation
    sample_size = input("Enter the sample size: ")  # User input
    # TODO: add more user input parameters

    for x in range(int(sample_size)):  # Uniform Generation
        # TODO: update status on timer
        sys.stdout.write("\rGenerating Uniform Data{0}/{1}".format(x + 1, sample_size))  # Generation Process Updates
        sys.stdout.flush()
        uniform_random_data.append(rn.uniform(0, 1))  # Appending Generated Data

    for x in range(int(sample_size)):  # TODO: Exponential Generation
        # TODO: update status on timer
        sys.stdout.write("\rGenerating Uniform Data{0}/{1}".format(x + 1, sample_size))  # Generation Process Updates
        sys.stdout.flush()
        exponential_random_data.append("""random data""")  # Appending Generated Data

    for x in range(int(sample_size)):  # TODO: Weibull Generation
        # TODO: update status on timer
        sys.stdout.write("\rGenerating Uniform Data{0}/{1}".format(x + 1, sample_size))  # Generation Process Updates
        sys.stdout.flush()
        weibull_random_data.append("""random data""")  # Appending Generated Data

    for x in range(int(sample_size)):  # TODO: Inverse Pyramid Generation
        # TODO: update status on timer
        sys.stdout.write("\rGenerating Uniform Data{0}/{1}".format(x + 1, sample_size))  # Generation Process Updates
        sys.stdout.flush()
        inverse_pyramid_random_data.append("""random data""")  # Appending Generated Data

    print("\nFinished")
