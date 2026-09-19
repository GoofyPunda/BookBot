# Essentiall splits the book's text into words & returns the total word count
def words_in_book(book_text: str) -> int:
    separate_words = book_text.split()
    return len(separate_words)

# Loops through every character in the text, lowercases it & tallies how many times each one appears
def counting_characters(book_text: str) -> dict[str, int]:
    character_count = {}

    for character in book_text:
        character = character.lower()

        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

# Helper function for sorted(): given a (character, count) tuple, returns the count for comparison
def sort_on(character_count_pair: tuple[str, int]) -> int:
    return character_count_pair[1]

# Converts the character count dictionary into a list of (character, count) tuples; sorted frommost to least frequent hence the "reverse=True"
def chars_dict_to_sorted_list(sorted_dict: dict[str, int]) -> list[tuple[str, int]]:
    tuples_list = []

    for single_character in sorted_dict:
        tuples_list.append((single_character, sorted_dict[single_character]))

    sorted_list = sorted(tuples_list, reverse=True, key=sort_on)
    return sorted_list