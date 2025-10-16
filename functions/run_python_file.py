import os

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory_abs, file_path)
    
    if os.path.commonpath([working_directory_abs, os.path.abspath(full_path)]) != working_directory_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    pass