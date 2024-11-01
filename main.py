def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    if text:
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()

        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")




def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

import re

def get_chars_dict(text):
    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""  # returning an empty string to ensure the rest of the code doesn't crash
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""



main()


