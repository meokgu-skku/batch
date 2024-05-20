create_table_restaurants = """
    CREATE TABLE IF NOT EXISTS `restaurants` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(64) NOT NULL,
    `original_categories` VARCHAR(64) NOT NULL,
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

create_table_restaurant_likes = """
    CREATE TABLE IF NOT EXISTS `restaurant_likes` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `user_id` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
create_table_categories = """
    CREATE TABLE IF NOT EXISTS `categories` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

create_table_restaurant_categories = """
    CREATE TABLE IF NOT EXISTS `restaurant_categories` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `category_id` BIGINT NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

create_table_operating_infos = """
    CREATE TABLE IF NOT EXISTS `operating_infos` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `day` VARCHAR(255) NOT NULL,
        `info` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

create_table_menus = """
    CREATE TABLE IF NOT EXISTS `menus` (
        `id` BIGINT NOT NULL AUTO_INCREMENT,
        `restaurant_id` BIGINT NOT NULL,
        `name` VARCHAR(255) NOT NULL,
        `price` INT NOT NULL,
        `description` VARCHAR(512) NOT NULL,
        `is_representative` TINYINT(1) NOT NULL,
        `image_url` VARCHAR(512) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
