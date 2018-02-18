from flask import Flask
from flask import render_template, request, jsonify
import simplejson as json
import csv
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random import *


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


def updateMap(item,num):
     
    background = Image.open("map.png")
    
    mainItemName = item['name']
    mainItemX = int(float(item['x']))
    mainItemY = int(float(item['y']))
    
    similarItem1Name = item['similar'][0]['name']
    similarItem1X = int(float(item['similar'][0]['x']))
    similarItem1Y = int(float(item['similar'][0]['y']))
    
    similarItem2Name = item['similar'][1]['name']
    similarItem2X = int(float(item['similar'][1]['x']))
    similarItem2Y = int(float(item['similar'][1]['y']))
    
    similarItem3Name = item['similar'][2]['name']
    similarItem3X = int(float(item['similar'][2]['x']))
    similarItem3Y = int(float(item['similar'][2]['y']))
    
    similarItem4Name = item['similar'][3]['name']
    similarItem4X = int(float(item['similar'][3]['x']))
    similarItem4Y = int(float(item['similar'][3]['y']))
    
    similarItem5Name = item['similar'][4]['name']
    similarItem5X = int(float(item['similar'][4]['x']))
    similarItem5Y = int(float(item['similar'][4]['y']))
    
    draw = ImageDraw.Draw(background)
    draw.ellipse((mainItemX, mainItemY-20, mainItemX+80, mainItemY+60), outline ='red')
    
    imageMain = Image.open("itemImages/" +mainItemName + ".png")
    sim1 = Image.open("itemImages/" +similarItem1Name + ".png")
    sim2 = Image.open("itemImages/" +similarItem2Name + ".png")
    sim3 = Image.open("itemImages/" +similarItem3Name + ".png")
    sim4 = Image.open("itemImages/" +similarItem4Name + ".png")
    sim5 = Image.open("itemImages/" +similarItem5Name + ".png")
    
    background.paste(imageMain, (mainItemX, mainItemY), imageMain)
    background.paste(sim1, (similarItem1X, similarItem1Y), sim1)
    background.paste(sim2, (similarItem2X, similarItem2Y), sim2)
    background.paste(sim3, (similarItem3X, similarItem3Y), sim3)
    background.paste(sim4, (similarItem4X, similarItem4Y), sim4)
    background.paste(sim5, (similarItem5X, similarItem5Y), sim5)
    
    background.save("static/" + "image"+str(num)+".png")
    # background.show()
    return "image"+str(num)
    #background.show()

@app.route('/retailer') 
def retail():	
	return render_template('realtime_update.html')


@app.route('/message', methods = ['POST']) 
def handleMessage():
	userMessage = request.json['userMessage']
	randNum = randint(1, 10000)
	item = query(userMessage,randNum)
	apiResponse = {
		"imgName":item["img"],
		"sim1Name":item["similar"][0]["name"],
		"sim2Name":item["similar"][1]["name"],
		"sim3Name":item["similar"][2]["name"],
		"sim4Name":item["similar"][3]["name"],
		"sim5Name":item["similar"][4]["name"],
		"sim1Price":item["similar"][0]["price"],
		"sim2Price":item["similar"][1]["price"],
		"sim3Price":item["similar"][2]["price"],
		"sim4Price":item["similar"][3]["price"],
		"sim5Price":item["similar"][4]["price"]
    }
	r = json.dumps(apiResponse)
	print(r)
	response = app.response_class(
		response=r,
		status=200,
		mimetype='application/json'
	)
	return response 


def query(word,num):
    item = {}
    percentSale = [] 
    with open("food_database.csv", 'rt') as f:
        reader = csv.reader(f, delimiter=",")
        csv_file = list(reader)

        for row in csv_file:
            percentSale.append(row[10])
            if word == row[0]:
                item["name"] = word
                item["x"] = row[1]
                item["y"] = row[2]
                item["id"] = row[6]
                
        for idx,row in enumerate(csv_file):
#             print(item["id"])
#             print(row[6])
            if item["id"] != row[6]:
                percentSale[idx] = 0
            
        matches = np.asarray(percentSale).argsort()[-5:][::-1]
        item["similar"] = [
    {
      "name": csv_file[matches[0]][0],
      "x": csv_file[matches[0]][1],
      "y": csv_file[matches[0]][2],
      "price": csv_file[matches[0]][10]
    },
    {
      "name": csv_file[matches[1]][0],
      "x": csv_file[matches[1]][1],
      "y": csv_file[matches[1]][2],
      "price": csv_file[matches[1]][10]
    },
    {
      "name": csv_file[matches[2]][0],
      "x": csv_file[matches[2]][1],
      "y": csv_file[matches[2]][2],
      "price": csv_file[matches[2]][10]
    },
    {
      "name": csv_file[matches[3]][0],
      "x": csv_file[matches[3]][1],
      "y": csv_file[matches[3]][2],
      "price": csv_file[matches[3]][10]
    },
    {
      "name": csv_file[matches[4]][0],
      "x": csv_file[matches[4]][1],
      "y": csv_file[matches[4]][2],
      "price": csv_file[matches[4]][10]
    }
  ]
        
    imgName = updateMap(item,num)
    item['img'] = imgName
    return item


if __name__ == '__main__':
    app.run()
