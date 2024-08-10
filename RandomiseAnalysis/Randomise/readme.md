
# Batch Processing for fMRI Analysis with Slurm and FSL

This folder contains two scripts designed to automate the t-test analysis of fMRI data using FSL's `randomise` tool within a Slurm-managed  environment.

## Overview

The workflow involves:
1. **`Parallel_batch_randomise.sh`** - Submits Slurm jobs to process data for each `x`-axis value across all `y`-axis values.
2. **`randomise.sh`** - Processes stimulus `.mat` files and associated `.nii.gz` files for all `y`-axis values corresponding to a specific `x`-axis value.

### `Parallel_batch_randomise.sh`

This script submits 64 jobs, each corresponding to an `x`-axis value. Jobs are distributed across different partitions (`highmem`, `normal`, `gindev`) to balance the workload.

#### Key Code Snippet:
```bash
for ((x=1; x<=64; x++)); do
    if [ $highmem_count -lt 26 ]; then
        partition="highmem"
    elif [ $highmem_count -lt 52 ]; then
        partition="normal"
    else
        partition="gindev"
    fi
    sbatch --job-name="${x}_batch" --export=i="$x" --partition=$partition randomise.sh
done
```

### `randomise.sh`

This script is run by each Slurm job to process all `y`-axis values for a given `x`-axis value. It performs t-tests using the FSL `randomise` tool and merges the results.

#### Key Code Snippet:
```bash
for ((y=1; y<=64; y++)); do
    mat_file="${mat_folder}/datax${i}y${y}.mat"
    for nii_file in "${nii_folder}"/*.nii.gz; do
        randomise -i "$nii_file" -o "${output_dir}/${nii_filename}_${mat_filename}" \
        -d "${mat_file}" -t "$mat_folder/design2.con" -m "$mat_folder/MNI152_mask" -n 1 -x -D
    done
    fslmerge -t "4d_${mat_filename}.nii.gz" $(ls | grep '_tstat1.nii.gz')
done
```

## Workflow

1. **Submit Jobs**: Run the `batch_merge_s4d_func_asso.sh` script to submit 64 jobs, each processing a different `x`-axis value.
   ```bash
   sbatch Parallel_batch_randomise.sh
   ```

2. **Job Processing**: Each job processes all `y`-axis values (`y=1` to `y=64`) for its assigned `x`-axis value, performing t-tests and merging results.

## Prerequisites

- **Slurm**: For job scheduling.
- **FSL 6.0.4**: Required for running `randomise`.
- **Data Path**: Stimulus files named `datax${i}y${y}.mat` and `.nii.gz` files in the correct folders.

## How to Use

1. Place `.mat` and `.nii.gz` files in the specified directories.
2. Run the Slurm script to begin processing:
   ```bash
   sbatch Parallel_batch_randomise.sh
   ```
3. Monitor job progress with Slurm commands like `squeue`.


