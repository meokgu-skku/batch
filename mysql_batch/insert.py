import pymysql 

def insert_into_restaurants(cursor, restaurant):
    
    insert_query = """
    INSERT INTO `restaurants` (
      `id`,
      `name`, 
      `category_detail`, 
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


def upsert_into_categories(cursor, restaurant):
    
    upsert_query = """
        INSERT IGNORE INTO categories (restaurant_id, name)
        VALUES (%s, %s);
        """
    
    cursor.execute(upsert_query, (
      restaurant['id'],
      restaurant['custom_category']
    ))
