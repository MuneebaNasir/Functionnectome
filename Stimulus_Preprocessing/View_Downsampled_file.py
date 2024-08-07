#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:43:22 2024

@author: mnasir
"""
"""this file will create the downsampled mat file,
 and then convert the downsampled mat file into video for cross verification, (running in VNC)"""

import imageio
import numpy as np
import h5py
from scipy.ndimage import zoom

# Load the MATLAB v7.3 file using h5py

mat_file = h5py.File('/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat', 'r')

# Access the data from the file
data = mat_file['stim']  # Replace 'your_variable_name' with the actual variable name in the MATLAB file

# Convert the data to a NumPy array if necessary
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

# Define the output file path where video is stored
output_file = '/data/extra/mnasir/scripts/downsampled_64_video_RETCCWsmall.mov'

# Create a writer object with the desired output file path, codec, and FPS
writer = imageio.get_writer(output_file, codec='png', fps=30)  # Adjust the codec and FPS as needed

# Iterate over the time dimension of the resized_data and add frames to the writer

for t in range(resized_data.shape[0]):
    frame = resized_data[t]  # Select the frame at index t
    writer.append_data(frame)

# Close the writer to finalize the video file
writer.close()

# Print a message indicating the completion
print(f"Video saved as {output_file}")
