from stats import words_in_book
from stats import counting_characters

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = words_in_book(text)
    print(f"Found {num_words} total words")

    character_counts = counting_characters(text)
    print(character_counts)

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

main()

