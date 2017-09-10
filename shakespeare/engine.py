from __future__ import division
from collections import Counter,defaultdict
from bs4 import BeautifulSoup
import os
import glob
import nltk
import math

def count_tokens(folder):
    result = 0 # initialize Myindex
    for infile in os.listdir(folder):  # loop over each file
        with open(folder +'/'+ infile, 'r') as f:  # open file
            for w in f:    # update Myindex with each token 
                result+=1
                
    return result

def index_collection(folder):
    Myindex = defaultdict(Counter) # initialize Myindex
    for infile in os.listdir(folder):  # loop over each file
        fileIndex = os.path.basename(infile).replace('.xml','')
        print ("current file is: " + fileIndex)
        with open(folder +'/'+ infile, 'r') as f:  # open file
            for w in f:    # update Myindex with each token 
                Myindex[w[:-2]][fileIndex]+=1

    return Myindex

def frequency_index(Myindex):
    freq_index = {}
    for word in Myindex:
        result = 0
        for index in Myindex[word]:
            result += Myindex[word][index]
        freq_index[word]=[len(Myindex[word]),result] 

    return freq_index

def frequency_checker(index, amount, mode):
    result = 0 
    for word in index:
        if index[word][mode] > amount:
            result += 1
    return result


MyIndex = index_collection('tokens')
freq_table = frequency_index(MyIndex)
print(frequency_checker(freq_table, 18, 1))

#freq_index = frequency_index(Myindex)
#print(freq_index['love'])