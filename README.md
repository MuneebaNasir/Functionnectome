
#  Finding impact of White Matter Connectivity on Brain Functions and Structure in Visual Processing. 

## Overview

This repository contains a series of scripts and tools for processing and analyzing fMRI data. The workflow includes preprocessing stimuli, converting neuroimaging data to a standard space, performing functional connectivity analyses, and applying statistical analyses. The pipeline is designed to work with fMRI data and involves several steps to ensure accurate and comprehensive analysis. 
For further information and results, see the [thesis report](https://drive.google.com/file/d/1qRR232acUeL-FRPvsEP3Ti2wympBlMqA/view).


## Project Structure

- **`Stimulus Preprocessing`**: Downsample stimulus data and prepare it for analysis.
- **`fMRI Preprocessing`**: Convert fMRI data to MNI152 standard space.
- **`Functionnectome Analyses`**: Apply functional connectivity analyses using the Functionnectome package.
- **`Randomise Analysis`**: Perform statistical analyses and sum voxel intensities across multiple NIfTI files.

## Step-by-Step Workflow

### Step 1: Stimulus Preprocessing

**Objective**: Process and downsample stimulus files.

1. **Downsampling Script** (`1_downsampling.py`):
   - **Description**: Downsamples a 3D matrix of video frames from a MATLAB `.mat` file and converts it to text files. Each text file contains time series data for specific pixels.
   - **Usage**: Modify file paths in the script, then run to generate text files.

2. **Text to MAT Conversion Script** (`2_text_mat.py`):
   - **Description**: Converts text files to MAT files using the `Text2Vest` utility from FSL.
   - **Usage**: Ensure FSL is configured, modify paths, then run to convert text files.

3. **Downsampled Data Visualization Script** (`view_downsampled.py`):
   - **Description**: Visualizes the downsampled data by creating a video.
   - **Usage**: Modify file paths, then run to generate a video of the downsampled data.

### Step 2: fMRI Preprocessing

**Objective**: Convert subject-specific fMRI data to MNI152 standard space.

- **Script** (`reorient_fMRI.py`):
  - **Description**: Uses the FSL tool `flirt` to reorient fMRI data files.
  - **Usage**: Set directory paths and task folders, ensure FSL is configured, then run the script to process fMRI data.

### Step 3: Functionnectome Analyses

**Objective**: Apply functional connectivity analyses using the Functionnectome package.

1. **Generating Input Files Script** (`Generating_Input_files.py`):
   - **Description**: Creates `.fcntm` files required for Functionnectome analysis.
   - **Usage**: Modify directory paths and file settings, then run to generate `.fcntm` files.

2. **Run Functionnectome Script** (`run_fcntm.sh`):
   - **Description**: Executes the Functionnectome analysis.
   - **Usage**: Ensure Anaconda and the correct Python version are set up, then run the script to start the analysis.

3. **Batch Processing Script** (`batch_fcntm.sh`):
   - **Description**: Submits batch jobs to a SLURM scheduler for parallel processing of `.fcntm` files.
   - **Usage**: Submit the script to SLURM for parallel job processing.

### Step 4: Randomise Analysis

**Objective**: Perform statistical t-tests and sum voxel intensities.

1. **Randomise Analysis Scripts**:
   - **`Parallel_batch_randomise.sh`**: Submits SLURM jobs for processing across `x`-axis values for all `y`-axis values.
   - **`randomise.sh`**: Processes `.mat` and `.nii.gz` files for specific axes.

2. **Sum Voxel Intensities Scripts**:
   - **`Parallel_Batch_add_xn.sh`**: Submits SLURM jobs to sum voxel intensities for each `y` index.
   - **`add_xn.sh`**: Sums voxel intensities along the x-axis.

### Execution Order

1. **Run Stimulus Preprocessing**:
   - Execute `1_downsampling.py` to downsample and convert stimulus data.
   - Run `2_text_mat.py` to convert text files to MAT files.
   - Generate a video of the downsampled data using `view_downsampled.py`.

2. **Perform fMRI Preprocessing**:
   - Run `reorient_fMRI.py` to preprocess fMRI data into MNI152 standard space.

3. **Conduct Functionnectome Analyses**:
   - Generate `.fcntm` files using `Generating_Input_files.py`.
   - Execute the Functionnectome analysis with `run_fcntm.sh`.
   - Submit batch jobs using `batch_fcntm.sh`.

4. **Apply Randomise Analysis**:
   - Perform statistical t-tests and voxel intensity summation with scripts in the `/Randomise` and `/sum_voxel_intensities` directories.

## Prerequisites

- **Python 3.x**: Required for script execution.
- **FSL**: Required for neuroimaging preprocessing and randomise analysis.
- **SLURM**: Required for job scheduling in batch processing.
- **Functionnectome**: Required for functional connectivity analysis.

## Installation

1. Install Python packages and dependencies as specified in each script.
2. Ensure FSL and SLURM are installed and configured properly.
3. Install the Functionnectome package using pip:
   ```bash
   pip install Functionnectome
   ```

## Monitoring and Results

- **Monitor Jobs**: Use SLURM commands like `squeue` to check job statuses.
- **Review Results**: Check output directories for resulting NIfTI files, `.fcntm` files, and other generated data.

## Documentation and References

- [Functionnectome GitHub Repository](https://github.com/NotaCS/Functionnectome)
- [FSL Documentation](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/install/index)
- [The_Functionnectome_Userguide.pdf](https://github.com/NotaCS/Functionnectome)

