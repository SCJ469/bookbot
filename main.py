import sys
import time

if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return(book_text)

from stats import get_word_count
from stats import get_character_count
from stats import sorted_list

def main():
    book = str(sys.argv[1])
    book_text = get_book_text(book)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sorted_list(character_count)
    sorted_dict = dict(sorted_character_count)

    report = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {book}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------"
    )
    
    print(report)
    for character in sorted_character_count:
        if character[0].isalpha():
            print(f'{character[0]}: {character[1]}')
    print("============= END ===============")

main()