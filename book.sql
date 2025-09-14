-- Now create Books table (references Authors)
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL
);