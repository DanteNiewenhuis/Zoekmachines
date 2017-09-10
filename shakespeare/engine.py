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
                Myindex[w.replace('\n','')][fileIndex]+=1

    return Myindex

def index_collection2(folder):
    MyIndex= defaultdict(Counter) # initialize MyIndex
    for infile in os.listdir(folder):  # loop over each file
        fileIndex = os.path.basename(folder + '/' + infile).replace('.xml','')
        print("current file is: " + fileIndex)
        with open(folder + '/' + infile, 'r') as f:  # open file
            soup = BeautifulSoup(f.read(), 'lxml')  # get the text out
            text = [w.lower() for w in nltk.word_tokenize(soup.get_text())]   # tokenize, lower case
            for w in text:    # update MyIndex with each token 
                MyIndex[w][fileIndex]+=1
                
    return MyIndex

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

def corpus_frequency(freq_table):
    result = []
    for word in freq_table:
        result.append([word, freq_table[word][1]])

    return result

MyIndex = index_collection('tokens')
freq_table = frequency_index(MyIndex)
corpus_freq = corpus_frequency(freq_table)
sort_freq = sorted(corpus_freq, key=lambda student: student[1], reverse=True)
print(sort_freq[:5])

#freq_index = frequency_index(Myindex)
#print(freq_index['love'])