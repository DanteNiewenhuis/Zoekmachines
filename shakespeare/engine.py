from __future__ import division
from collections import Counter,defaultdict
from bs4 import BeautifulSoup
import os
import glob
import nltk
import math
import matplotlib.pyplot as plt

def count_tokens(folder):
    result = 0 # initialize Myindex
    for infile in os.listdir(folder):  # loop over each file
        with open(folder +'/'+ infile, 'r') as f:  # open file
            for w in f:     
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

# make a dict with the corpus frequency and the dictionary frequency 
# for every word
def frequency_index(Myindex):
    freq_index = {}
    for word in Myindex:
        result = 0
        for index in Myindex[word]:
            result += Myindex[word][index]

        freq_index[word]=[len(Myindex[word]),result] 

    return freq_index

# return the amount of words that have the right the corpus frequency or 
# dictionary frequency mode:0 will give the dictionary frequency and mode:1 the corpus. 
def frequency_checker(index, amount, mode, greater=False):
    result = 0 
    if greater:
        for word in index:
            if index[word][mode] > amount:
                result += 1
    else:
        for word in index:
            if index[word][mode] == amount:
                result += 1
    return result

def corpus_frequency(freq_table):
    result = []
    for word in freq_table:
        result.append(math.log(freq_table[word][1]))
    return result

def opdracht1():
    MyIndex = index_collection(folder)
    print(count_tokens[folder]) # total tokens in the corpus
    print(len(MyIndex)) # total unique tokens in the corpus


def opdracht5(folder):
    MyIndex = index_collection(folder)
    freq_table = frequency_index(MyIndex)

    print(len(freq_table))
    print(frequency_checker(freq_table, 1, 1))
    print(frequency_checker(freq_table, 1, 0))
    print(frequency_checker(freq_table, len(os.listdir(folder)), 0))
    print(frequency_checker(freq_table, len(os.listdir(folder))/2, 0, greater=True))


def opdracht6(folder):
    MyIndex = index_collection(folder)
    freq_table = frequency_index(MyIndex)
    corpus_freq = corpus_frequency(freq_table) # get a list of frequencies of words in the corpus descending
    sort_freq = sorted(corpus_freq, reverse=True) # sort the list
    x_axis = []
    for x in range(1,len(sort_freq)+1):
        x_axis.append(math.log(x))

    #plot the graph
    plt.plot(x_axis, sort_freq)
    plt.show()   

folder = 'tokens'
