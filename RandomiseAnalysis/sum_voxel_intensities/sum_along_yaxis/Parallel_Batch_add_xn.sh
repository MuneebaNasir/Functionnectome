#!/bin/bash
#SBATCH --job-name=batch_merge_xn   # Name of the SLURM job
#SBATCH --partition=highmem # Partition to submit to

# Load the FSL module (FSL version 6.0.4)
module load fsl/6.0.4

# Define the path to the subject's folder
subject_folder="/data/extra/mnasir/scripts/Func_results_feb_2024/Association_Probabilistic/s4d_files/ttest_BAR1_s4d"

# create an output directory
output_file="$subject_folder/data_y_xn_add"
mkdir -p $output_file

# Loop through numbers 1 to 64
for ((y=1; y<=64; y++)); do
    # Submit a job to SLURM for each iteration
    # Pass the current value of 'y' to the script bar1_add_xn.sh
    sbatch --job-name="${y}bar1add" --export=y="$y" --partition=highmem add_xn.sh
done
