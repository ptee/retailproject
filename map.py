def updateMap(item):
     
    print(item)    
    background = Image.open("backgroundNew.png")
    
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
    
    background.paste(imageMain, (int(mainItemX), int(mainItemY)), imageMain)
    background.paste(sim1, (similarItem1X, similarItem1Y), sim1)
    background.paste(sim2, (similarItem2X, similarItem2Y), sim2)
    background.paste(sim3, (similarItem3X, similarItem3Y), sim3)
    background.paste(sim4, (similarItem4X, similarItem4Y), sim4)
    background.paste(sim5, (similarItem5X, similarItem5Y), sim5)
    
    background.show()


    
    



    