# BOOKBOT!!!!

## Description

BookBot is a Python program that analyzes novels and reports their word and character counts. It reads a `.txt` file and generates a simple word and character count report.

## Status

🚧 In progress:
- word counting complete (13/10/2026)
- character counting complete (13/10/2026)
- report formatting coming next

## Features

- Reads the full text of a book from a `.txt` file
- Counts the total number of words in the book
- Counts how many times each character appears (case-insensitive), including spaces and symbols
- Prints a summary report to the terminal

## Project Structure(files/folders)

```
├── books/
│   └── frankenstein.txt
├── main.py
├── stats.py
└── README.md
```

## Requirements

- Python 3 (Python.org download)

## Usage

Run the script from the project root directory:

```zsh
python3 main.py
```

By default, the script analyzes `books/frankenstein.txt`. To analyze a different book, place the `.txt` file in the `books/` folder and update the `book_path` variable inside the `main()` function in `main.py`.

## Example Output

- Found 75767 total words
- {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, ...}


## How It Works (this specific project, variables can change)

**main.py**
- `get_book_text(path)` — opens the given file and returns its full contents as a string
- `main()` — loads the book, calculates word and character counts, and prints the results


**stats.py**
- `words_in_book(book_text)` — splits the text into words and returns the total word count
- `counting_characters(book_text)` — loops through the text, lowercases each character, and returns a dictionary mapping each character to how many times it appears
- `sort_on(character_count_pair)` — helper function used for sorting; given a `(character, count)` tuple, returns just the count
- `chars_dict_to_sorted_list(sorted_dict)` — converts the character-count dictionary into a list of `(character, count)` tuples, sorted from most to least frequent