import json

import requests

url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
myobj = {'pid': 'MSS-1001210'}

x = requests.post(url, data = myobj)
b = x.json()
insname = b['0']['insname']
process = tuple(b.keys())
with open('temp.json') as fp:
    a = json.load(fp)
    values = tuple(a.keys())
pass