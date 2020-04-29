import sqlite3
import os
from django.http import HttpResponse
import string
import random
from django.shortcuts import render

# Create your views here.

def gen_pass(request):
    length = request.GET['length']
    option = request.GET['option']

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
        return HttpResponse("".join([random.choice(option_1) for _ in range (length)]))
    elif option == 2:
        return HttpResponse("".join([random.choice(option_2) for _ in range(length)]))
    else:
        return HttpResponse("".join([random.choice(string.ascii_lowercase) for _ in range(10)]))

def execute_query(query):
    db_path = os.path.join(os.getcwd(), "chinook.db")
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    curr.execute(query)
    records = curr.fetchall()
    return records

def unique_names(request):
    query = "SELECT FirstName FROM customers"
    records = execute_query(query)
    records = set(records)
    answer = ""
    for i in records:
        answer += str(i)
        answer += "<br/>"
    return HttpResponse(answer)

def database_cities(request):
    state = request.GET['state']
    city = request.GET['city']
    if len(state)>3:               #Защита от sql инъекции путем ограничения максимальной длины стрки
        state = "CA"
    if len(city)>10:
        city = "Cupertino"

    query = f"SELECT FirstName, LastName, City FROM customers WHERE State = '{state}' AND City = '{city}'"
    records = execute_query(query)
    answer = ""
    for i in records:
        answer += str(i)
        answer += "<br/>"
    return HttpResponse(answer)


def turnover(request):
    query = "SELECT UnitPrice, Quantity FROM invoice_items"
    records = execute_query(query)
    turnover = 0
    for i in records:
        price = i[0] * i[1]
        turnover += price
    return HttpResponse(str(turnover))