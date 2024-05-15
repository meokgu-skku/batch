import pymysql 

def insert_into_restaurants(cursor, restaurant):
    
    insert_query = """
    INSERT INTO `restaurants` (
      `restaurant_id`,
      `name`, 
      `category`, 
      `custom_category`, 
      `review_count`, 
      `like_count`, 
      `address`, 
      `contact_num`, 
      `rating_avg`, 
      `representative_image_url`, 
      `kingo_pass`,
      `view_count`
    ) 
    VALUES (
      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    );
    """
    
    try:
        rating = float(restaurant['rating'])
    except ValueError:
        rating = 0.0

    cursor.execute(insert_query, (
      restaurant['id'],
      restaurant['name'], 
      restaurant['category'], 
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