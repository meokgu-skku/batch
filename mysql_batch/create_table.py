def create_table(cursor):
    # table creation query

    delete_table_restaurants = """
    DROP TABLE IF EXISTS `restaurants`;
    """
    delete_table_restaurant_likes= """
    DROP TABLE IF EXISTS `restaurant_likes`;
    """
    cursor.execute(delete_table_restaurants)
    #cursor.execute(delete_table_restaurant_likes)  // 좋아요 테이블을 삭제 보류
    
    create_table_restaurants = """
    CREATE TABLE `restaurants` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(64) NOT NULL,
    `category_detail` VARCHAR(64) NOT NULL,
    `review_count` INT NOT NULL DEFAULT 0,
    `like_count` INT NOT NULL DEFAULT 0,
    `address` VARCHAR(256),
    `contact_number` VARCHAR(32),
    `rating_avg` DOUBLE,
    `representative_image_url` TEXT,
    `view_count` INT DEFAULT 0,
    `discount_content` VARCHAR(128),
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    create_table_restaurant_likes ="""
    CREATE TABLE IF NOT EXISTS `restaurant_likes` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `user_id` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    create_table_categories ="""
    CREATE TABLE IF NOT EXISTS `categories` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `name` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY unique_restaurant_name (restaurant_id, name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    cursor.execute(create_table_restaurants)
    cursor.execute(create_table_restaurant_likes)
    cursor.execute(create_table_categories)
    
