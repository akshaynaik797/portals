from flask import Flask, render_template, jsonify, url_for, request
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)

@app.route('/my_list')
def my_list():
    a = [1,2,3]
    return jsonify(a)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    a = url_for('data_entry')
    user = {"username": "akshay naik"}
    return render_template('index.html', title="PPP", user=user)

@app.route('/data_entry')
def data_entry():
    return render_template('data_entry.html')


if __name__ == "__main__":
    app.run()
