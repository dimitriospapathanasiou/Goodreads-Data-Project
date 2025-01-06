import pandas as pd

books = pd.read_csv('cleaned_books_alternate.csv')
books = books.dropna(subset=['  num_pages', 'average_rating'])
books['  num_pages'] = books['  num_pages'].astype(str).str.strip().astype(int)
books['average_rating'] = books['average_rating'].astype(float)

# Page ranges
bins = [0, 100, 200, 300, 400, 500, 600, float('inf')]
labels = ['100 or below', '101-200', '201-300', '301-400', '401-500', '501-600', '600+']  # Labels for bins
books['page_range'] = pd.cut(books['  num_pages'], bins=bins, labels=labels, right=True)

page_range_ratings = books.groupby('page_range', observed=False)['average_rating'].mean().reset_index()
page_range_ratings.columns = ['Page Range', 'Average Rating']
import IPython.display as display
display.display(page_range_ratings)
