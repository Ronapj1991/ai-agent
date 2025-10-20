import os

from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    wd_path = os.path.abspath(working_directory) 
    fp_full = os.path.abspath(os.path.join(wd_path, file_path))
    
    if os.path.commonpath([wd_path, fp_full]) != wd_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    os.makedirs(os.path.dirname(fp_full), exist_ok=True)
    try:
        with open(fp_full, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file with the given text content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write."
            )
        }
    )
)
    