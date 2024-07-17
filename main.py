"""imports"""
from typing import Dict
from os import path as p


def main():
    """main function"""
    book_path = "./books/frankenstein.txt"
    book = open_book(book_path)
    num_of_words = count_words(book)
    chars = count_char(book)

    print_report(book_path, num_of_words, chars)


def open_book(path: str, enc: str = "utf-8") -> str:
    """open a book file"""
    book_content = ""
    with open(path, encoding=enc) as f:
        book_content = f.read()

    return book_content


def count_words(text: str) -> int:
    """count the num of words in a string"""
    split_text = text.split()
    return len(split_text)


def count_char(text: str) -> Dict[str, int]:
    """count the num of chars in a string"""
    cache: Dict[str, int] = {}
    for char in text:
        l = char.lower()
        if l.isalpha():
            if not cache.get(l):
                cache[l] = 1
            else:
                cache[l] += 1

    cache_keys = cache.keys()
    cache_keys = sorted(cache_keys)
    cache = {k: cache[k] for k in cache_keys}

    return cache


def print_report(path: str, num_of_words: int, chars: Dict[str, int]) -> None:
    """print report"""
    print()
    print(f"------- Starting a report on '{p.basename(path)}' -------")
    print(f"*** {num_of_words} words found in the file ***")
    print()

    for key in chars:
        print(f"The '{key}' character appears {chars[key]} times")

    print()
    print("------- Report completed -------")
    print()


if __name__ == "__main__":
    main()
