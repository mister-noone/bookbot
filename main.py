def main():

  BOOK_PATH = "./books/Silent_Patient.txt"
  eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
  
  with open(BOOK_PATH, "r") as b:
    book = b.read()
    num_of_words = count_words(book)
    chars = count_characters(book, eng_alphabet)
    chars_list = [item for item in chars.items()]
    print(f"\n--- Book report about '{BOOK_PATH}' ---\n")
    print(f"{num_of_words} words found in the file\n")
    for char in sorted(chars_list):
      print(f"The '{char[0]}' character was found {char[1]} times")
    
  

def count_words(text):
  split_text = text.split()    
  return len(split_text)
    
    
def count_characters(text, alphabet):
  chars = {}
  text = "".join(text.split())
  for char in text.lower():
    if char in alphabet:
      if not char in chars:
        chars[char] = 1
      chars[char] += 1
    
  return chars
  
    
if __name__ == "__main__":
  main()