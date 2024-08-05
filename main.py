def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    num_letters = {}
    for letter in text:
        letter = letter.lower()
        if(letter in num_letters):
            num_letters[letter] +=1
        else:
            num_letters[letter] = 1
    return num_letters

def get_book(path):
    with open(path) as f:
        return f.read() 

def report(word_count, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for entry in characters:
        print(f"'{entry['name']}' was found {entry['num']} times")
    print()
    print("--- End report ---")
    return

def sort_on(dict):
    return dict["num"]

def list_convert(dict):
    chars = []
    for char in dict:
        if(char.isalpha()):
            chars.append({"name" : char, "num" : dict[char]})
    return chars
    

def main():
   book_path = "books/frankenstein.txt"
   text = get_book(book_path)
   num_words = word_count(text)
   letter_count = char_count(text)
   letters_list = list_convert(letter_count)
   letters_list.sort(reverse=True, key=sort_on)
   report(num_words, letters_list)
   #print(f"there are {num_words} words")
   #print(f"{letter_count}")

main()