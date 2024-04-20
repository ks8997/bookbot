def main():
    path = "books/frankenstein.txt"
    text = read_txt(path)
    n = num_words(text)
    print(n)

def read_txt(path):
    f = open(path)
    c = f.read()
    f.close()
    return c

def num_words(text):
    words = text.split()
    return len(words)


main()