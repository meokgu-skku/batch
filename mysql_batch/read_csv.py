import csv

with open('restaurants.csv', mode ='r')as file:
    csv_dict = csv.DictReader(file)
    for row in csv_dict:
        print(row)
        break