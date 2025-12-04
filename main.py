import sys
from stats import get_num_words,count_letters,sort_order,chars_dict_to_sorted_list


def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
    return file_contents

def main() :
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    letters_counted = count_letters(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(letters_counted)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()