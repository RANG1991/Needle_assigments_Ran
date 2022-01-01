from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

plurals = ["photo", "photon"]

singles = [stemmer.stem(plural) for plural in plurals]

print(singles)
