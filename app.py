import json
import sqlite3

import requests
from flask import Flask, request, jsonify

import db_functions
app = Flask(__name__)
dbname = 'database1.db'


@app.route('/')
def index():
    return 'this is portal automation'


@app.route('/get_mss_no_details', methods=["POST"])
def get_mss_no_details():
    try:
        url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
        myobj = {'pid': request.form['mss_no']}
        response = requests.post(url, data=myobj)
        if response.ok is True and response.status_code == 200:
            data_dict = response.json()
            with open("temp.json", "w") as outfile:
                json.dump(data_dict, outfile)

            claim_no, mss_no = data_dict['0']['ClaimId'], request.form['mss_no']
            insname, process = data_dict['0']['insname'], data_dict['0']['status']

            q = f"select insname from insname_alias where alias='{insname}'"
            q1 = f"select process_name from process_name_alias where alias='{process}'"
            with sqlite3.connect(dbname) as con:
                cur = con.cursor()
                cur.execute(q)
                result1 = cur.fetchone()
                cur.execute(q1)
                result2 = cur.fetchone()
                if result1 is not None:
                    if result2 is not None:
                        if result2[0] == 'final_bills':
                            if 'Claim' in data_dict:
                                doa, dod = data_dict['Claim'][0]['Date_Of_Admission'], data_dict['Claim'][0][
                                    'Date_Of_Discharge']
                                amount, remark = data_dict['Claim'][0]['Cliamed_Amount'], data_dict['Claim'][0][
                                    'Remark']
                                docs = [i['Doc'] for i in data_dict['Claim'][0]['Doc']]
                                response = {
                                    'mss_no': mss_no,
                                    'claim_no': claim_no,
                                    'insname': result1[0],
                                    'process': result2[0],
                                    'doa': doa,
                                    'dod': dod,
                                    'amount': amount,
                                    'remark': remark,
                                    'docs': docs,
                                    'login_details': db_functions.get_portal_details_dict(result1[0], result2[0])
                                }
                                return jsonify(response)
                            else:
                                return jsonify('claim data not found')
                        else:
                            return jsonify('process not found')
                    else:
                        return jsonify('process not found')
                else:
                    return jsonify('insurer not found')
    except Exception as e:
        return jsonify(e)


if __name__ == "__main__":
    app.run()
