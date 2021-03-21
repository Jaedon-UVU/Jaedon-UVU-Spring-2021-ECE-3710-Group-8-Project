# Libraries
import numpy as np
import cmath as cm
import random as rn
import sys
import time

# Functions

# Global Variables
sample_size = 0
rand_data = []

# Executable Code
if __name__ == '__main__':
    # Random Data Generation
    sample_size = input("Enter the sample size: ")  # User input
    for x in range(int(sample_size)):
        sys.stdout.write("\rGenerating {0}/{1}".format(x + 1, sample_size))  # Generation Process Updates
        sys.stdout.flush()
        rand_data.append(rand_data)  # Appending Generated Data
    print("\nFinished")
