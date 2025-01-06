BULK INSERT dbo.DimAuthor
FROM 'C:\Users\marke\Desktop\Big Data\dim_author.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);

BULK INSERT dbo.DimBook
FROM 'C:\Users\marke\Desktop\Big Data\dim_book.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);

BULK INSERT dbo.DimLanguage
FROM 'C:\Users\marke\Desktop\Big Data\dim_language.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);

BULK INSERT dbo.DimPublisher
FROM 'C:\Users\marke\Desktop\Big Data\dim_publisher.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);

BULK INSERT dbo.DimTime
FROM 'C:\Users\marke\Desktop\Big Data\dim_time.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);

BULK INSERT dbo.DimBookAuthor
FROM 'C:\Users\marke\Desktop\Big Data\dim_book_author.csv'
WITH
(
    FORMAT='CSV',
    FIRSTROW=2
);

BULK INSERT dbo.DimBookPublisher
FROM 'C:\Users\marke\Desktop\Big Data\dim_book_publisher.csv'
WITH
(
    FORMAT='CSV',
    FIRSTROW=2
);

BULK INSERT dbo.FactBook
FROM 'C:\Users\marke\Desktop\Big Data\fact_book.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
);
