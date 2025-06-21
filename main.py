from stats import word_count
from stats import char_count
from stats import sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    num_words = word_count(get_book_text(book))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = char_count(get_book_text(book))
    sorted_dict = sort(num_char)
    for d in sorted_dict:
        if d["char"].isalpha():
            char = d["char"]
            num = d["num"]
            print(f"{char}: {num}")
    print("============= END ===============")

main()