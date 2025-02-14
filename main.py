def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    character_dict = get_alpha_character_count(text.lower())
    print_characters(character_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(raw_text):
    words = raw_text.split()
    return len(words)

    
def get_character_count(text):
    characters = {}
    for word in text:
        for character in word:
            characters[character] = characters.get(character, 0) + 1
    return dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))
        
def get_alpha_character_count(text):
    characters = {}
    for word in text:
        for character in word:
            if(character.isalpha()):
                characters[character] = characters.get(character, 0) + 1
    return dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))

def print_characters(letters):
    for letter in letters:
        print(f"The '{letter}' character was found {letters.get(letter)} times")

main()