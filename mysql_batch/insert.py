import pymysql 

def insert_into_restaurants(cursor, restaurant):
    
    insert_query = """
    INSERT INTO `restaurants` (
      `id`,
      `name`, 
      `original_categories`, 
      `review_count`, 
      `like_count`, 
      `address`, 
      `contact_number`, 
      `rating_avg`, 
      `representative_image_url`, 
      `view_count`,
      `discount_content`
    ) 
    VALUES (
      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    );
    """

    
    try:
        rating = float(restaurant['rating'])
    except ValueError:
        rating = 0.0

    cursor.execute(insert_query, (
      restaurant['id'],
      restaurant['name'], 
      restaurant['custom_category'], 
      0, 
      0, 
      restaurant['address'], 
      restaurant['number'], 
      rating , 
      restaurant['image_url'], 
      0,
      0
    ))


def insert_into_categories(cursor, restaurant):
    
    insert_query = """
        INSERT IGNORE INTO categories (restaurant_id, name)
        VALUES (%s, %s);
        """
    
    cursor.execute(insert_query, (
      restaurant['id'],
      restaurant['custom_category']
    ))

def insert_into_operating_infos(cursor, operation):
    
    insert_query = """
        INSERT IGNORE INTO operating_infos (restaurant_id, day, info)
        VALUES (%s, %s, %s);
        """
    
    cursor.execute(insert_query, (
      operation['restaurant_id'],
      operation['day'],
      operation['info']
    ))

def insert_into_menus(cursor, menu):
    
    insert_query = """
        INSERT IGNORE INTO menus (
          restaurant_id, 
          name,
          price,
          description,
          is_representative,
          image_url
        )
        VALUES (%s, %s, %s, %s, %s, %s);
        """
    
    cursor.execute(insert_query, (
      menu['restaurant_id'],
      menu['menu_name'],
      int(menu['price'].replace(",","")),
      menu['description'],
      (menu['is_representative']=="대표"),
      menu['image_url']
    ))
