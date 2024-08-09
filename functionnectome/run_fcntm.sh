#!/bin/bash

# This script sets up the environment and runs the `functionnectome.py` script with a specified .fcntm file as input.
# Anaconda is used to ensure Python 3.10 is available and properly configured.
# If Python 3.10 is installed directly on your system, you can modify the script to use the system Python.

# Add the Anaconda binary directory to the PATH environment variable.
# This step allows the script to use Python 3.10 and related packages provided by Anaconda.
export PATH="/srv/shares/softs/anaconda3_v23/bin:$PATH"

# Run the `functionnectome.py` script using Python 3.10 from the Anaconda environment.
# The .fcntm file containing the input parameters for the analysis is passed as an argument.
# Ensure that `functionnectome.py` is located in the current directory or adjust the path to its location.
python3.10 functionnectome.py $fcntm_file

# If you have Python 3.10 installed directly on your system and do not need Anaconda, 
# you can use the following line instead of the one above:
# python3 functionnectome.py $fcntm_file
