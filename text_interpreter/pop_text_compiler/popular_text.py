import nltk
from nltk.collocations import *
import requests
import collections
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json


class popText:
    def __init__(self):
        self.archiveMessages = []

        self.occurances_threshold = 3
        self.highest_ngram_pmi_lim = 10

    def collate_data(self, words):
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        #trigram_measures = nltk.collocations.TrigramAssocMeasures()

        tempColloList = []

        # makes a list of words from a json of words
        #words = json_to_words(json_data)
        #TODO:append time stamp to the end of the dictionary entries
        #append words dictionary to the end of persistent list
        self.archiveMessages.extend(words)
        #TODO: scan list for time stamps greater than 1 min
        tokenizer = RegexpTokenizer(r'\w+')

        for i in self.archiveMessages:
            message=i.get('message').lower()
            tokenizer.tokenize(message)
            tempColloList.extend(message)

        #TODO:incorperate stop word trimming
        #TODO: turn words to topic (dogs to dog)

        finder = BigramCollocationFinder.from_words(words)
        finder.apply_freq_filter(self.occurances_threshold)

        b=finder.nbest(bigram_measures.pmi, self.highest_ngram_pmi_lim)

        #TODO: glue value pairs together by space
        #TODO: get PMI and occurance for each value
        #

        for k, v in finder.ngram_fd.items():
            print(k,v)

        return b

        # TODO: may need code here that calls push_data

    def json_to_words(self, some_json):
        # TODO: makes sure to make the entries case neutral
        pass


#x = popText()
#a = [{'username': 'spiderinqz', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'the_mathcat', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'pepsidude555', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'lavow', 'message': u'SPAM SMOrc THIS SMOrc BOSS SMOrc TO SMOrc MOURN SMOrc SHANGHAI\u2019S SMOrc loss', 'channel': '#overwatchleague'}, {'username': 'phaaedra', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'acalacaboo', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'danzilla132', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'irrelavantstreams', 'message': u'Hey i got 100 tokens', 'channel': '#overwatchleague'}, {'username': 'bazzlover69', 'message': u'LOL', 'channel': '#overwatchleague'}]
#c=x.collate_data(a)
#print(c)

def biggestCommenters(listOfDictsIn):
    usersList = [li['username'] for li in listOfDictsIn] #makes list of all the usernames
    #for x in listOfDictsIn

    counter = collections.Counter(usersList) #now make it into a dictionary of usernames as keys, fields are count, from highest to lowest

    return json.loads(json.dumps(counter)) #loads to desired dict json representation


#biggestCommenters([{'username': 'spiderinqz', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'the_mathcat', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'pepsidude555', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'lavow', 'message': u'SPAM SMOrc THIS SMOrc BOSS SMOrc TO SMOrc MOURN SMOrc SHANGHAI\u2019S SMOrc loss', 'channel': '#overwatchleague'}, {'username': 'phaaedra', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'the_mathcat', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'danzilla132', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'irrelavantstreams', 'message': u'Hey i got 100 tokens', 'channel': '#overwatchleague'}, {'username': 'bazzlover69', 'message': u'LOL', 'channel': '#overwatchleague'}])