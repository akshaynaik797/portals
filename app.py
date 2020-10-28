import sqlite3
import json

from flask import Flask, request, jsonify, send_from_directory, abort
app = Flask(__name__)
dbname = 'database1.db'


@app.route('/')
def index():
    return 'this is portal automation'


@app.route('/get_mss_no_details', methods=["POST"])
def get_mss_no_details():
    try:
        q = f"select data from mss_no_data where mss_no='{request.form['mss_no']}'"
        with sqlite3.connect(dbname) as con:
            cur = con.cursor()
            cur.execute(q)
            a = json.loads(cur.fetchone()[0])
            return jsonify(a)
    except Exception as e:
        return jsonify(e)

if __name__ == "__main__":
    app.run()