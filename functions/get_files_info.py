import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    wd = os.path.abspath(working_directory)
    
    if not full_path.startswith(wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    
    

def contents_str_builder(full_path):
    dir_contents = ""
    for file in os.listdir(full_path):
        file_path = os.path.join(full_path, file)
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        dir_contents += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return dir_contents