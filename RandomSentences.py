import re
import pprint

#Generates random sentences based on input

AustenDict = {}
AC = open("AustenC.txt")
AustenC = AC.readlines()
for line in AustenC:
    AustenC = re.sub("\n", "", line)
    Aprob = AustenC.split(':')
    AustenDict[Aprob[0]] = AustenDict.get(Aprob[0], float(Aprob[1]))

inp = input("Enter the words you wish to make a sentence out of (don't use punctuation :D) : ")
#inp = 'love Catherine'
list = inp.split()

items = []

for item in list:
    newdict = {}
    for key, value in AustenDict.items():
        pattern = '\''+item+'\''
        if re.search(pattern, key):
            newdict[key] = newdict.get(key, value)
    if len(newdict) == 0:
        items.append(item + " is barely a word")
    else:
        pair = sorted(newdict.items(), key=lambda x: x[1], reverse = True)
        newpair = re.sub('[,\.:;”\'!-\/\?_]','', pair[0][0])
        items.append(newpair)

print("Here's your very random, grammatically incorrect, and most likely short sentence: ", ' '.join(items)+'.')
