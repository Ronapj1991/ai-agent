import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
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
    
    generate_content(client, messages, user_prompt)

def has_verbose(end_of_sysargv):
    return end_of_sysargv == "--verbose"

def verbose_print(user_prompt, prompt_tokens, response_tokens):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

def generate_content(client, messages, user_prompt):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )

    if has_verbose(sys.argv[-1]):
        verbose_print(user_prompt, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count)

    print(response.text)

if __name__ == "__main__":
    main()
