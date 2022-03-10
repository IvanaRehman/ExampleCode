import nltk
import re
import os
import csv
import pprint
import collections
from nltk.tokenize import word_tokenize, sent_tokenize

"""
This program takes as input a folder of text files with transcriptions of speech
and returns a csv file with number of repairs, repetitions, pauses, and words per speaker.
The code is following the transcription/annotation for the particular dataset.
"""

dirpath = '/Users/Ivana/Downloads/Trans'
files = os.listdir(dirpath)

file = "/Users/Ivana/Desktop/PythonNew.csv"
    #writer = csv.writer(open(file, 'w'))
writer = open(file, "w")

for file in files:
    list = []
    with open(os.path.join(dirpath, file), 'r') as inp:
        data = inp.read().replace('\n', '')
        #print(data)
        data1 = re.sub('%.{2}', 'PAUSE ', data)
        data1= re.sub('\[(.*?)\]', 'PAUSE ', data1)
        #print(data)
        list = re.split('==>', data1)
        #print(list)
        for sent in sent_tokenize(data):
            words = word_tokenize(sent)
    tagged = nltk.pos_tag(nltk.word_tokenize(sent))
    pausecount = []
    #print(tagged)
    for item in list:
        count = 0
        for word in item.split():
            if word == "PAUSE":
                count = count + 1
        pausecount.append(count)
    repetitions = []
    for item in list:
        repcount = 0
        itemlist = item.split()
        for i in range(len(itemlist) - 1):
            if itemlist[i] == itemlist[i+1]:
                repcount = repcount + 1
        repetitions.append(repcount)
    repairs =[]
    listforwords = []
    for item in list:
        repair = 0
        itemlist = item.split()
        for i in range(len(itemlist)):
            #print (itemlist[i])
            if re.search('[a-zA-Z]+\-$', itemlist[i]):
                repair = repair + 1
        repairs.append(repair)
        data = re.sub('%.{2}', '', data)
        data = re.sub('\[(.*?)\]', '', data)
        data = re.sub('[a-zA-Z]+\-[\s,]', '', data)
        data = re.sub('\<UNK\>', '', data)
        data = re.sub(r'\b(\w+)( \1\b)+', r'', data)
        data = ' '.join(data.split())
        listforwords = re.split('==>', data)
    wordcountlist = []
    for item in listforwords:
        wordcount = 0
        for word in item.split():
            wordcount = wordcount + 1
        wordcountlist.append(wordcount)
    print("This is the number of repairs: ", repairs[1:])
    print("This is the number of repetitions: ", repetitions[1:])
    print("This is the number of pauses per response: ", pausecount[1:])
    print("This is the number of words per response: ", wordcountlist[1:])

    counter = collections.defaultdict(int)

    line = ""
    for item in repairs:
        line += str(item) + "\n"
    for item in repetitions:
        line += str(item) + "\n"
    for item in pausecount:
        line += str(item) + "\n"
    for item in wordcountlist:
        line += str(item) + "\n"
    writer.write(line)
    #print(line)
    writer.write("\n")
writer.close()
    #print(listforwords)
    #print(data)
    #pprint.pprint(listforwords)
