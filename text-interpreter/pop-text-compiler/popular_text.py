import nltk
from nltk.collocations import *
import requests


def popular_text():
    words = None

    occurances_threshold = None
    highest_ngram_pmi_lim = None


    def __init__(self):
        pass

    def get_data():
        pass

    def push_data():
        pass

    def collate_data(json_data):
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        trigram_measures = nltk.collocations.TrigramAssocMeasures()

        # makes a list of words from a json of words
        words = json_to_words(json_data)

        finder = BigramCollocationFinder.from_words(words)
        finder.apply_freq_filter(occurances_threshold)

        finder.nbest(bigram_measures.pmi, highest_ngram_pmi_lim)

        # TODO: may need code here that calls push_data

    def json_to_words(some_json):
        # TODO: makes sure to make the entries case neutral

        pass


