import json
import requests
import os


def invokeNSXTGET(url: str) -> requests.Response:
    myHeader = {"Content-Type": "application/json","Accept": "application/json"}
    try:
        response = requests.get(url,headers=myHeader, auth=(os.environ['EXP_srcNSXmgrUsername'] , os.environ['EXP_srcNSXmgrPassword']), verify=True)
        if response.status_code != 200:
            print(f'API Call Status {response.status_code}, text:{response.text}')
        return response
    except Exception as e:
            print(e)
            return None
        
base_url = os.environ['EXP_srcNSXmgrURL']
url = f'{base_url}/policy/api/v1/infra/tags'
response = invokeNSXTGET(url)
print(json.dumps(response.json(), indent=4))