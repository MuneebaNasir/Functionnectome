#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:47:09 2024

@author: Muneeb Anasir

This Python script processes neuroimaging data by converting subject-specific fMRI data files to the MNI152 standard space using the FSL tool `flirt`. 
The script is intended to be run on a Linux-based system where FSL is installed and configured.

Dependencies:
- Python 3.x
- FSL (FMRIB Software Library) version 6.0.4

Prerequisites:
- Ensure FSL is installed and configured properly.
- Ensure the FSL module is loaded in the environment.

Usage:
- Update the directory paths (`subject_directory` and `subject_directory_output`) as needed.
- Run the script using Python 3: `python3 reorient_fMRI.py`
"""

import os
import subprocess

# Load the FSL module required for using the flirt tool.
subprocess.run("module load fsl/6.0.4", shell=True)
subprocess.run("which flirt", shell=True)  # Verifies the flirt tool is available.
subprocess.run("flirt", shell=True)  # Runs flirt to verify that it is properly loaded.

# Define the directory containing the subject data files.
subject_directory = "/data/extra/mnasir/scripts/NIFTI_DATA/1_unzipfiles_NIFT"

# Define the directory where the output files will be stored.
subject_directory_output = "/data/extra/mnasir/scripts/NIFTI_DATA/MNI152_NIFT"

# Create the output directory if it doesn't exist.
if not os.path.exists(subject_directory_output):
    os.makedirs(subject_directory_output)

# Define the path to the MNI152 standard brain template file.
ref_file = "$FSLDIR/data/standard/MNI152_T1_2mm_brain.nii.gz"

# List of task folders to process. Add more tasks as needed.
task_folders = ["tfMRI_RETBAR1_7T_AP"]  # Example: ["tfMRI_RETBAR2_7T_PA", "tfMRI_RETCCW_7T_AP"]

# Loop over each subject folder in the subject directory.
for subject_folder in os.listdir(subject_directory):
    print('Starting: ', subject_folder)

    # Define the path to the subject's MNINonLinear folder where task results are stored.
    mninonlinear_folder = os.path.join(subject_directory, subject_folder, "MNINonLinear/Results")
    
    # Iterate over each task folder within the subject's MNINonLinear folder.
    for task_folder in task_folders:
        
        # Define the path to the specific task subfolder.
        task_subfolder = os.path.join(mninonlinear_folder, task_folder)
        
        # Define the output directory for the current task's processed data.
        task_subfolder_output = os.path.join(subject_directory_output, task_folder)
        
        # Create the output directory for the task if it doesn't exist.
        if not os.path.exists(task_subfolder_output):
            try:
                os.makedirs(task_subfolder_output)
            except Exception as e:
                print('error:', e)
                continue
        
        # Check if the task subfolder is a valid directory.
        if os.path.isdir(task_subfolder):
            # Define the path to the input fMRI data file.
            input_file = os.path.join(task_subfolder, task_folder + ".nii.gz")
            
            # Define the output file path where the MNI152 transformed data will be saved.
            output_file = os.path.join(task_subfolder_output, subject_folder + "_" + task_folder + "_MNI.nii.gz")
            print("output_file", output_file)
            
            # Construct the flirt command to align the input file to the MNI152 template.
            command = f"flirt -in {input_file} -ref {ref_file} -out {output_file} -applyxfm -init $FSLDIR/etc/flirtsch/ident.mat"
            
            # Execute the flirt command.
            subprocess.run(command, shell=True)
            print('Done: ', input_file)

"""
The loop breaks after processing the first task folder and the first subject folder.
This is for testing purposes, and the breaks should be removed to process all subjects and tasks.
"""
       # break  # Remove this break statement to process all tasks.
   # break  # Remove this break statement to process all subjects.
