import string

from flask import Flask
import datetime
import random

from faker import Faker
import csv

app = Flask("app")


@app.route("/")
def hello():
    return "Hellio"

@app.route("/now")
def now():
    return str(datetime.datetime.now())

@app.route("/gp")
def gen_pass():
    return "".join( [
        random.choice(string.ascii_lowercase)
        for _ in range (10)
    ])



app.run()





