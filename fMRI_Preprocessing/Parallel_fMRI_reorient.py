from concurrent.futures import ProcessPoolExecutor
import subprocess

def process_task(input_file, output_file, ref_file):
    command = f"flirt -in {input_file} -ref {ref_file} -out {output_file} -applyxfm -init $FSLDIR/etc/flirtsch/ident.mat"
    subprocess.run(command, shell=True)

# Adjust the number of workers according to your CPU's core count.
with ProcessPoolExecutor(max_workers=4) as executor:
    for subject_folder in os.listdir(subject_directory):
        mninonlinear_folder = os.path.join(subject_directory, subject_folder, "MNINonLinear/Results")
        
        for task_folder in task_folders:
            task_subfolder = os.path.join(mninonlinear_folder, task_folder)
            task_subfolder_output = os.path.join(subject_directory_output, task_folder)
            
            if not os.path.exists(task_subfolder_output):
                try:
                    os.makedirs(task_subfolder_output)
                except Exception as e:
                    print('error:', e)
                    continue
            
            if os.path.isdir(task_subfolder):
                input_file = os.path.join(task_subfolder, task_folder + ".nii.gz")
                output_file = os.path.join(task_subfolder_output, subject_folder + "_" + task_folder + "_MNI.nii.gz")
                print("output_file", output_file)
                
                # Submit the task to the executor for parallel processing.
                executor.submit(process_task, input_file, output_file, ref_file)
