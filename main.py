from stats import words_in_book
from stats import counting_characters
from stats import chars_dict_to_sorted_list

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = words_in_book(text)

    character_counts = counting_characters(text)

    print_report(book_path, num_words, chars_dict_to_sorted_list(character_counts))

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(book_path: str, word_count: int, character_counts: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character_count_section in character_counts:
        if character_count_section[0].isalpha():
            print(f"{character_count_section[0]}: {character_count_section[1]}")

    print("============= END ===============")

main()

