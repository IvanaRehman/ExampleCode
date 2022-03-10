import nltk
import re
import os
import string
from nltk.stem import WordNetLemmatizer
import pprint

"""
Performs a variety of calculations:
- word density
- first 1000K most frequent
- first 2000K most frequent
- academic word list percentage
- fourgrams
- PP phrases
- VP phrases
- NP phrases
"""


dirpath = '/Users/Ivana/Downloads/TestFiles' #make sure to put the appropriate directory where the taggedfilles folder is on your computer
files = os.listdir(dirpath)

file = "/Users/Ivana/Desktop/attachments/ENGL 515/DataTest.txt" #same - pay attention to the directory
writer = open(file, 'w')
writer.write('level\twordcount\tcontent word\tK1\tK2\tAWL\tTTR\tPPBased\tNPBased\tVPBased\n')

AWLK1t = open('AWLK1w.txt')
AWLK1 = AWLK1t.read().lower()
AWLK1 = AWLK1.replace("\\", "").split()
AWLK2t = open('AWLK2w.txt')
AWLK2 = AWLK2t.read().lower()
AWLK2 = AWLK2.replace(",,\\", "").split()
AWL1 = open('AWL.txt')
AWL = AWL1.read().lower().replace(" ", "").split()

lemmatizer = WordNetLemmatizer()
for file in files:
    list = []
    with open(os.path.join(dirpath, file), 'r') as inp:
        if file.endswith(".txt"):
            mainlist = []
            #print(file[0])
            data = inp.readlines()
            #print(data)
            count = len(data[12:])
            #print(count)
            dicttype = {}
            contentw = 0
            countK1 = 0
            countK2 = 0
            countAWL = 0
            for line in data[12:]:
                #print (line)replace('\n', '')
                wordtag = line.split(" ^")
                mainlist.append(wordtag)
                #print(wordtag)
                tag = ""
                lemma = ""
                if re.search('^\w', wordtag[0]):
                    #print(wordtag[0])
                    if wordtag[1].startswith("n"):
                        tag = "n"
                        contentw = contentw + 1
                        lemma = lemmatizer.lemmatize(wordtag[0].lower(), pos= tag)
                    elif wordtag[1].startswith("j"):
                        tag = "a"
                        contentw = contentw + 1
                        lemma = lemmatizer.lemmatize(wordtag[0].lower(), pos= tag)
                    elif wordtag[1].startswith("v"):
                        tag = "v"
                        contentw = contentw + 1
                        lemma = lemmatizer.lemmatize(wordtag[0].lower(), pos= tag)
                    elif wordtag[1].startswith("rb"):
                        tag = "r"
                        contentw = contentw + 1
                        lemma = lemmatizer.lemmatize(wordtag[0].lower(), pos= tag)
                    else:
                        lemma = wordtag[0].lower()
                dicttype[lemma] = dicttype.get(lemma, 0) + 1

                if lemma in set(AWLK1):
                    countK1 = countK1 + 1
                if lemma in set(AWLK2):
                    countK2 = countK2 + 1
                if lemma in set(AWL):
                    countAWL = countAWL + 1
            density = contentw/count
            K1 = countK1/count
            K2 = countK2/count
            AWLc = countAWL/count
            fourgram = []
            PPBased = []
            VPBased = []
            NPBased = []
            for i in range(len(mainlist)-3):
                if mainlist[i][0] not in string.punctuation and mainlist[i+1][0] not in string.punctuation and mainlist[i+2][0] not in string.punctuation and mainlist[i+3][0] not in string.punctuation:
                    fourgram.append((mainlist[i], mainlist[i+1], mainlist[i+2], mainlist[i+3]))
            for tup in fourgram:
                if tup[0][1].startswith('in+') or tup[0][1].startswith('pi+'):
                    PPBased.append(tup)
                elif tup[0][1].startswith('n') or tup[0][1].startswith('at') or tup[0][1].startswith('d'):
                    NPBased.append(tup)
                elif (tup[0][1].startswith('md') and tup[3][0] == 'that') or (tup[0][1].startswith('v') and not tup[0][1].startswith('vbg') and not tup[0][1].startswith('vwbg') and not tup[0][1].startswith('vwbn') and not tup[0][1].startswith('vprf')):
                    VPBased.append(tup)
            #print(len(VPBased))

            line = ""
            types = len(dicttype)
            TTR = types/count
            writer.write(file[0] + '\t')
            writer.write(str(count) + '\t')
            writer.write(str(density) + '\t')
            writer.write(str(K1) + '\t')
            writer.write(str(K2) + '\t')
            writer.write(str(AWLc) + '\t')
            writer.write(str(TTR) + '\t')
            writer.write(str(len(PPBased)) + '\t')
            writer.write(str(len(NPBased)) + '\t')
            writer.write(str(len(VPBased)) + '\n')

writer.close()
