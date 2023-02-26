# Idea of Shell Variant & Blogpost from SAKATA: https://medium.com/geekculture/2022-how-to-use-chatgpt-api-with-curl-88830dec8a65
# Asciart from: https://patorjk.com/software/taag/#p=testall&h=2&v=1&c=bash&f=Graffiti&t=pygpt
# The following Python3 modified Code was AI-assisted with GPT, for GPT!

# Below replace my_api_key with your API-Key

#!/usr/bin/env python3

import sys
import requests
import json

print(r"""  
  .----.-.  .-.---..----. .---. 
  | {}  } \/ /   __} {}  |_   _}
  | .--' }  {\  {_ } .--'  | |  
  `-'    `--' `---'`-'     `-'  
      """)
print("----------------------------------------------"))

if len(sys.argv) != 3:
    print("Usage: python script.py prompt temperature")
    print('Example: python3 openai.py "Explain divide & conquer in C++, then show some code!" 1.0')
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

print("----------------------------------------------"))
print("Debugging fields:", json.dumps(debugging_fields))
