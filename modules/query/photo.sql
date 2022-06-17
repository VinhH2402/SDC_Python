CREATE TABLE photo (
    id INTEGER NOT NULL AUTO_INCREMENT,
    review_id INTEGER,
    url VARCHAR(255),  
    PRIMARY KEY (id),
    FOREIGN KEY(review_id) REFERENCES review(id)
);