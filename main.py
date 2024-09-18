def main():
    file = "books/frankenstein.txt"

    text = get_book_text(file)
    wordcount = count_words(text)
    charcount = count_chars(text)

    # Affichage final
    create_report(wordcount,charcount,file)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_chars(file_content):
    # Passe la string en minuscule pour éviter les doublons
    file_tolowercase = file_content.lower()
    chars_count_dic = {} # dictionnaire pour stocker le compte des lettres

    for char in file_tolowercase:
        if char.isalpha():
            if char not in chars_count_dic:
                chars_count_dic[char] = 1
            else:
                chars_count_dic[char] += 1
    
    return chars_count_dic

def create_report(wordcount,charcount,file):
    print(f"--- Begin report of {file} ---")
    print(f"{wordcount} words found in this document")

    for char in charcount.keys():
        print(f"The {char} character was found {charcount[char]} times")
    print("--- End Report ---")

        

    


main()