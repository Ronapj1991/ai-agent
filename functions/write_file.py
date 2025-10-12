import os

def write_file(working_directory, file_path, content):
    wd_path = os.path.abspath(working_directory) 
    fp_full = os.path.abspath(file_path)
    
    if not fp_full.startswith(wd_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    pass