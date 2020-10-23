import json
import requests

url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
myobj = {'pid': 'MSS-1001172'}

x = requests.post(url, data = myobj)

a = x.json()


with open('temp.json') as fp:
    a = json.load(fp)
pass