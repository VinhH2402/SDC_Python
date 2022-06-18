CREATE TABLE review (
    id INTEGER NOT NULL AUTO_INCREMENT,
    product_id INTEGER,
    rating INTEGER,
    date VARCHAR(20),
    summary TEXT, 
    body TEXT,
    recommend CHAR(10),
    reported CHAR(10),
    reviewer_name VARCHAR(100),
    reviewer_email VARCHAR(100),
    response TEXT,
    helpfulness INTEGER,
    PRIMARY KEY (id)
);
