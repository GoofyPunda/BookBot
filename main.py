def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()
