import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory_abs, file_path)
    
    if os.path.commonpath([working_directory_abs, os.path.abspath(full_path)]) != working_directory_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    py_file = [sys.executable, full_path, *args]
    try:
        completed_process = subprocess.run(
                py_file,
                timeout=30,
                capture_output=True,
                cwd=working_directory_abs,
                text=True
            )
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    out = completed_process.stdout.strip()
    err = completed_process.stderr.strip()
    err_code = completed_process.returncode
    
    output = f"STDOUT: {out}\nSTDERR: {err}"
    if err_code != 0:
        output += f"\nProcess exited with code {err_code}"
    if not out and not err:
        output = "No output produced."
    
    return output