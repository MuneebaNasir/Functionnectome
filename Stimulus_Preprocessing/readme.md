

# Stimulus Preprocessing Scripts

This repository contains Python scripts for processing a stimulus file from a MATLAB `.mat` file. The processing involves downsampling a 3D matrix of video frames, converting the downsampled data to text files, and converting these text files to MAT files. Additionally, there is a script to visualize the downsampled data as a video.

## Scripts

### 1. Downsampling Script: `1_Downsampling.py`

**Description:**  
This script processes a stimulus file containing a 3D matrix of video frames from a MATLAB `.mat` file. It downsamples the matrix from `300x300x300` to `64x64x300` dimensions and converts the downsampled data into text files. Each text file corresponds to a specific pixel in the `64x64` frame and contains a time series of `300` timepoints.

**Dependencies:**
- `numpy`
- `h5py`
- `scipy`
- `os`

**Usage:**
1. Replace the `mat_file` variable with the path to your `.mat` file.
2. Replace the `out_dir` variable with the desired output directory for the text files.
3. Run the script to generate the text files.

**Code Explanation:**

1. **Load the MATLAB `.mat` file:**

    ```python
    import h5py
    mat_file = h5py.File('/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat', 'r')
    ```

    This code snippet opens the `.mat` file using the `h5py` library.

2. **Access and retrieve data:**

    ```python
    data = mat_file['stim']
    downsampled_data = data[()]
    mat_file.close()
    ```

    This retrieves the data from the specified variable (`'stim'`) and converts it to a NumPy array.

3. **Downsample the data:**

    ```python
    from scipy.ndimage import zoom
    target_size = (64, 64)
    resized_data = np.zeros((downsampled_data.shape[0], target_size[0], target_size[1]))
    for t in range(downsampled_data.shape[0]):
        resized_data[t] = zoom(downsampled_data[t], (target_size[0] / downsampled_data.shape[1], target_size[1] / downsampled_data.shape[2]), order=1)
    ```

    This code downsamples each time frame of the data to the target size using the `zoom` function from `scipy.ndimage`.

4. **Save data to text files:**

    ```python
    for x in range(target_size[0]):
        for y in range(target_size[1]):
            filename = f"{out_dir}/textfilex{x + 1}y{y + 1}.txt"
            with open(filename, "w") as file:
                for t in range(300):
                    file.write(str(resized_data[t, x, y]) + "\n")
    ```

    This loop iterates over each pixel location and writes the time series data to text files named according to their pixel coordinates.

---

### 2. Text to MAT Conversion Script: `2_text_mat.py`

**Description:**  
This script converts text files into MAT files using the `Text2Vest` command-line utility provided by the FSL module. It assumes that the FSL module is available and that `Text2Vest` is installed.

**Dependencies:**
- FSL (FMRIB Software Library)
- `Text2Vest` utility from FSL

**Usage:**
1. Ensure that the FSL module is available and properly configured.
2. Modify the `directory` variable to point to the location of the input text files.
3. Modify the `out_dir` variable to specify the output directory for MAT files.
4. Run the script to convert each text file to a MAT file.

**Code Explanation:**

1. **Load the FSL module:**

    ```python
    import subprocess
    subprocess.run("module load fsl/6.0.4", shell=True, check=True)
    ```

    This command loads the FSL module required for `Text2Vest`.

2. **Process each text file:**

    ```python
    directory = '/data/extra/mnasir/scripts/textfiles_row_stimuli_RETCCWsmall'
    out_dir = '/data/extra/mnasir/scripts/matfiles_row_stimuli_RETCCWsmall'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for x in range(64):
        for y in range(64):
            input_filename = f"textfilex{x + 1}y{y + 1}.txt"
            output_filename = f"datax{x + 1}y{y + 1}.mat"
            input_path = os.path.join(directory, input_filename)
            output_path = os.path.join(out_dir, output_filename)
            command = f"Text2Vest {input_path} {output_path}"
            subprocess.run(command, shell=True, check=True)
            print(f'Processed x: {x}, y: {y}')
    ```

    This code iterates over a grid of text files and uses `Text2Vest` to convert each text file to a MAT file, saving them to the specified output directory.

---

### 3. Downsampled Data Visualization Script: `view_downsampled.py`

**Description:**  
This script processes a stimulus file from a MATLAB `.mat` file by downsampling it and converting the downsampled data into a video for cross-verification.

**Dependencies:**
- `imageio`
- `numpy`
- `h5py`
- `scipy`

**Usage:**
1. Replace the `mat_file_path` variable with the path to your `.mat` file.
2. Replace the `output_file` variable with the path where you want to save the video.
3. Run the script to generate the video.

**Code Explanation:**

1. **Load the MATLAB `.mat` file:**

    ```python
    import h5py
    mat_file_path = '/data/extra/mnasir/drive/analyzePRFcode/osfstorage-archive/apertures/RETCCWsmall.mat'
    mat_file = h5py.File(mat_file_path, 'r')
    ```

    This opens the `.mat` file using `h5py`.

2. **Downsample the data:**

    ```python
    from scipy.ndimage import zoom
    target_size = (64, 64)
    resized_data = np.zeros((downsampled_data.shape[0], target_size[0], target_size[1]))
    for t in range(downsampled_data.shape[0]):
        resized_data[t] = zoom(downsampled_data[t], (target_size[0] / downsampled_data.shape[1], target_size[1] / downsampled_data.shape[2]), order=1)
    ```

    This snippet downsamples each time frame of the data to `64x64` dimensions.

3. **Create and save the video:**

    ```python
    import imageio
    output_file = '/data/extra/mnasir/scripts/downsampled_64_video_RETCCWsmall.mov'
    writer = imageio.get_writer(output_file, codec='png', fps=30)
    for t in range(resized_data.shape[0]):
        frame = resized_data[t]
        writer.append_data(frame)
    writer.close()
    print(f"Video saved as {output_file}")
    ```

    This code creates a video from the downsampled frames and saves it to the specified output path.

---

## General Notes

- Ensure that all dependencies are installed and properly configured in your environment before running the scripts.
- Modify file paths and directory names as needed to suit your file structure and requirements.

