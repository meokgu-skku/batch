from create_table_list import *
from delete_table_list import *

def create_table(cursor):
    
    # table deletion query
    cursor.execute(delete_table_restaurants)
    cursor.execute(delete_table_categories)
    cursor.execute(delete_table_operating_infos)
    cursor.execute(delete_table_menus)

    # table creation query
    cursor.execute(create_table_restaurants)
    cursor.execute(create_table_restaurant_likes)
    cursor.execute(create_table_categories)
    cursor.execute(create_table_restaurant_categories)
    cursor.execute(create_table_operating_infos)
    cursor.execute(create_table_menus)
    
