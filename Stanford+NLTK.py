from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
import pprint
import re
import string
from nltk.tree import *

#Uses Stanford parser and NLTK to count occurrences of phrases (noun, verb, prepositional)


parser_folder = "stanford-parser-full-2017-06-09/"

parser_jar = parser_folder + "stanford-parser.jar"
models_jar = parser_folder + "stanford-parser-3.8.0-models.jar"


const_parser = StanfordParser(parser_jar, models_jar)
dep_parser = StanfordDependencyParser(parser_jar, models_jar)

def countTrees(tree):
    nps = 1
    vps = 1
    pps = 1
    NPlength = []
    VPlength = []
    PPlength = []
    for item in tree:
        for subtree in Tree.subtrees(item):
            if Tree.label(subtree) == 'NP':
                NPlength.append(len(Tree.leaves(subtree)))
                nps = nps+1
            elif Tree.label(subtree) == 'VP':
                VPlength.append(len(Tree.leaves(subtree))) #Length of the phrase
              #  print(Tree.label(subtree))
                vps = vps+1
            elif Tree.label(subtree) == 'PP':
               # print(Tree.label(subtree))
                PPlength.append(len(Tree.leaves(subtree)))
                pps = pps+1
    #NPct.append(nps)
    #VPct.append(vps)
    #PPct.append(pps)
    return [nps,vps,pps, sum(NPlength)/nps, sum(VPlength)/vps, sum(PPlength)/pps]

ELE = []
INT = []
ADV = []
mainlist = []

text = open('/Users/Ivana/Desktop/RA Sowmya/INTADV.txt', 'r')
for line in text:
    line = re.sub('\*\*\*\*\*\*\*', '', line)
    line = re.sub('\n', '', line)
    if line != '':
        mainlist.append(line)

ELE = mainlist[0::2]  #takes odd sentences (ele ones)
INT = mainlist[1::2]  #takes even sentences
print(len(ELE))
print(len(INT))
NPct = []
VPct = []
PPct = []
NPLen = []
VPLen = []
PPLen = []
#pprint.pprint((list))
count = 0
for item in ELE:
    #print(item)
    const_output = const_parser.raw_parse(item)
    #print(item)
    output = countTrees(const_output)
    NPct.append(output[0])
    VPct.append(output[1])
    PPct.append(output[2])
    NPLen.append(output[3])
    VPLen.append(output[4])
    PPLen.append(output[5])
    count = count +1
    #print(type(output))
#print(intEI)

print("Printing NP, VP, PP counts for Elementary sentences: ")
print(sum(NPct)/len(NPct))
print(sum(VPct)/len(VPct))
print(sum(PPct)/len(PPct))
print("Printing NPLen, VPLen, PPLen for Elementary sentences: ")
print(sum(NPLen)/len(NPct))
print(sum(VPLen)/len(VPct))
print(sum(PPLen)/len(PPct))

NPctI = []
VPctI = []
PPctI = []
NPLenI = []
VPLenI = []
PPLenI = []

for item in INT:
    #print(item)
    const_output = const_parser.raw_parse(item)
    #print(item)
    output = countTrees(const_output)
    NPctI.append(output[0])
    VPctI.append(output[1])
    PPctI.append(output[2])
    NPLenI.append(output[3])
    VPLenI.append(output[4])
    PPLenI.append(output[5])

print("Printing NP, VP, PP counts for Intermediate sentences: ")
print(sum(NPctI)/len(NPctI))
print(sum(VPctI)/len(VPctI))
print(sum(PPctI)/len(PPctI))
print("Printing NPLen, VPLen, PPLen for Intermediate sentences: ")

print(sum(NPLenI)/len(NPctI))
print(sum(VPLenI)/len(VPctI))
print(sum(PPLenI)/len(PPctI))
