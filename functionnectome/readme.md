
# Functionnectome Batch Processing

## Overview

The `Functionnectome` is a Python package designed for applying a method that combines functional signals from distant voxels in a classical fMRI 4D volume, utilizing probabilistic structural relationships provided by anatomical priors of the involved brain circuits. 

For more details on the `Functionnectome` package, visit its [GitHub repository](https://github.com/NotaCS/Functionnectome).

### Additional Tool

**WhiteRest**: A tool included with the `Functionnectome` package to explore the impact of white matter lesions on resting-state networks. It is based on the WhiteRest atlas. More information can be found in the WhiteRest manual.

### Documentation

The complete manual is available on the project's GitHub page under the name [The_Functionnectome_Userguide.pdf](https://github.com/NotaCS/Functionnectome).

## Scripts

This repository contains three main scripts for setting up and running `Functionnectome` analyses:

1. **Generating_Input_files.py**
2. **run_fcntm.sh**
3. **batch_fcntm.sh**

### 1. Generating_Input_files.py

This Python script generates `.fcntm` files required for `Functionnectome` analysis. Each `.fcntm` file contains paths to NIFTI (converted into MNI152 standard, 2mm resolution) data files and configuration parameters for the analysis.

#### Main Code Snippets

- **Define Directory and Get Files**
  ```python
  directory = "/data/extra/mnasir/scripts/NIFTI_DATA/2_MNIFormat_23_6/tfMRI_RETCCW_7T_AP"
  files = os.listdir(directory)
  files.sort()
  ```

  Sets the directory containing NIFTI files and retrieves a sorted list of files.

- **Create .fcntm Files**
  ```python
  for i in range(num_text_files):
      start_index = i * files_per_text_file
      end_index = min((i + 1) * files_per_text_file, len(files))
      with open(os.path.join(output_directory, f"{i+1}_file_paths.fcntm"), "w") as f:
          f.write("Output folder:\n\t/data/extra/mnasir/scripts/Func_results_feb_2024/tfMRI_RETCCW_7T_AP\n")
          # Additional configuration parameters...
          for file_name in files[start_index:end_index]:
              f.write(os.path.join(directory, file_name) + "\n")
          # Mask file path...
  ```

  Creates `.fcntm` files with the specified number of NIFTI files per configuration file and writes the necessary parameters for the analysis.

### 2. run_fcntm.sh

This shell script sets up the environment and runs the `functionnectome.py` script using Python 3.10. It uses Anaconda to ensure the correct Python version and dependencies.

#### Main Code Snippets

- **Setup Environment and Run Analysis**
  ```bash
  export PATH="/srv/shares/softs/anaconda3_v23/bin:$PATH"
  python3.10 functionnectome.py $fcntm_file
  ```

  Adds Anaconda to the `PATH` and executes the `functionnectome.py` script with the `.fcntm` file as an argument.

### 3. batch_fcntm.sh

This shell script submits batch jobs to a SLURM scheduler for processing multiple `.fcntm` files in parallel. It manages job allocation to different partitions based on the number of jobs submitted.

#### Main Code Snippets

- **Submit Jobs to SLURM**
  ```bash
  for fcntm_file in /homes_unix/mnasir/Functionnectome-main/Functionnectome/Path_tfMRI_RETCCW_7T_AP/*.fcntm; do
      if [ $highmem_count -lt 4 ]; then
          partition="highmem"
          ((highmem_count++))
      elif [ $highmem_count -lt 8 ]; then
          partition="normal"
          ((highmem_count++))
      else
          partition="gindev"
      fi
      sbatch --job-name="$fcntm_file" --export=fcntm_file="$fcntm_file" --partition=$partition --mem=35000 run_fcntm.sh
  done
  ```

  Iterates through `.fcntm` files, selects an appropriate SLURM partition, and submits jobs for each file.

## Installation

To use `Functionnectome`, ensure it is installed on your system. You can install it using pip by following the instructions on its [GitHub page](https://github.com/NotaCS/Functionnectome). 

Once installed, you can launch the `Functionnectome` GUI using:
```bash
FunctionnectomeGUI
```
Or run an analysis with a settings file using:
```bash
Functionnectome <setting_file.fcntm>
```

