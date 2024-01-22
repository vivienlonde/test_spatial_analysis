import os
from dotenv import load_dotenv
import requests
import json
import base64
from pprint import pprint

load_dotenv()

endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
key = os.getenv('AZURE_OPENAI_KEY')
deployment_name = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')

root_uri = endpoint  + 'openai/deployments/' + deployment_name + '/chat/completions'
api_version = '?api-version=2023-12-01-preview'
endpoint = root_uri + api_version
# print(endpoint)

headers = {   
    "Content-Type": "application/json",   
    "api-key": key
} 

image_file = "data/car.png"
base_64_encoded_image = base64.b64encode(open(image_file, "rb").read()).decode("ascii")

data = { 
    "messages": [ 
        { "role": "system", "content": "You are a helpful assistant." }, # Content can be a string, OR 
        { "role": "user", "content": [       # It can be an array containing strings and images. 
            "What is the color of the car?", # brand, model and color
            { "image": base_64_encoded_image }      # Images are represented like this. 
        ] } 
    ], 
    "max_tokens": 100 
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))   

# print(f"Status Code: {response.status_code}")   
# pprint(response.json())

if response.status_code == 200:
        result = json.loads(response.text)["choices"][0]["message"]["content"]
        print(result)
    
elif response.status_code == 429:
    print("[ERROR] Too many requests. Please wait a couple of seconds and try again.")
    
else:
    print("[ERROR] Error code:", response.status_code)