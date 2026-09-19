import sys

from stats import words_in_book
from stats import counting_characters
from stats import chars_dict_to_sorted_list

# Entry point - reads a book path from the command line & prints a character report
def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Load the book's text and run the analysis
    text = get_book_text(book_path)

    num_words = words_in_book(text)

    character_counts = counting_characters(text)

    # Sorts the characters by frequency & print the final formatted report
    print_report(book_path, num_words, chars_dict_to_sorted_list(character_counts))

# Opens a file & returns its full contents as a single string
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

# Prints the full BookBot Projects report - Header, Word Count & Character Frequency Breakdown
def print_report(book_path: str, word_count: int, character_counts: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character_count_section in character_counts:
        if character_count_section[0].isalpha():
            print(f"{character_count_section[0]}: {character_count_section[1]}")
            # Tuples start at index 0, therefore the first element is the character and the second is the count
            # Refer to the "isAlpha()" link on the bootDev site on as to how to use it properly. Peer request is a last resort

    print("============= END ===============")

main()