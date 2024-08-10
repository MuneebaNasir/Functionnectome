

# fMRI Randomise Analysis 

## Overview

The workflow includes batch processing of fMRI data to perform statistical t-tests and summing voxel intensities across multiple nifti files.
The workflow is explained below.

## Folder Structure

- **`Randomise`**: Contains scripts for performing t-test analysis and merging results.
- **`sum_voxel_intensities`**: Contains scripts for summing voxel intensities along the x-axis.
  - **`sum_along_yaxis`**: Scripts for summing 4D files along the x-axis.
  - **`sum_along_circle`**: Scripts for summing 4D files along circle based on circle stimuli.
  - **`sum_along_bar`**: Scripts for summing 4D files along wedges based on bar stimuli.


## 1. /Randomise

### Scripts
- **`Parallel_batch_randomise.sh`** 
  - **Function**: Submits Slurm jobs to process data for each `x`-axis value across all `y`-axis values.
  - **Result**:
    
- **`randomise.sh`**
  - **Function**: Processes stimulus `.mat` files and associated `.nii.gz` files for all `y`-axis values corresponding to a specific `x`-axis value.
  - **Result**:

### How to Use

1. Place `.mat` and `.nii.gz` files in the specified directories.
2. Run the Slurm script to begin processing:
   ```bash
   sbatch Parallel_batch_randomise.sh
   ```
3. Monitor job progress with Slurm commands like `squeue`.


## 2. /sum_voxel_intensities/sum_along_yaxis

## Scripts

- **`Parallel_Batch_add_xn.sh`**:
  - **Function**: Submits SLURM jobs to process files for each `y` index.
  - **Result**:
  
- **`add_xn.sh`**:
  - **Function**: Sums voxel intensities along the x-axis using `fslmaths`.
  - **Result**: Outputs files named `4d_x64yn.nii.gz`.

### How to Use

1. Ensure FSL and SLURM are configured.
2. Submit the main script using:
   ```bash
   sbatch Parallel_Batch_add_xn.sh
   ```


## Example Workflow

1. **Perform Randomise Analysis**:
   ```bash
   sbatch batch_processing/Parallel_batch_randomise.sh
   ```

2. **Sum Voxel Intensities**:
   ```bash
   sbatch sum_voxel_intensities/Parallel_Batch_add_xn.sh
   ```

3. **Apply Stimulus-Specific Summing**:
   - Use appropriate scripts from `sum_along_xaxis`, `sum_along_circle`, or `sum_along_bar` based on your stimulus type.

## Prerequisites

- **Slurm**: For job scheduling.
- **FSL 6.0.4**: Required for running `randomise` and `fslmaths`.
- **Data Path**: Ensure stimulus files and NIfTI files are in the correct directories.

## Monitoring and Results

- **Monitor Jobs**: Use Slurm commands such as `squeue` to check job statuses.
- **Review Results**: Check output directories for resulting NIfTI files as specified in the scripts.
