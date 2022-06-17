CREATE TABLE photo (
    id INTEGER NOT NULL AUTO_INCREMENT,
    reviewer_id INTEGER,
    url VARCHAR(255),  
    PRIMARY KEY (id)
);