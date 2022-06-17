CREATE TABLE review (
    id INTEGER NOT NULL AUTO_INCREMENT,
    product_id INTEGER,
    rating INTEGER,
    date TIMESTAMP,
    summary TEXT, 
    body TEXT,
    recommend INTEGER,
    reported INTEGER,
    response TEXT,
    helpfulness INTEGER,
    reviewer INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (reviewer) REFERENCES reviewer(id)
);
