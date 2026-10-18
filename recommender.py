"""Book recommender: type the start of a genre, pick one, get recommendations."""

from books_data import BOOKS
from trie import Trie

genre_trie = Trie(BOOKS)


def suggest_genres(prefix):
    """Autocomplete: genres that start with what the user typed."""
    return genre_trie.starts_with(prefix.strip().lower())


def recommendations_for(genre):
    """Look up all books stored for a genre (dictionary lookup, O(1))."""
    return BOOKS.get(genre, [])


def choose_genre():
    while True:
        prefix = input("\nWhat genre are you in the mood for? (type a few letters, 'q' to quit): ")
        if prefix.strip().lower() == "q":
            return None
        matches = suggest_genres(prefix)
        if not matches:
            print("No genre starts with '{0}'. Try again.".format(prefix))
            continue
        if len(matches) == 1:
            answer = input("Did you mean '{0}'? (y/n): ".format(matches[0])).strip().lower()
            if answer == "y":
                return matches[0]
            continue
        print("Possible genres:")
        for genre in matches:
            print(" - " + genre)
        if prefix.strip().lower() in matches:
            return prefix.strip().lower()


def main():
    print("Welcome to the book recommender!")
    while True:
        genre = choose_genre()
        if genre is None:
            break
        print("\nBooks for '{0}':".format(genre))
        for title, author in recommendations_for(genre):
            print(" * {0} by {1}".format(title, author))
    print("Happy reading!")


if __name__ == "__main__":
    main()
