import math
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag
from matplotlib import pyplot as plt
from nltk.stem import PorterStemmer

def remove_punc(words_list):
    stop_words = set(stopwords.words('english'))
    words_list = [word for word in words_list if word not in stop_words]
    return words_list


def plot_words(words):
    fdist = FreqDist(words)
    tokens_list = fdist.most_common()
    log_rank = [math.log(i) for i in range(1, len(tokens_list) + 1)]
    log_freq = [math.log(x[1]) for x in tokens_list]
    plt.plot(log_rank, log_freq)
    plt.show()


def tokenize_book(book_file_path):
    words = []
    tokenizer = RegexpTokenizer(r"\w+")
    with open(book_file_path, "r", encoding="utf8") as f:
        for row in f:
            words += tokenizer.tokenize(row)
    return words


def main():
    words_tok = tokenize_book("./Pride_Jane_Air_Book.txt")
    plot_words(words_tok)
    word_wo_punc = remove_punc(words_tok)
    plot_words(word_wo_punc)
    pos_tags = pos_tag(words_tok)
    adj_noun_phrases = []
    current_phrase = []
    for word, tag in pos_tags:
        if "JJ" in tag:
            current_phrase.append(word)
        if "NN" in tag and len(current_phrase) > 0:
            current_phrase.append(word)
            adj_noun_phrases.append(tuple(current_phrase))
            current_phrase.clear()
    print(adj_noun_phrases)
    plot_words(adj_noun_phrases)


import re

if __name__ == "__main__":
    stemmer = PorterStemmer()
    print(stemmer.stem("officer"))
    print(stemmer.stem("office"))
    print(stemmer.stem("moral"))
    print(stemmer.stem("morale"))

    print(stemmer.stem("sure"))
    print(stemmer.stem("unsure"))
    print(stemmer.stem("special"))
    print(stemmer.stem("specialist"))

    # with open("./Pride_Jane_Air_Book.txt", "r", encoding="utf8") as f:
    #     s = f.read()
    #     two_consecutive_repeated_words_pattern = r"\b(\w+)(\W+)(\1)\b"
    #     results = re.findall(two_consecutive_repeated_words_pattern, s)
    #     for tup in results:
    #         print(tup[1].join([tup[0], tup[2]]))
    #     if results:
    #         print(len(results))
    #         print(results)
    #     else:
    #         print("No two consecutive repeated words pattern found")
