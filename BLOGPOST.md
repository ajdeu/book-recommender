# Building a Book Recommender with a Trie in Python

I built a small terminal program that recommends books. You type the first letters of a genre, the program completes them, and you get a list of books for the genre you pick.

## Storing the data

The books live in a dictionary that maps a genre to a list of (title, author) tuples. A dictionary lookup takes constant time, so showing all recommendations for a chosen genre is instant.

## Autocomplete with a trie

For the autocomplete I used a trie (prefix tree). Each node represents one letter, and a path from the root spells a genre. To find all genres that start with a prefix, the program walks down the prefix and then collects every word below that node. This is faster than scanning every genre, because the work depends on the length of the prefix, not on the number of genres.

## What I learned

- Picking the right data structure for each job (dictionary for lookup, trie for prefixes) keeps the code simple.
- Recursion makes collecting the words below a trie node short and readable.
- Small Git commits made it easy to follow how the program grew.

## Run it yourself

```bash
python3 recommender.py
```

Next steps could be adding more genres, searching by author, or ranking recommendations.
