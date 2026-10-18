# Book Recommender

A terminal program that recommends books by genre. Type the first letters of a genre, see the matching genres (autocomplete), pick one and get a list of books.

## Run

```bash
python3 recommender.py
```

## How it works

- `books_data.py`: genre -> list of (title, author) stored in a dictionary.
- `trie.py`: a trie (prefix tree) that powers the autocomplete.
- `recommender.py`: the interactive program.
