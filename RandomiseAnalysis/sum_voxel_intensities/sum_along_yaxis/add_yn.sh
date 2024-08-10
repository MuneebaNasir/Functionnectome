#!/bin/bash

# Load the FSL module, required for FSL commands used in the script
module load fsl/6.0.4

# Define the path to the subject folder containing the randomise analyses results
subject_folder="/data/extra/mnasir/scripts/Func_results_feb_2024/Association_Probabilistic/s4d_files/ttest_BAR1_s4d"

# Initialize an empty array to store file paths
file_paths=()

# Loop through each x-axis index (1 to 64) for the current y-axis
for ((x=1; x<=64; x++)); do
    # Construct the path to the current 4D NIfTI file for the given x and y
    file="$subject_folder/datax${x}y${y}/4d_x${x}y${y}.nii.gz"
    
    # Check if the file exists
    if [[ -f "$file" ]]; then
        # Add the file path to the array if it exists
        file_paths+=("$file")
    fi
done

# If there are any files in the file_paths array
if [[ ${#file_paths[@]} -gt 0 ]]; then
    # Define the output file path where the resulting image will be saved
    output_file="$subject_folder/data_y_xn_add/4d_y${y}xn.nii.gz"

    # Initialize the command for fslmaths with the first file in the array
    command="fslmaths ${file_paths[0]}"

    # Loop through the remaining files and build the add command for fslmaths
    for ((i=1; i<${#file_paths[@]}; i++)); do
        command+=" -add ${file_paths[i]}"
    done

    # Add the output file path to the fslmaths command
    command+=" $output_file"

    # Execute the constructed command to combine the images
    eval "$command"
fi
