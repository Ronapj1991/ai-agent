import os

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory_abs, file_path)
    
    if os.path.commonpath([working_directory_abs, os.path.abspath(full_path)]) != working_directory_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    pass