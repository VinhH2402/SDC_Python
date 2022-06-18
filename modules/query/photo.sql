CREATE TABLE photo (
    id INT NOT NULL AUTO_INCREMENT,
    review_id INT,
    url VARCHAR(255),  
    PRIMARY KEY (id),
    FOREIGN KEY (review_id) REFERENCES review(id)
);