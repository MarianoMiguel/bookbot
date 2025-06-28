from stats import words_in_document
from stats import get_sorted_character_counts

def get_book_text(filepath): 
    with open(filepath) as f:
      file_contents = f.read()
      return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    sorted = get_sorted_character_counts(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {words_in_document(book)} total words")
    print("--------- Character Count -------")
    for key in sorted:
        print(f"{key["char"]}: {key["num"]}")

main()
