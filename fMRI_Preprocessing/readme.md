# Neuroimaging Data Pre-Processing Script

This Python script processes neuroimaging data by converting subject-specific fMRI data files to the MNI152 standard space using the FSL tool `flirt`. It is intended to be run on a Linux-based system where FSL is installed and configured.

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed.
- **FSL (FMRIB Software Library) version 6.0.4**: Ensure FSL is installed and configured properly.
- **Environment Setup**: The FSL module should be loaded in your environment.

## Setup and Configuration

### Directory Paths

Update the `subject_directory` and `subject_directory_output` variables in the script to match your data paths:

```python
# Define the directory containing the subject data files.
subject_directory = "/data/extra/mnasir/scripts/NIFTI_DATA/1_unzipfiles_NIFT"

# Define the directory where the output files will be stored.
subject_directory_output = "/data/extra/mnasir/scripts/NIFTI_DATA/MNI152_NIFT"
```

## Task Folders
Modify the task_folders list to include all the task-specific folders you want to process:

``` python

# List of task folders to process. Add more tasks as needed.
task_folders = ["tfMRI_RETBAR1_7T_AP"]
```
## Reference File
The script uses the MNI152 standard brain template file. Ensure the path to MNI152_T1_2mm_brain.nii.gz is correct:

``` python

# Define the path to the MNI152 standard brain template file.
ref_file = "$FSLDIR/data/standard/MNI152_T1_2mm_brain.nii.gz"
```
## Usage
Running the Script
Execute the script using Python 3:

``` bash

python3 reorient_fMRI.py
```
## Script Execution
The script performs the following actions:

Loads the FSL module required for the flirt tool.
Verifies the availability of the flirt tool.
Converts subject-specific fMRI data files to the MNI152 standard space.
Saves the output files in the specified output directory.
## Sample Output
The output files will be saved with the following naming convention:

``` plaintext

<subject_folder>_<task_folder>_MNI.nii.gz
```
For example:

``` plaintext

100307_tfMRI_RETBAR1_7T_AP_MNI.nii.gz
```
## Code Overview
Loading FSL Module
The script begins by loading the required FSL module:

``` python

import subprocess

# Load the FSL module required for using the flirt tool.
subprocess.run("module load fsl/6.0.4", shell=True)
subprocess.run("which flirt", shell=True)  # Verifies the flirt tool is available.
subprocess.run("flirt", shell=True)  # Runs flirt to verify that it is properly loaded.
```
## Directory and Task Configuration
Set the paths to your subject data directory and output directory:

``` python

# Define the directory containing the subject data files.
subject_directory = "/data/extra/mnasir/scripts/NIFTI_DATA/1_unzipfiles_NIFT"

# Define the directory where the output files will be stored.
subject_directory_output = "/data/extra/mnasir/scripts/NIFTI_DATA/MNI152_NIFT"

# Create the output directory if it doesn't exist.
if not os.path.exists(subject_directory_output):
    os.makedirs(subject_directory_output)
```

## Note on Script Testing
In the presence of 'break' statement, the loop will finish after processing the first task folder and the first subject folder, this is for testing purposes. To process all subjects and tasks, donot uncomment the remove the break statements:

``` python
# break  # Remove this break statement to process all tasks.

# break  # Remove this break statement to process all subjects.
```

## Additional Information
For more details on the flirt tool and the FSL library, refer to the [FSL Documentation.](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/install/index)

