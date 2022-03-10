import nltk
import re
from nltk import pos_tag, word_tokenize

#Counts phrase occurrences

sent = input("Enter a sentence: ")
tagged = pos_tag(word_tokenize(sent))
print(tagged)
templist = []
for i in range(len(tagged)):
    if tagged[i][1].startswith('V'):
        templist.append('VP')
        templist.append(tagged[i][0])
    elif tagged[i][1] == "MD":
        templist.append("VP")
        templist.append(tagged[i][0])
    elif tagged[i][1] == "IN":
        templist.append("PP")
        templist.append(tagged[i][0])
    elif tagged[i][1] == "RB":
        templist.append("AdvP")
        templist.append(tagged[i][0])
    else:
        templist.append("NP")
        templist.append(tagged[i][0])
output = [templist[0], templist[1]]
for i in range(0, len(templist)-2, 2):
    if templist[i] == templist[i+2]:
        output.append(templist[i+3])
    else:
        output.append(templist[i+2])
        output.append(templist[i+3])
string = ' '.join(output)
string1 = re.sub('(VP|PP|NP|AdvP)', r"][\1", string)
string2 = re.sub('^]', r"", string1)
string3 = re.sub('([\.\?!]$)', r"]\1", string2)
print(string3)
