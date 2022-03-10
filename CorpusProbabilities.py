import re
import math

L1 = 0.33
L2 = 0.33
L3 = 0.34

#Transferring information from text files into dictionary to use in this program:
#Austen Corpus data:
AustenDict = {}
AC = open("AustenC.txt")
AustenC = AC.readlines()
for line in AustenC:
    AustenC = re.sub("\n", "", line)
    Aprob = AustenC.split(':')
    AustenDict[Aprob[0]] = AustenDict.get(Aprob[0], Aprob[1])

#Dickens Corpus data:
DickensDict = {}
DC = open("DickensC.txt")
DickensC = DC.readlines()
for line in DickensC:
    DickensC = re.sub("\n", "", line)
    Dprob = DickensC.split(':')
    DickensDict[Dprob[0]] = DickensDict.get(Dprob[0], Dprob[1])

#Counts of uni, bi, and trigrams necessary for probability calculations:
Counts = {}
CC = open("Counts.txt")
CountsC = CC.readlines()
for line in CountsC:
    CountsC = re.sub("\n", "", line)
    C = CountsC.split(':')
    Counts[C[0]] = Counts.get(C[0], int(C[1]))

#This part divides the input into lists of unigrams, bigrams, and trigrams:
sent = input("Enter a sentence: ")
#sent = "Sowmya is doing"
sent1 = re.sub('[,\.:;”\'!-\/\?_]',' ', sent)
Suni = sent1.split()
sentbi = []
for i in range(len(Suni)-1):
        S1 = Suni[i]
        S2 = Suni[i+1]
        Sbi = (S1, S2)
        sentbi.append(Sbi)
senttri = []
for i in range(len(Suni)-2):
        T1 = Suni[i]
        T2 = Suni[i+1]
        T3 = Suni[i+2]
        Stri = (T1, T2, T3)
        senttri.append(Stri)

#Here will be the probabilities for each unigram, trigram, and bigram from the input which will go into the final calculation:
unilistA = []
bigramA = []
trigramA = []
unilistD = []
bigramD = []
trigramD = []
probA = []

for item in Suni:
    if item in AustenDict:
        unilistA.append(AustenDict[item])
    else:
        sum = math.log(1/Counts["Austen unigram"])
        unilistA.append(sum)
for item in Suni:
    if item in DickensDict:
        unilistD.append(DickensDict[item])
    else:
        sum = math.log(1/Counts["Dickens unigram"])
        unilistD.append(sum)
for item in sentbi:
    if item in AustenDict:
        bigramA.append(AustenDict[item])
    else:
        sum = math.log(1/Counts["Austen bigram"])
        bigramA.append(sum)
for item in sentbi:
    if item in DickensDict:
        bigramD.append(DickensDict[item])
    else:
        sum = math.log(1/Counts["Dickens bigram"])
        bigramD.append(sum)
for item in senttri:
    if item in AustenDict:
        trigramA.append(AustenDict[item])
    else:
        sum = math.log(1/Counts["Austen trigram"])
        trigramA.append(sum)
for item in senttri:
    if item in DickensDict:
        trigramD.append(DickensDict[item])
    else:
        sum = math.log(1/Counts["Dickens trigram"])
        trigramD.append(sum)

#Added probabilities to go to the interpolation formula:
totaluniA = 0
totaluniD = 0
totalbiA = 0
totalbiD = 0
totaltriA = 0
totaltriD = 0

for item in unilistA:
    totaluniA = totaluniA + float(item)
for item in unilistD:
    totaluniD = totaluniD + float(item)
for item in bigramA:
    totalbiA = totalbiA + float(item)
for item in bigramD:
    totalbiD = totalbiD + float(item)
for item in trigramA:
    totaltriA = totaltriA + float(item)
for item in trigramD:
    totaltriD = totaltriD + float(item)

ProbA = L1 * totaluniA + L2 * totalbiA + L3 * totaltriA
ProbD = L1 * totaluniD + L2 * totalbiD + L3 * totaltriD

print("The probability for your sentence to show up in the Austen corpus is: ", ProbA)
print("The probability for your sentence to show up in the Dickens corpus is: ", ProbD)
