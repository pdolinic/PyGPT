# Idea of Shell Variant & Blogpost from SAKATA: https://medium.com/geekculture/2022-how-to-use-chatgpt-api-with-curl-88830dec8a65

# The following Python3 modified Code was AI-assited with GPT, for GPT
# Below replace my_api_key with your API-Key

#!/usr/bin/env python3

import sys
import requests
import json

if len(sys.argv) != 3:
    print("Usage: python script.py prompt temperature")
    sys.exit(1)

keyword = sys.argv[1]
temperature = float(sys.argv[2])

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer my_api_key"
}

data = {
    "model": "text-davinci-003",
    "prompt": keyword,
    "max_tokens": 4000,
    "temperature": temperature
}

response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)

output = response.json()

for choice in output["choices"]:
    print(choice["text"].strip())

debugging_fields = {
    "id": output["id"],
    "object": output["object"],
    "created": output["created"],
    "model": output["model"]
}

print("Debugging fields:", json.dumps(debugging_fields))
