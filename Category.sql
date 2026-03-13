create database category_db;
use category_db;
CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(80) UNIQUE NOT NULL,
    subtitle VARCHAR(120) UNIQUE NOT NULL,
    description VARCHAR(200) UNIQUE NOT NULL,
    image VARCHAR(200) UNIQUE NOT NULL,
    status BOOLEAN DEFAULT TRUE,
    delete_status BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    Updated_at DATETIME NULL ON UPDATE CURRENT_TIMESTAMP
);
SELECT * FROM category;