import math

from nltk import RegexpTokenizer
from nltk.probability import FreqDist
from matplotlib import pyplot as plt


def main():
    words = []
    tokenizer = RegexpTokenizer(r"\w+")
    with open("./Pride_Jane_Air_Book.txt", "r", encoding="utf8") as f:
        for row in f:
            words += tokenizer.tokenize(row)
    fdist = FreqDist(words)
    tokens_list = fdist.most_common()
    log_rank = [math.log(i) for i in range(1, len(tokens_list) + 1)]
    log_freq = [math.log(x[1]) for x in tokens_list]
    plt.plot(log_rank, log_freq)
    plt.show()


if __name__ == "__main__":
    main()
