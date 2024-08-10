
# Summing Voxel Intensities Along Y Axis

This documentation describes two SLURM batch scripts designed to perform voxel-wise addition of NIfTI images, summing the intensity values for each voxel across multiple images.


## Scripts

### `Parallel_Batch_add_xn.sh`

- **Function**: Submits SLURM jobs to process files for each `y` index.
- **Creates**: it run 64 sbatch commands for a different value of y ranging from 1-64.
### `add_xn.sh`

- **Function**: Processes files for a specific `y` index by summing voxel intensities along the `x` axis using `fslmaths`.
- **Result**: For each `y` index, the result is a single NIfTI file named `y1xn.nii.gz`, which is the sum of files `y1x1.nii.gz`, `y1x2.nii.gz`, ..., `y1x64.nii.gz`.



## Usage

1. **Prepare Environment**:
   - Ensure that the FSL module is available on your system.
   - Verify that SLURM is configured for job scheduling on your high-performance computing cluster.

2. **Submit the Main Script**:
   - Run `Parallel_Batch_add_xn.sh` to initiate the batch processing for all `y` indices.
   ```bash
   sbatch Parallel_Batch_add_xn.sh
   ```

3. **SLURM Job Execution**:
   - This will submit 64 SLURM jobs, each processing files for a different `y` index. Each job will run the `add_xn.sh` script.

4. **Processing**:
   - Each `add_xn.sh` job will sum the voxel intensities of all `x`-indexed files for its specific `y` index, creating an output file for each `y` index.

5. **Review Results**:
   - Check the output directory specified in `Parallel_Batch_add_xn.sh` for the resulting NIfTI files. Each file will be named in the format `4d_y64xn.nii.gz`, where `y` corresponds to the specific index.

