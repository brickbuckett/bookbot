def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    sanitized_text = get_sanitized_text(text)
    letter_count = get_letter_count(sanitized_text)
    list_of_dictionaries = get_list_of_dictionaries(letter_count)
    report(word_count, list_of_dictionaries, book_path)

def report(word_count, list_of_dictionaries, book_path):
    print (f"--- Begin report of {book_path} ---")
    print (f"There are {word_count} words in this document")
    print("")
    for x in list_of_dictionaries:
        print(f"The letter {x['letter']} was found {x['count']} times")

def get_list_of_dictionaries(letter_count):
    list_of_tups = list(letter_count.items())
    keys = ['letter', 'count']
    list_of_dictionaries = []
    for tup in list_of_tups:
        list_of_dictionaries.append(dict(zip(keys, tup)))
    sorted_list = sorted(list_of_dictionaries, key=lambda x: x['count'], reverse=True)
    return sorted_list

def get_word_count(text):
    wc = len(text.split())
    return wc

def get_sanitized_text(text):
    text_lowercase = text.lower()
    character_split = [x for x in text_lowercase]
    remove_special_characters = [x for x in character_split if x.isalnum()]
    remove_numbers = [x for x in remove_special_characters if not x.isdigit()]
    sanitized_text = remove_numbers
    return sanitized_text

def get_letter_count(sanitized_text):
    lc_dict = {}
    for letter in sanitized_text:
        if letter in lc_dict:
            lc_dict[letter] += 1
        else:
            lc_dict[letter] = 1
    return lc_dict

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()