#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:45:19 2024

Author: mnasir

Description:
This script converts text files into MAT files using the `Text2Vest` command-line utility provided by the FSL module.
The script assumes that the FSL module is available and the `Text2Vest` utility is installed.

Dependencies:
- FSL (FMRIB Software Library)
- `Text2Vest` utility from FSL

Usage:
1. Ensure that the FSL module is available and properly configured in your environment.
2. Modify the `directory` variable to point to the location of the input text files.
3. Modify the `out_dir` variable to specify the output directory where MAT files will be saved.
4. Run the script to convert each text file in the specified directory to a MAT file.

The script will:
1. Load the FSL module.
2. Iterate over a grid of text files (64x64), assuming filenames follow a specific pattern.
3. Convert each text file to a MAT file using `Text2Vest`.
4. Save the output MAT files to the specified output directory.
"""

import subprocess
import os

# Load the FSL module required for `Text2Vest`
subprocess.run("module load fsl/6.0.4", shell=True, check=True)
subprocess.run("which Text2Vest", shell=True, check=True)  # Verify that `Text2Vest` is available

# Define the directory containing the input text files
directory = '/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall'

# Define the directory where the output MAT files will be stored
out_dir = '/data/extra/mnasir/scripts/matfiles_row_stimuli_RETCCWsmall'

# Create the output directory if it does not exist
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Iterate over a 64x64 grid to process each text file
for x in range(64):
    for y in range(64):
        # Construct the input and output filenames
        input_filename = f"textfilex{x + 1}y{y + 1}.txt"
        output_filename = f"datax{x + 1}y{y + 1}.mat"
        
        # Construct full paths for input and output files
        input_path = os.path.join(directory, input_filename)
        output_path = os.path.join(out_dir, output_filename)
        
        # Construct the command to convert text to MAT file
        command = f"Text2Vest {input_path} {output_path}"
        
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        
        # Print status to monitor progress
        print(f'Processed x: {x}, y: {y}')

