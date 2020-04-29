import string

from flask import Flask
import datetime
import random
import sqlite3
import os

from flask import request

app = Flask("app")


@app.route("/")
def hello():
    return "Hellio"

@app.route("/now")
def now():
    return str(datetime.datetime.now())


@app.route("/gp/<length>/<option>")
def gen_pass(length,option):

    option_1 = string.ascii_lowercase
    b = "1234567890"
    option_2 = option_1 + b

    try:                        # здесь проверка на длину и на то, что это число, если проверка не пройдена - параметр устанавливается принудительно
        length = int(length)
        if 7 < length < 25:
            pass
        else:
            length = 15
    except:
        length = 10

    option = int(option)       # тут устанавливаем будет в пароле цифры или нет

    if option == 1:
        return "".join([random.choice(option_1) for _ in range (length)])
    elif option == 2:
        return "".join([random.choice(option_2) for _ in range(length)])
    else:
        return "".join([random.choice(string.ascii_lowercase) for _ in range(10)])

@app.route("/database-cities/<city>/<state>")
def database_cities(city, state):
    query = f"SELECT FirstName, LastName, City FROM customers WHERE State = '{state}' AND City = '{city}'"
    records = execute_query(query)
    answer = ""
    for i in records:
        answer += str(i)
        answer += "<br/>"
    return answer

@app.route("/unique-names")
def unique_names():
    query = "SELECT FirstName FROM customers"
    records = execute_query(query)
    records = set(records)
    answer = ""
    for i in records:
        answer += str(i)
        answer += "<br/>"
    return answer

@app.route("/turnover")
def turnover():
    query = "SELECT UnitPrice, Quantity FROM invoice_items"
    records = execute_query(query)
    turnover = 0
    for i in records:
        price = i[0] * i[1]
        turnover += price
    return str(turnover)


def execute_query(query):
    db_path = os.path.join(os.getcwd(), "chinook.db")
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    curr.execute(query)
    records = curr.fetchall()
    return records

app.run()





