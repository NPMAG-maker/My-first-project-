
import sys

if len(sys.argv) != 2:
        print("Use the program like this Usage: python3 main.py <path_to_book>")
        sys.exit(1)

clear_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
        return_value = get_book_text(clear_path)
        print(return_value)

main()

def word_counter(word_receptor):
        words = word_receptor.split()
        return len(words)

with open(clear_path, "r") as f:
        file_contents = f.read()

from stats import word_counter

num_words = word_counter(file_contents)
print(f"{num_words} words found in the document")


from stats import count_characters
counts = count_characters(file_contents)
print(counts)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



main()

def word_counter(word_receptor):
        words = word_receptor.split()
        return len(words)



from stats import word_counter

num_words = word_counter(file_contents)
print(f"{num_words} words found in the document")


from stats import count_characters
counts = count_characters(file_contents)

for letter in "abcdefghijklmnopqrstuvwxyz":
    print(f"{letter}: {counts.get(letter, 0)}")


from stats import sort_characters

counts_dict = count_characters(file_contents)
