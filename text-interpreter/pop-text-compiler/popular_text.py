import nltk
from nltk.collocations import *
import requests


class popText:
    def __init__(self):
        #self.words = None

        self.occurances_threshold = None
        self.highest_ngram_pmi_lim = None

    def get_data(self):
        pass

    def push_data(self):
        pass

    def collate_data(self, words):
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        trigram_measures = nltk.collocations.TrigramAssocMeasures()

        # makes a list of words from a json of words
        #words = json_to_words(json_data)

        finder = BigramCollocationFinder.from_words(words)
        finder.apply_freq_filter(self.occurances_threshold)

        finder.nbest(bigram_measures.pmi, self.highest_ngram_pmi_lim)

        # TODO: may need code here that calls push_data

    def json_to_words(self, some_json):
        # TODO: makes sure to make the entries case neutral

        pass