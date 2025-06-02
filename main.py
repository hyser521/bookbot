from stats import count_letters, count_words, report
import sys
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    letter_dict = count_letters(text)
    rpt = report(letter_dict, word_count)
    print(rpt)



main()