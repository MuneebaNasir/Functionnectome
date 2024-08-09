#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:45:40 2023

@author: mnasir

Description:
    This script processes a stimulus file, containing a 3D matrix of video frames from a MATLAB .mat file, downsampled the 3D matrix from
    300x300x300 to 64x64x300 dimensions, and then converts the downsampled data into text files. Each text file corresponds
    to a specific pixel in the 64x64 frame and contains a time series of 300 timepoints. The text files are named according
    to their pixel coordinates (e.g., textfilex1y1.txt, textfilex1y2.txt, etc.).

Steps:
1. Load the MATLAB v7.3 file using h5py.
2. Create the output directory if it doesn't exist.
3. Access and retrieve the data from the loaded MATLAB file.
4. Downsample the 3D data from 300x300x300 to 64x64x300.
5. Save each pixel's time series data into separate text files named according to pixel coordinates.

Dependencies:
- numpy
- h5py
- scipy
- os

Usage:
    Replace the file path in `mat_file` and `out_dir` variables with actual paths before running the script.
"""

import numpy as np
import h5py
from scipy.ndimage import zoom
import os

# Load the MATLAB v7.3 file using h5py
# Replace the file path with the actual path to the .mat file
mat_file = h5py.File('/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat', 'r')

# Define the output directory for the text files
# Replace with the actual path where you want to save the text files
out_dir = '/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall'

# Create the output directory if it doesn't exist
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Access the data from the loaded MATLAB file
# Replace 'stim' with the actual variable name from the MATLAB file
data = mat_file['stim']  # The variable name in the .mat file

# Convert the data to a NumPy array
downsampled_data = data[()]  # Retrieve the dataset as a NumPy array

# Close the MATLAB file
mat_file.close()

# Define the target size for downsampling
target_size = (64, 64)

# Initialize an array to hold the resized data
resized_data = np.zeros((downsampled_data.shape[0], target_size[0], target_size[1]))

# Downsample each time frame of the data to the target size
for t in range(downsampled_data.shape[0]):
    resized_data[t] = zoom(downsampled_data[t], (target_size[0] / downsampled_data.shape[1], target_size[1] / downsampled_data.shape[2]), order=1)

print(resized_data.shape)  # Print the shape of the resized data

# Update data variable to use the resized data
data = resized_data

# Iterate over each pixel location in the 64x64 frame
for x in range(target_size[0]):
    for y in range(target_size[1]):
        # Define the filename for the text file based on pixel coordinates
        filename = f"{out_dir}/textfilex{x + 1}y{y + 1}.txt"
        
        # Open the text file for writing
        with open(filename, "w") as file:
            # Write the time series data for the pixel (x, y) to the text file
            for t in range(300):
                file.write(str(data[t, x, y]) + "\n")
        # File is automatically closed when exiting the 'with' block
