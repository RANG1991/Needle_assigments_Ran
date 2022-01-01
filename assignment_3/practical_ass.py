from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


def main():
    words = []
    with open("./Pride_Jane_Air_Book.txt", "r", encoding="utf8") as f:
        for row in f:
            words += word_tokenize(row)
    fdist = FreqDist(words)
    print(fdist)


if __name__ == "__main__":
    main()
