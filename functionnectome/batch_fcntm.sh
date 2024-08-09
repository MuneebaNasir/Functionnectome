#!/bin/bash

# This script submits batch jobs to process functionectome analyses in parallel.
# It iterates through each .fcntm file in the specified directory and submits a job to the SLURM scheduler.
# Jobs are allocated to different partitions based on a counter to manage resource usage.

# Initialize counter for highmem partition to track the number of jobs submitted to each partition.
highmem_count=0

# Iterate through each .fcntm file in the specified directory.
# Adjust the directory path as needed for your setup.
for fcntm_file in /homes_unix/mnasir/Functionnectome-main/Functionnectome/Path_tfMRI_RETCCW_7T_AP/*.fcntm; do
    echo "Processing file: $fcntm_file"
    
    # Determine which partition to use based on the counter.
    # Allocate jobs to partitions to manage resource usage and avoid overloading a single partition.
    if [ $highmem_count -lt 4 ]; then
        # Use 'highmem' partition for the first 4 jobs to ensure high-memory resources.
        partition="highmem"
        ((highmem_count++))
    elif [ $highmem_count -lt 8 ]; then
        # Use 'normal' partition for the next set of jobs to distribute the load.
        partition="normal"
        ((highmem_count++))
    else
        # Use 'gindev' partition for remaining jobs if more than 8 jobs have been allocated.
        partition="gindev"
    fi

    # Submit a job to the SLURM scheduler for each .fcntm file.
    # - --job-name: Set the job name to the .fcntm file name for easy identification.
    # - --export: Pass the .fcntm file path as an environment variable to the job script.
    # - --partition: Specify the partition based on the counter value.
    # - --mem: Request 35 GB of memory for the job.
    # Ensure that 'run_fcntm.sh' script is correctly configured to process the .fcntm file.
    sbatch --job-name="$fcntm_file" --export=fcntm_file="$fcntm_file" --partition=$partition --mem=35000 run_fcntm.sh

done
