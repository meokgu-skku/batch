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

create_table_operating_infos ="""
    CREATE TABLE IF NOT EXISTS `operating_infos` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `day` VARCHAR(255) NOT NULL,
        `info` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY unique_restaurant_name (restaurant_id, day)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

create_table_menus ="""
    CREATE TABLE IF NOT EXISTS `menus` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `menu_name` VARCHAR(255) NOT NULL,
        `price` VARCHAR(32) NOT NULL,
        `description` VARCHAR(512) NOT NULL,
        `is_representative` VARCHAR(32) NOT NULL,
        `image_url` VARCHAR(512) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY unique_restaurant_name (restaurant_id, menu_name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """