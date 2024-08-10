#!/bin/bash
#SBATCH --job-name=batch_merge_s4d_func_asso  # Set the job name for Slurm
#SBATCH --partition=highmem                   # Default partition for the job

# Load the FSL module version 6.0.4, necessary for subsequent analysis
module load fsl/6.0.4

# Initialize a counter to track the number of jobs assigned to the high memory partition
highmem_count=0

# Loop over each x-value from 1 to 64
for ((x=1; x<=64; x++)); do
    # Determine which partition to use based on the counter value
    if [ $highmem_count -lt 26]; then
        # If the counter is less than 26, assign to "highmem" partition
        partition="highmem"
        ((highmem_count++))  # Increment the high memory counter
    elif [ $highmem_count -lt 52 ]; then
        # If the counter is between 26 and 51, assign to "normal" partition
        partition="normal"
        ((highmem_count++))  # Continue incrementing the counter
    else
        # If the counter is 52 or more, assign to "gindev" partition
        partition="gindev"
    fi

    # Submit a Slurm job for each x-value using the determined partition
    # The job name is set based on the current x-value
    # The "parallel_merge_s4d_func_asso.sh" script will be executed with the current x-value as an environment variable
    sbatch --job-name="${x}_batch" --export=i="$x" --partition=$partition randomise.sh
done
