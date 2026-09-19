# BOOKBOT!!!!

## Description

BookBot is a Python program that analyzes novels and reports their word and character counts. It reads a `.txt` file and generates a formatted word and character count report.

## Status

✅ Core features complete:
- word counting (13/10/2026)
- character counting (13/10/2026)
- sorting characters by frequency (14/10/2026)
- formatted report output (15/10/2026)

## Features

- Reads the full text of a book from a `.txt` file
- Counts the total number of words in the book
- Counts how many times each character appears (case-insensitive), including spaces and symbols
- Sorts characters from most to least frequent
- Prints a formatted report to the terminal, filtering out non-alphabetic characters (spaces, punctuation, symbols)

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

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============ END ==============


## How It Works (this specific project, variables can change)

**main.py**
- `get_book_text(path)` — opens the given file and returns its full contents as a string
- `print_report(book_path, word_count, character_counts)` — prints the full formatted report: header, book path, word count, and filtered/sorted character counts
- `main()` — loads the book, calculates word and character counts, and calls `print_report` to display the results

**stats.py**
- `words_in_book(book_text)` — splits the text into words and returns the total word count
- `counting_characters(book_text)` — loops through the text, lowercases each character, and returns a dictionary mapping each character to how many times it appears
- `sort_on(character_count_pair)` — helper function used for sorting; given a `(character, count)` tuple, returns just the count
- `chars_dict_to_sorted_list(sorted_dict)` — converts the character-count dictionary into a list of `(character, count)` tuples, sorted from most to least frequent

## Troubleshooting Notes

- **IndentationError while refactoring `main()`**: After moving print logic into a new `print_report` function, some old commented-out lines were left behind with mismatched indentation, causing `IndentationError: unindent does not match any outer indentation level`. Fixed by deleting the stray leftover lines entirely rather than trying to patch their spacing. Lesson: when refactoring, fully remove old code rather than commenting it out in place, to avoid indentation drift.