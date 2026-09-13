
def words_in_book(book_text: str) -> int:
    separate_words = book_text.split()
    return len(separate_words)

def counting_characters(book_text: str) -> dict[str, int]:
    character_count = {}

    for character in book_text:
        character = character.lower()

        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count