import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    wd = os.path.abspath(working_directory)
    if not full_path.startswith(wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

get_files_info("mydir", "new_folder")