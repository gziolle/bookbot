import sys
from stats import count_words, count_chars, get_char_report

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_formatted(filepath, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for tuple in char_list:
        if tuple["char"].isalpha():
            print(f"{tuple["char"]}: {tuple["num"]}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    contents = get_book_text(filepath)
    word_count = count_words(contents)
    char_list = get_char_report(count_chars(contents))

    print_formatted(filepath, word_count, char_list)


main()