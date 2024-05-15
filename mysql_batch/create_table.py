def create_table(cursor):
    # table creation query

    delete_table_restaurants = """
    DROP TABLE IF EXISTS `restaurants`;
    """
    delete_table_restaurant_likes= """
    DROP TABLE IF EXISTS `restaurant_likes`;
    """
    cursor.execute(delete_table_restaurants)
    cursor.execute(delete_table_restaurant_likes)
    
    create_table_restaurants = """
    CREATE TABLE `restaurants` (
    `restaurant_id` BIGINT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(64) NOT NULL,
    `category` VARCHAR(64),
    `custom_category` VARCHAR(64) NOT NULL,
    `review_count` BIGINT NOT NULL DEFAULT 0,
    `like_count` BIGINT NOT NULL DEFAULT 0,
    `address` VARCHAR(256),
    `contact_num` VARCHAR(32),
    `rating_avg` DOUBLE,
    `representative_image_url` TEXT,
    `kingo_pass` TINYINT,
    `view_count` BIGINT DEFAULT 0,
    PRIMARY KEY (`restaurant_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    create_table_restaurant_likes ="""
    CREATE TABLE `restaurant_likes` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `user_name` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    cursor.execute(create_table_restaurants)
    cursor.execute(create_table_restaurant_likes)
    
