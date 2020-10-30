import json

import requests

mss = 'MSS-1001643 '
url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
myobj = {'pid': mss}
response = requests.post(url, data=myobj)
if response.ok is True and response.status_code == 200:
    data_dict = response.json()
    for i in data_dict:
        print(i, data_dict[i])
    with open("temp.json", "w") as outfile:
        json.dump(data_dict, outfile)