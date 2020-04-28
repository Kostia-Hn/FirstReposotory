import string

from flask import Flask
import datetime
import random

from faker import Faker
import csv

app = Flask("app")

import string

from flask import Flask
import datetime
import random

from faker import Faker
import csv

app = Flask("app")

fake = Faker()
fakes_list = ""
for i in range (1,101,1):
    fakes_list += fake.safe_email()
    fakes_list += " ,"
    fakes_list += fake.name()
    fakes_list += " ;"


filepath = r"hw.csv"
arr1 = []
total_height = 0
total_mass = 0
with open(filepath, "r", newline="") as file:

    reader = csv.reader(file)

    for row in reader:
        arr1.append(row)

arr1.pop(0)
arr1.pop(-1)
students_counter = 0
for i in arr1:

    students_counter +=1
    total_height +=float(i[1])
    total_mass +=float(i[2])

avg_height = total_height/students_counter
avg_mass = total_mass/students_counter
str_avg_h = "Average height is " + str(int(avg_height * 2.54)) + " cm."
str_avg_m = "Average weight is " + str(int(avg_mass * 0.453592)) + " kg."


@app.route("/faker")
def f_fakes():
    return fakes_list

@app.route("/average")
def average():
    return str_avg_m + "; " + str_avg_h

@app.route("/modules")
def modules():
    f = open("requirements.txt",'r')
    return f.read()

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





