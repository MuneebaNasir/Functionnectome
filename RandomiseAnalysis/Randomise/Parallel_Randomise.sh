#!/bin/bash

module load fsl/6.0.4  # Load FSL version 6.0.4 module

# This script processes stimulus files and performs randomise analysis using FSL.
# It is designed to work with the Slurm script `batch_merge_s4d_func_asso.sh`, 
# where a separate job is submitted for each `x`-axis value, looping over all `y` values.

# Set the path to the folder containing the stimulus .mat files
mat_folder="/data/extra/mnasir/scripts/matnewformat_stimuli"
cd "$mat_folder"

# Set the path to the folder containing the .nii files
nii_folder="/data/extra/mnasir/scripts/Func_results_feb_2024/Association_Probabilistic/s4d_files"

# Create an output folder name based on the analysis being performed
folder="ttest_BAR1_s4d"

# Set the base directory for the output files
output_base_dir="${nii_folder}/${folder}"

# Function to check if a directory exists and create it if not
make_directory() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
    fi
}

# Check if the output directory exists, and create it if it doesn't
make_directory "$output_base_dir"

# Loop over y-values for the specific x-value passed as an environment variable ($i)
for ((y=1; y<=64; y++)); do
    # Define the path to the .mat file corresponding to the current x and y values
    mat_file="${mat_folder}/datax${i}y${y}.mat"

    # Extract the filename of the .mat file without the extension
    mat_filename=$(basename "$mat_file" .mat)

    # Set the output directory name for the current .mat file
    output_dir="${output_base_dir}/${mat_filename}"

    # Check if the output directory exists, and create it if it doesn't
    make_directory "$output_dir"

    # Loop over all .nii.gz files in the nii_folder
    for nii_file in "${nii_folder}"/*.nii.gz; do
        # Extract the filename of the .nii file without the extension
        nii_filename=$(basename "$nii_file" .nii.gz)

        # Check if the output file already exists to avoid redundant processing
        if [ ! -f "${output_dir}/${nii_filename}_${mat_filename}" ]; then
            # Run the randomise command to perform the analysis
            randomise -i "$nii_file" -o "${output_dir}/${nii_filename}_${mat_filename}" -d "${mat_file}" -t "$mat_folder/design2.con" -m "$mat_folder/MNI152_mask" -n 1 -x -D
        else
            # If the output file already exists, skip the analysis for this combination
            echo "Output file ${output_dir}/${nii_filename}_${mat_filename} already exists. Skipping randomise."
        fi
    done

    # After processing all nii files, merge the results into a 4D file
    cd "$output_dir" || exit 1
    # Merge only the files matching the pattern "*_Tstat1.nii.gz", excluding corrected p-values files
    fslmerge -t "4d_${mat_filename}.nii.gz" $(ls | grep '_tstat1.nii.gz' | grep -v '_vox_corrp_tstat1.nii.gz')

    # Move back to the mat_folder for the next iteration
    cd "$mat_folder" || exit 1
done
