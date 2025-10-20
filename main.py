import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

def main():
    load_dotenv() #pulls the API key from .env
    
    args = sys.argv[1:] #returrns a list of arguments. Each item will be what is after the script name when ran
    
    if not args: 
        print("Usage: uv run main.py <prompt>")
        sys.exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY") #if not for load_dotenv this will return None
    client = genai.Client(api_key=api_key) # instantiate Google Generative AI Python SDK package with my own API key
    
    user_prompt = " ".join(args) # turns everything after the script name into one string
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]) #found in https://googleapis.github.io/python-genai/genai.html#genai.types.ApiAuthApiKeyConfigDict under genai.live module
    ]
    
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file])
    generate_content(client, messages, user_prompt, system_prompt, available_functions)

def has_verbose(end_of_sysargv):
    return end_of_sysargv == "--verbose"

def verbose_print(user_prompt, prompt_tokens, response_tokens):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

def generate_content(client, messages, user_prompt, system_prompt, available_functions):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    if has_verbose(sys.argv[-1]):
        verbose_print(user_prompt, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count)
    
    if getattr(response, "function_calls", None):
        for fc in response.function_calls:
            print(f"Calling function: {fc.name}({fc.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
