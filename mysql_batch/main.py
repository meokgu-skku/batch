import pymysql
import csv
from create_table import create_table
from insert import insert_into_restaurants

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


# table insert query
# restaurants insert
with open('restaurants.csv', mode ='r')as file:
    csv_dict = csv.DictReader(file)
    for restaurant in csv_dict:
        insert_into_restaurants(cursor, restaurant)

conn.commit()


# restaurant_likes insert


# close the connection
conn.close()