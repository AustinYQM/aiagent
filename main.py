import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
parser = argparse.ArgumentParser()
api_key = os.environ.get("GEMINI_API_KEY")

parser.add_argument("prompt")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity",)
args = parser.parse_args()

client = genai.Client(api_key=api_key)

messages = []
if not args.prompt:
    sys.exit(1)
else:
    messages.append(types.Content(role="user", parts=[types.Part(text=args.prompt)]))


client_model = "gemini-2.0-flash-001"

response = client.models.generate_content(
    model=client_model,
    contents=messages
)
if args.verbose:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
