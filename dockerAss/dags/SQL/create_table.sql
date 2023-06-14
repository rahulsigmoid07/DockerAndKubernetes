drop table if exists users;
            CREATE TABLE IF NOT EXISTS USERS (
                id INT not null unique,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                organization VARCHAR(255) NOT NULL
            );