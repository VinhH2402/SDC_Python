CREATE TABLE characteristic_review (
    id INTEGER NOT NULL AUTO_INCREMENT,
    characteristic_id INTEGER,
    review_id INTEGER,
    value INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (review_id) REFERENCES review(id),
    FOREIGN KEY (characteristic_id) REFERENCES characteristic(id)
);