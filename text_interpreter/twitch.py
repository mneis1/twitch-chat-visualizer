from __future__ import print_function
import nltk
from nltk.collocations import *
import requests
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json


class popText:
    def __init__(self):
        self.archiveMessages = []
        self.tempColloList = []
        self.occurances_threshold = 2
        self.highest_ngram_pmi_lim = 10

    def collate_data(self, words):
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        #trigram_measures = nltk.collocations.TrigramAssocMeasures()

        tempDictList = []

        # makes a list of words from a json of words
        #words = json_to_words(json_data)
        #TODO:append time stamp to the end of the dictionary entries
        #append words dictionary to the end of persistent list

        self.archiveMessages.extend(words)
        #TODO: scan list for time stamps greater than 1 min
        tokenizer = RegexpTokenizer(r'\w+')

        for i in self.archiveMessages:
            message=i.get('message').lower().split()
            #tokenizer.tokenize(message)
            self.tempColloList.extend(message)

        stop = set(stopwords.words('english'))
        self.tempColloList = [w for w in self.tempColloList if not w in stop]

        #TODO:incorperate stop word trimming
        #TODO: turn words to topic (dogs to dog)

        finder = BigramCollocationFinder.from_words(self.tempColloList)
        finder.apply_freq_filter(self.occurances_threshold)

        finder.nbest(bigram_measures.pmi, self.highest_ngram_pmi_lim)

        #TODO: glue value pairs together by space
        #TODO: get PMI and occurance for each value
        #

        for k, v in finder.ngram_fd.items():
            tempDict = {}
            tempDict["name"] = " ".join(k)
            tempDict["size"] = v
            tempDictList.append(tempDict.copy())

        return json.dumps(tempDictList)


        # TODO: may need code here that calls push_data

    def json_to_words(self, some_json):
        # TODO: makes sure to make the entries case neutral
        pass


#x = popText()
#a = [{'username': 'spiderinqz', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'the_mathcat', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'pepsidude555', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'lavow', 'message': u'SPAM SMOrc the THIS SMOrc is BOSS SMOrc TO SMOrc MOURN SMOrc SHANGHAI\u2019S SMOrc loss', 'channel': '#overwatchleague'}, {'username': 'phaaedra', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'acalacaboo', 'message': u'F', 'channel': '#overwatchleague'}, {'username': 'danzilla132', 'message': u'100', 'channel': '#overwatchleague'}, {'username': 'irrelavantstreams', 'message': u'Hey i got 100 tokens', 'channel': '#overwatchleague'}, {'username': 'bazzlover69', 'message': u'LOL', 'channel': '#overwatchleague'}]
#c=x.collate_data(a)
#print(c)


#Reads data from a twitch server. Requires a username and oauth key.
#Adapted from tutorial: https://317070.github.io/python/
from twitchstream.outputvideo import TwitchOutputStreamRepeater
from twitchstream.chat import TwitchChatStream
import argparse
import time
import json
import numpy as np
import urllib2
import popular_text



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--username',
                          help='twitch username',
                          required=True)
    required.add_argument('-o', '--oauth',
                          help='twitch oauth '
                               '(visit https://twitchapps.com/tmi/ '
                               'to create one for your account)',
                          required=True)
    args = parser.parse_args()

    with TwitchChatStream(username=args.username,
                          oauth=args.oauth,
                          verbose=False)as chatstream:

        #Name of streamer's twitch chat to join.
        chatstream.join_channel("nickmercs")
        x = popText()

        while True:
            received = chatstream.twitch_receive_messages()
            if received:
                print("Received")
                print(received)
                print("\n")
            
                fJson = x.collate_data(received)
                print("JSON\n")
                print(fJson)
                print("\n\n\n")
                
                req = urllib2.Request('http://ec2-52-91-71-192.compute-1.amazonaws.com:8080/send')
                req.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(req, json.dumps(received))
                
                #for key in received:
                                        
                    #print(key)
                    
                
#                json.dumps(received)
#                print(  received)
#                print(dictionaryToJson(received))
#                for chat_message in received:
#                    print( chat_message['message'])
                #print("received:", received)
                #j = json.loads(re
            time.sleep(1)

