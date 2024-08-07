#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:45:19 2024

@author: mnasir
"""

import subprocess
import os
"""
converting text files into mat files 
It require fsl module
"""

# Load FSL module
subprocess.run("module load fsl/6.0.4", shell=True)
subprocess.run("which Text2Vest", shell=True)
subprocess.run("Text2Vest", shell=True)

# Iterate over each pixel location
#Replace the variable directory with actual path to text files
directory='/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall'

# Replace variable out_dir with path where mat files need to be stored
out_dir='/data/extra/mnasir/scripts/matfiles_row_stimuli_RETCCWsmall'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

#Looping over each text file    
for x in range(64):
    for y in range(64):
      
        # Creating the input and output filenames
        input_filename = f"textfilex{x + 1}y{y + 1}.txt"
        output_filename = f"datax{x + 1}y{y + 1}.mat"
      
        input_path = os.path.join(directory, input_filename)
        output_path = os.path.join(out_dir, output_filename)
        command = f"Text2Vest {input_path} {output_path} "
        
        # Execute the command
        subprocess.run(command, shell=True)

        print('x:',x, '  y:', y)
