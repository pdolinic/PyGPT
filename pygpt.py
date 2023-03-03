#!/usr/bin/env python3

# Idea of Shell Variant & Blogpost from SAKATA: https://medium.com/geekculture/2022-how-to-use-chatgpt-api-with-curl-88830dec8a65
# Asciart from: https://patorjk.com/software/taag/#p=testall&h=2&v=1&c=bash&f=Graffiti&t=pygpt
# The following Python3 modified Code was AI-assisted with GPT3, for GPT3!

import sys
import requests
import json

# Set model 
model = "gpt-3.5-turbo"

# Set api key file & api key path 
api_key_file = "my_api_key.txt"
api_key_path = f"/usr/local/bin/{api_key_file}"

with open(api_key_path, "r") as f:
    my_api_key = f.read().strip()

print("--------------------------------------------------------------------------------------------")
print(r"""
  .----.-.  .-.---..----. .---.
  | {}  } \/ /   __} {}  |_   _}
  | .--' }  {\  {_ } .--'  | |
  `-'    `--' `---'`-'     `-'
      """)
print("--------------------------------------------------------------------------------------------")

if len(sys.argv) < 2:
    print("Usage: python3 pygpt.py prompt1 prompt2 prompt3 ...")
    sys.exit(1)

prompts = sys.argv[1:]

json_data = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
        for prompt in prompts
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_api_key}"
    },
    json=json_data
)

if response.status_code == 200:
    output = response.json()
    #print(json.dumps(output, indent=4))

    if "choices" in output:
        for choice in output["choices"]:
            if "message" in choice and "content" in choice["message"]:
                content = choice["message"]["content"]
                print(content)
            else:
                print("No response generated")
    else:
        print("Error: no choices in output")

    debugging_fields = {}

    if "id" in output:
        debugging_fields["id"] = output["id"]
    if "object" in output:
        debugging_fields["object"] = output["object"]
    if "created" in output:
        debugging_fields["created"] = output["created"]
    if "model" in output:
        debugging_fields["model"] = output["model"]

    print("--------------------------------------------------------------------------------------------")
    print("Debugging fields:", json.dumps(debugging_fields, indent=4))

else:
    print("Error: {} {}".format(response.status_code, response.reason))
