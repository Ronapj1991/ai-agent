import os
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file

wd = os.getcwd()

print(get_file_content(wd, "main.py"))
print(write_file(wd, "main.txt", "hello"))
print(run_python_file(wd, "main.py"))
print(get_files_info(wd, "pkg"))