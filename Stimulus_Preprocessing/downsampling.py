#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:45:40 2023

@author: mnasir
"""


import numpy as np
import h5py
from scipy.ndimage import zoom
import os

"""
    Downsample the stimulus file from 300*300*300 to 64*64*300. 64*64 (frame size), 300 (time frame)
    Convert the downsampled mat files into 64*64 text files, seperate text file for each pixel of the frame. 
    Each text file have 300 timepoints and is saved as textfilex1y1.txt, textfilex1y2.txt,..., textfilex1y64.txt, ...., textfilex64y64.txt
"""


# Load the MATLAB v7.3 file using h5py
# RETCCWsmall: mat file of a stimulus video where wedge is rotating Counter clockwise.

# Replace the "/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat" with actual path
mat_file = h5py.File('/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat', 'r')

# Replace '/data/extra/mnasir/scripts/' with the actual path 
out_dir='/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall'
# It will create the folder if it doesnot exist already
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Access the data from the mat_file
data = mat_file['stim']  # Replace 'stim' with the actual variable name in the MATLAB file

# Convert the data to a NumPy array
downsampled_data = data[()]  # This retrieves the entire dataset as a NumPy array

# Close the file
mat_file.close()

# Define the target size
target_size = (64, 64)

# Resize the downsampled_data to the target size
resized_data = np.zeros((downsampled_data.shape[0], target_size[0], target_size[1]))
for t in range(downsampled_data.shape[0]):
    resized_data[t] = zoom(downsampled_data[t], (target_size[0] / downsampled_data.shape[1], target_size[1] / downsampled_data.shape[2]), order=1)

print(resized_data.shape)

data = resized_data

# Iterate over each pixel location
for x in range(target_size[0]):
    for y in range(target_size[1]):
        # Create a text file for the pixel at (x, y)
        # Replace the "/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall/" with actual folder path
        filename = f"/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall/textfilex{x + 1}y{y + 1}.txt"
        with open(filename, "w") as file:
            # Write the time series data to the text file
            for t in range(300):
                file.write(str(data[t, x, y]) + "\n")
        file.close()
