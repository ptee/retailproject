
import csv
import datetime
import threading

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()

def mainfunc():
    with open("food_database.csv", 'rt') as f:
        reader = csv.reader(f, delimiter=",")
        food = list(reader)

    currentDate = datetime.datetime.now()

    for k in range (1,len(food)):
       
        date = food[k][3]
        date = date.replace("/","")
        #date = date[0:4]+"20"+date[4:6]
        expiry = datetime.datetime.strptime(date[2:4]+date[0:2]+'20'+date[4:6], '%d%m%Y')
        currentAmount = int(food[k][5])
        originalAmount = int(food[k][4])
        currentPrice = 0
        highestPrice = int(food[k][9])
        lowestPrice = int(food[k][8])
        deltaPrice = highestPrice - lowestPrice
        deltaTime = expiry - currentDate
        
        flag1 = 0
        flag2 = 0
        if currentAmount > originalAmount:
            flag1 = 1
        
        if deltaTime.days <= 3:
            flag2 = 1
            
        currentPrice = highestPrice - flag1*(deltaPrice*0.5*(currentAmount-originalAmount)/originalAmount) - \
        deltaPrice*0.5*flag2* ((3.0-deltaTime.days)/3.0)
        food[k][7] = currentPrice
        
        food[k][10]=((highestPrice - currentPrice)/highestPrice)
        
    with open("food_database.csv", "w") as m:
        writer = csv.writer(m)
        writer.writerows(food)

setInterval(mainfunc, 3)