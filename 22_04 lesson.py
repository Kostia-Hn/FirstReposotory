import string

from flask import Flask
import json
import datetime
import random
app=Flask(__name__)
from flask import request
import requests
import sqlite3


@app.route("/get-astronauts")
def astro():
    length = request.args["length"]
    response = requests.get('http://api.open-notify.org/astros.json')
    if response.status_code == 200:
        resp = json.loads(response.text)
        return f'Astronauts number {resp["number"]}'
    else:
        return f'Error{response.status_code}'

@app.route("/")
def hello():
    return "Hellio"


@app.route("/gp")
def gen_pass():
    return "".join( [
        random.choice(string.ascii_lowercase)
        for _ in range (10)
    ])
@app.route("/get_customers")
def get_customers():
    query = 'select FirstName, LastName from customers WHERE City = "Oslo" or City = "Paris"'
    records = execute_query(query)
    return str(records)

def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records

app.run()