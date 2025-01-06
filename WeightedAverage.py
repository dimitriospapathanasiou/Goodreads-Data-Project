import pandas as pd

books = pd.read_csv('cleaned_books.csv')
books = books.dropna(subset=['authors', 'average_rating', 'ratings_count'])
books['average_rating'] = books['average_rating'].astype(float)
books['ratings_count'] = books['ratings_count'].astype(int)
books['authors'] = books['authors'].str.split('/')
books = books.explode('authors')

# Global statistics
C = books['average_rating'].mean()
m = 100

# Weighted score for each author
author_stats = books.groupby('authors').agg(
    total_ratings=('ratings_count', 'sum'),
    average_rating=('average_rating', 'mean')
).reset_index()
author_stats['Weighted Score'] = ((author_stats['total_ratings'] * author_stats['average_rating']) + (m * C)) / (
        author_stats['total_ratings'] + m)
author_stats = author_stats.sort_values(by='Weighted Score', ascending=False)
import IPython.display as display

display.display(author_stats[['authors', 'Weighted Score', 'average_rating', 'total_ratings']].head(10))
