import requests
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

with open("gemini-api-key.txt","r") as file:
    api_key = file.readline()

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": api_key
}

payload = {
    "contents": [
      {
        "parts": [
          {
            "text": "Explain concepts of python required for Agentic AI."
          }
        ]
      }
    ]
  }

response = requests.post(url, headers=headers, json=payload)

response.raise_for_status()

print(response.status_code)

with open("gemini-response.json", "w") as file:
    json.dump(response.json(), file, indent=4)
