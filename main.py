def main():
    file = "books/frankenstein.txt"

    text = get_book_text(file)
    wordcount = count_words(text)

    print(f"[1] Il y a {wordcount} mots dans ce texte")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_content):
    words = file_content.split()
    return len(words)
    


main()