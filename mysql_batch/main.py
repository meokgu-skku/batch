import pymysql
import csv
from create_table import create_table
from insert import *

# connect to MySQL server
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="skku-user",
    password="skku-pw",
    db="skku",
    charset='utf8'
)

# table creation query(restaurants, restaurant_likes)
cursor = conn.cursor()
create_table(cursor)
conn.commit()


# Insert restaurants, categories 
with open('../restaurants.csv', mode ='r')as file:
    csv_dict = csv.DictReader(file)
    for restaurant in csv_dict:
        insert_into_restaurants(cursor, restaurant)
        insert_into_categories(cursor, restaurant)

conn.commit()

# Insert operating_infos
with open('../operations.csv', mode ='r')as file:
    csv_dict = csv.DictReader(file)
    for operation in csv_dict:
        insert_into_operating_infos(cursor, operation)
        

conn.commit()

# Insert menus
with open('../menus.csv', mode ='r')as file:
    csv_dict = csv.DictReader(file)
    for menu in csv_dict:
        insert_into_menus(cursor, menu)

conn.commit()


# close the connection
conn.close()