import os

def get_file_content(working_directory, file_path):
    wd_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(wd_path, file_path))
    if not full_path.startswith(wd_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    