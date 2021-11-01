# Import Module
import json
import requests
# api key : c7a0375217eb9bdf535ebb72e6c195b8
baseUrl = 'http://api.weatherstack.com/';

params = {
  'access_key': 'c7a0375217eb9bdf535ebb72e6c195b8',
  'query': 'Sofia',
}

response = requests.get("http://api.weatherstack.com/current", params)

print(response.json())