import pandas as pd
from itertools import combinations
from collections import defaultdict

books = pd.read_csv('cleaned_books.csv')
books = books.dropna(subset=['authors', 'publisher'])
author_publisher = books[['authors', 'publisher']]
transactions = author_publisher.groupby('publisher')['authors'].apply(list).reset_index()
author_publisher_pairs = []
for _, row in transactions.iterrows():
    publisher = row['publisher']
    authors = row['authors']
    for author in authors:
        author_publisher_pairs.append((author, publisher))

pair_counts = defaultdict(int)
for pair in author_publisher_pairs:
    pair_counts[pair] += 1
pair_df = pd.DataFrame.from_dict(pair_counts, orient='index', columns=['count'])
pair_df.index = pd.MultiIndex.from_tuples(pair_df.index, names=['author', 'publisher'])
pair_df = pair_df.reset_index()

significant_pairs = pair_df[pair_df['count'] > 1]
significant_pairs = significant_pairs.sort_values(by='count', ascending=False)
import IPython.display as display
display.display(significant_pairs)
