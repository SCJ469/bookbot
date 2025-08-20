def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return(word_count)

def get_character_count(book_text):
    lower_book_text = book_text.lower()
    letters = {}

    for character in lower_book_text:
        if character in letters:
            letters[character] += 1
        else:
            letters[character] = 1

    return(letters)

def sorted_list(character_count):
    def sort_on(character_count):
        return character_count[1]

    character_count = list(character_count.items())
    character_count.sort(reverse=True, key=sort_on)
    return character_count

