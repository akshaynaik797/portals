import json

import requests

mss = 'MSS-1001544'
url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
myobj = {'pid': mss}
response = requests.post(url, data=myobj)
if response.ok is True and response.status_code == 200:
    data_dict = response.json()
    with open("temp.json", "w") as outfile:
        json.dump(data_dict, outfile)