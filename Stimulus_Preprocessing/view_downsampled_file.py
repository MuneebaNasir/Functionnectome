#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:43:22 2024

@author: mnasir

Description:
    This script processes a stimulus file from a MATLAB .mat file by downsampling it and converting the downsampled
    data into a video for cross-verification. The process involves loading the .mat file, downsampling the 3D data,
    and creating a video from the downsampled frames.

Steps:
1. Load the MATLAB v7.3 file using h5py.
2. Access and retrieve the data from the MATLAB file.
3. Downsample the 3D data from its original size to a target size of 64x64 for each time frame.
4. Create a video from the downsampled data using the imageio library.
5. Save the video to the specified output file path.

Dependencies:
- imageio
- numpy
- h5py
- scipy

Usage:
    Ensure that the path to the .mat file and the output path for the video are correctly specified before running the script.
"""

import imageio
import numpy as np
import h5py
from scipy.ndimage import zoom

# Load the MATLAB v7.3 file using h5py
# Replace the path with the actual path to your .mat file
mat_file_path = '/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat'
mat_file = h5py.File(mat_file_path, 'r')

# Access the data from the file
# Replace 'stim' with the actual variable name in your MATLAB file
data = mat_file['stim']

# Convert the data to a NumPy array if necessary
downsampled_data = data[()]  # Retrieve the entire dataset as a NumPy array

# Close the file
mat_file.close()

# Define the target size for downsampling
target_size = (64, 64)

# Initialize an array to hold the resized data
resized_data = np.zeros((downsampled_data.shape[0], target_size[0], target_size[1]))

# Downsample each time frame of the data to the target size
for t in range(downsampled_data.shape[0]):
    resized_data[t] = zoom(downsampled_data[t], (target_size[0] / downsampled_data.shape[1], target_size[1] / downsampled_data.shape[2]), order=1)

print(resized_data.shape)  # Print the shape of the resized data

# Define the output file path for the video
# Replace with the actual path where you want to save the video
output_file = '/data/extra/mnasir/scripts/downsampled_64_video_RETCCWsmall.mov'

# Create a video writer object with the specified output file path, codec, and FPS
writer = imageio.get_writer(output_file, codec='png', fps=30)  # Adjust the codec and FPS as needed

# Iterate over the time dimension of the resized data and add each frame to the video writer
for t in range(resized_data.shape[0]):
    frame = resized_data[t]  # Select the frame at index t
    writer.append_data(frame)

# Close the writer to finalize the video file
writer.close()

# Print a message indicating the completion
print(f"Video saved as {output_file}")
