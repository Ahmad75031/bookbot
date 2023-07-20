def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    words = text.split()
    character_count = count_each_letter(words)
    sorted_character_count = sorted_list(character_count)
    print("-- Begin report --")
    print(f"Number of words {number_of_words(words)}")
    for item in sorted_character_count:
        print(f"The '{item['ch']}' characker was found {item['num']} times")
    print("--- End report ---")
def number_of_words(text):
    number = 0
    for i in text:
        number += 1
    return number

def get_book_text(bookpath):
    with open("books/frankenstein.txt") as f:
        return f.read()
def sort_on(d):
    return d["num"]

def sorted_list(character_dic):
    sorted_list = []
    for character in character_dic:
        sorted_list.append({"ch":character , "num":character_dic[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def count_each_letter(text):
    each_letter = dict()
    for word in text:
        lower_word = word.lower()
        for c in lower_word:
            if not c.isalpha():
                continue
            if c in each_letter.keys():
                each_letter[c] += 1
            else:
                each_letter[c] = 1
    return each_letter
main()

