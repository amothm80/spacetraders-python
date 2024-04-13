import io
import requests
from requests.exceptions import HTTPError
import json


token = ''
api_url = 'https://api.spacetraders.io/v2/'
agent_url = 'my/agent'

def get_token():
    global token
    tokenfile = open('spacetradertoken.txt','r')
    token = tokenfile.readline()

def get_agent():
    try:
        header = {'Content-Type': 'application/json',\
                  'Authorization':'Bearer '+token}
        response = requests.get(api_url+agent_url,headers=header)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        return response.json()


if __name__ == '__main__':
    get_token()
    print(get_agent()["data"])