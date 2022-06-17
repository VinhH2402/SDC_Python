CREATE TABLE charac_review (
    id INTEGER NOT NULL AUTO_INCREMENT,
    char_id INTEGER,
    review_id INTEGER,
    value INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (review_id) REFERENCES review(id),
    FOREIGN KEY (char_id) REFERENCES characteristic(id)
);