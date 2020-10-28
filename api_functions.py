import requests


def get_patient_data(mss_no):
    url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
    myobj = {'pid': mss_no}
    response = requests.post(url, data=myobj)
    if response.ok is True and response.status_code == 200:
        data = response.json()
        return data


if __name__ == "__main__":
    a = get_patient_data('MSS-1001210')
    pass