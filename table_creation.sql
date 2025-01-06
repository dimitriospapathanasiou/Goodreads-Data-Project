CREATE TABLE DimBook (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    num_pages INT,
    isbn CHAR(10),
    isbn13 CHAR(13),
);

CREATE TABLE DimAuthor (
    author_id INT PRIMARY KEY,
    author NVARCHAR(255)
);

CREATE TABLE DimLanguage (
    language_id INT PRIMARY KEY,
    language_code NVARCHAR(255)
);

CREATE TABLE DimPublisher (
    publisher_id INT PRIMARY KEY,
    publisher VARCHAR(255)
);

CREATE TABLE DimTime (
    time_id FLOAT PRIMARY KEY,
    date DATE NOT NULL,
    year SMALLINT NOT NULL,
    quarter TINYINT NOT NULL,
    month TINYINT NOT NULL,
    day TINYINT NOT NULL,
    week SMALLINT NOT NULL,
    day_of_week TINYINT NOT NULL,
    is_weekend BIT NOT NULL,
);

CREATE TABLE DimBookAuthor (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES DimBook(book_id),
    FOREIGN KEY (author_id) REFERENCES DimAuthor(author_id)
);

CREATE TABLE DimBookPublisher (
    book_id INT,
    publisher_id INT,
    PRIMARY KEY (book_id, publisher_id),
    FOREIGN KEY (book_id) REFERENCES DimBook(book_id),
    FOREIGN KEY (publisher_id) REFERENCES DimPublisher(publisher_id)
);

CREATE TABLE FactBook (
    fact_id INT PRIMARY KEY,
    book_id INT,
    author_id INT,
    language_id INT,
    publisher_id INT,
    average_rating FLOAT,
    ratings_count INT,
    text_reviews_count INT,
    time_id FLOAT,
    FOREIGN KEY (book_id) REFERENCES DimBook(book_id),
    FOREIGN KEY (author_id) REFERENCES DimAuthor(author_id),
    FOREIGN KEY (language_id) REFERENCES DimLanguage(language_id),
    FOREIGN KEY (publisher_id) REFERENCES DimPublisher(publisher_id),
    FOREIGN KEY (time_id) REFERENCES DimTime(time_id)
);
