import os
"""
 This script generates .fcntm files to be used as input for the functionectome analysis.
 Each .fcntm file will contain a list of file paths to NIFTI data files, along with other configuration parameters.
 The output will be stored in a specified directory.
"""

# Define the directory containing the NIFTI files.
directory = "/data/extra/mnasir/scripts/NIFTI_DATA/2_MNIFormat_23_6/tfMRI_RETCCW_7T_AP"

# Get a list of all files in the specified directory.
files = os.listdir(directory)

# Sort the list of files to ensure consistent ordering.
files.sort()

# Define the number of files that each .fcntm file will include.
files_per_text_file = 18

# Calculate the number of .fcntm files needed based on the total number of files.
num_text_files = (len(files) + files_per_text_file - 1) // files_per_text_file

# Specify the output directory where the .fcntm files will be saved.
output_directory = "/homes_unix/mnasir/Functionnectome-main/Functionnectome/Path_tfMRI_RETCCW_7T_AP"

# Create the output directory if it does not already exist.
os.makedirs(output_directory, exist_ok=True)

# Iterate through each group of files to create separate .fcntm files.
for i in range(num_text_files):
    # Determine the range of files to be included in this .fcntm file.
    start_index = i * files_per_text_file
    end_index = min((i + 1) * files_per_text_file, len(files))
    
    # Create a new .fcntm file with a unique name.
    with open(os.path.join(output_directory, f"{i+1}_file_paths.fcntm"), "w") as f:
        # Write documentation and parameters for functionectome analysis to the file.
        
        # Output folder where results will be stored.
        f.write("Output folder:\n\t/data/extra/mnasir/scripts/Func_results_feb_2024/tfMRI_RETCCW_7T_AP\n")
        
        # Analysis type: 'voxel' for voxel-based analysis.
        f.write("Analysis ('voxel' or 'region'):\n\tvoxel\n")
        
        # Number of parallel processes to use during the analysis.
        f.write("Number of parallel processes:\n\t8\n")
        
        # Format of priors stored: 'h5' for HDF5 format.
        f.write("Priors stored as ('h5' or 'nii'):\n\th5\n")
        
        # Specify the HDF5 priors used in the analysis.
        f.write("HDF5 priors:\n\tV2.P.Asso - Association, Probabilistic\n")
        
        # Position of the subjects ID in their path (e.g., the 7th element in the path).
        f.write("Position of the subjects ID in their path:\n\t7\n")
        
        # Whether to mask the output or not.
        f.write("Mask the output:\n\t1\n")
        
        # Write the number of subjects included in this .fcntm file.
        f.write(f"Number of subjects:\n\t{len(files[start_index:end_index])}\n")
        
        # Number of masks to be used.
        f.write("Number of masks:\n\t1\n")
        
        # List of paths to the subject's BOLD (Blood Oxygen Level Dependent) data files.
        f.write("Subject's BOLD paths:\n")
        for file_name in files[start_index:end_index]:
            f.write(os.path.join(directory, file_name) + "\n")
        
        # Specify the mask file used for voxelwise analysis.
        f.write("\nMasks for voxelwise analysis:\n")
        f.write("/data/extra/mnasir/scripts/Functionnectome-main/Functionnectome/gray_100_threshold_final.img.nii.gz\n")
