import json

import requests

mss = 'MSS-1001504'
url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
myobj = {'pid': mss}
response = requests.post(url, data=myobj)
if response.ok is True and response.status_code == 200:
    data_dict = response.json()
    if 'Claim' in data_dict and 'Query Replied' in data_dict:
        if data_dict['Claim'] != '':
            print('this is final bills')
        elif len(data_dict['Query Replied']) > 0:
            print('this is query reply')
    with open("temp.json", "w") as outfile:
        json.dump(data_dict, outfile)