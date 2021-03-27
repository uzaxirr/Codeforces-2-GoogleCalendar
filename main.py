import requests
import json
response=requests.get("https://codeforces.com/api/contest.list")
events=response.json()
filename='data.txt'
with open(filename, 'w') as txt_file_open:
    json.dump(events, txt_file_open,indent=4)
variable=events['result']
list=(events['result'])
print(list[0]['name'])
print(type(eve))