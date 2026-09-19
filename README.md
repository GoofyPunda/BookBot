# BOOKBOT!!!!

## Description

BookBot is a Python program that analyzes novels and reports their word and character counts. It reads a `.txt` file (given via a command-line argument) and generates a formatted word and character count report.

## Status

✅ Project complete:
- word counting (13/10/2026)
- character counting (13/10/2026)
- sorting characters by frequency (14/10/2026)
- formatted report output (15/10/2026)
- command-line arguments for any book path (16/10/2026)

## Features

- Accepts any `.txt` book path as a command-line argument
- Reads the full text of a book from a `.txt` file
- Counts the total number of words in the book
- Counts how many times each character appears (case-insensitive), including spaces and symbols
- Sorts characters from most to least frequent
- Prints a formatted report to the terminal, filtering out non-alphabetic characters (spaces, punctuation, symbols)

## Project Structure (files/folders) - Updated at the end to add additional books
```
├── books/
│ ├── frankenstein.txt
│ ├── mobydick.txt
│ └── prideandprejudice.txt
├── .gitignore
├── main.py
├── stats.py
└── README.md
```



## Requirements

- Python 3 (Python.org download)

## Usage

Run the script from the project root directory, passing the path to a book as an argument:

```zsh
python3 main.py books/frankenstein.txt
```

You can analyze any `.txt` file — place it in the `books/` folder and pass its path as the argument. If no path is given, the program prints a usage message and exits:

Usage - python3 main.py <path_to_book>

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
- `main()` — reads the book path from command-line arguments (via `sys.argv`), calculates word and character counts, and calls `print_report` to display the results. Exits with a usage message if no book path is provided.

**stats.py**
- `words_in_book(book_text)` — splits the text into words and returns the total word count
- `counting_characters(book_text)` — loops through the text, lowercases each character, and returns a dictionary mapping each character to how many times it appears
- `sort_on(character_count_pair)` — helper function used for sorting; given a `(character, count)` tuple, returns just the count
- `chars_dict_to_sorted_list(sorted_dict)` — converts the character-count dictionary into a list of `(character, count)` tuples, sorted from most to least frequent

## AANOYING Troubleshooting Notes

- **IndentationError while refactoring `main()`**: After moving print logic into a new `print_report` function, some old commented-out lines were left behind with mismatched indentation, causing `IndentationError: unindent does not match any outer indentation level`. Fixed by deleting the stray leftover lines entirely rather than trying to patch their spacing. Lesson: when refactoring, fully remove old code rather than commenting it out in place, to avoid indentation drift.

- **IndentationError when adding `sys.argv` validation**: Lines inside an `if` block (like the usage message and `sys.exit(1)`) must be indented one level deeper than the `if` itself. Missing this caused `expected an indented block after 'if' statement`. Lesson: code inside any block (`if`, `for`, function body, etc.) always needs consistent, deeper indentation than the line that opens the block.

- **Type hint typo (`tuple(str, int)` vs `tuple[str, int]`)**: Accidentally used parentheses instead of square brackets in a type hint, which tried to call Python's `tuple()` constructor with two arguments instead of writing a valid type annotation, causing a `TypeError`. Lesson: type hints for generics like `tuple`, `list`, and `dict` always use square brackets (`tuple[str, int]`), never parentheses.