import csv
import sys


with open("food_database.csv", 'rt') as f:
    reader = csv.reader(f, delimiter=",")
    food = list(reader)

#print type(sys.argv[1]), type(sys.argv[2])

for k in range(0,len(food)):
    i = food[k].index(str(sys.argv[1])) if str(sys.argv[1]) in food[k] else None#str(sys.argv[1])
    if isinstance(i, int):
        row = k

food[row][5] = int(food[row][5]) + int(sys.argv[2])

with open("food_database.csv", "w") as k:
    writer = csv.writer(k)
    writer.writerows(food)



