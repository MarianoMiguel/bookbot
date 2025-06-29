from stats import words_in_document
from stats import get_sorted_character_counts
import sys

def get_book_text(filepath): 
    with open(filepath) as f:
      file_contents = f.read()
      return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book = get_book_text(path)
    sorted = get_sorted_character_counts(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {words_in_document(book)} total words")
    print("--------- Character Count -------")
    for key in sorted:
        print(f"{key["char"]}: {key["num"]}")

main()
