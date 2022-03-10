import re
import pprint
import math

"Some frequency and probability counts"


t1 = open("Austen.txt")
Austen = t1.read()
t2 = open("Dickens.txt")
Dickens = t2.read()

#frequency counts of Unigrams for the first corpus
Austennopunct = re.sub('[,\.:;”\'!-\/\?_]',' ', Austen)
Austenlist = Austennopunct.split()
freqAusten = {}
totalAusten = len(Austenlist)
for item in Austenlist:
        freqAusten[item] = freqAusten.get(item, 0) + 1

#frequency counts of Unigrams for the second corpus
Dickensnopunct = re.sub('[,\.:;”\'!-\/\?_]',' ', Dickens)
Dickenslist = Dickensnopunct.split()
freqDickens = {}
totalDickens = len(Dickenslist)
for item in Dickenslist:
        freqDickens[item] = freqAusten.get(item, 0) + 1

#frequency counts of Bigrams for the first corpus
bigramA = []
bigramAfreq = dict()
for i in range(totalAusten-1):
        firstA = Austenlist[i]
        secondA = Austenlist[i+1]
        keyA = (firstA, secondA)
        bigramA.append(keyA)
for i in bigramA:
        bigramAfreq[i] = bigramAfreq.get(i, 0) + 1

#frequency counts of Bigrams for the second corpus
bigramD = []
bigramDfreq = dict()
for i in range(totalDickens-1):
        firstD = Dickenslist[i]
        secondD = Dickenslist[i+1]
        keyD = (firstD, secondD)
        bigramD.append(keyD)
for i in bigramD:
        bigramDfreq[i] = bigramDfreq.get(i, 0) + 1

#frequency counts of Trigrams for the first corpus
trigramA = []
trigramAfreq = dict()
for i in range(totalAusten-2):
        A1 = Austenlist[i]
        A2 = Austenlist[i+1]
        A3 = Austenlist[i+2]
        trikeyA = (A1, A2, A3)
        trigramA.append(trikeyA)
for i in trigramA:
        trigramAfreq[i] = trigramAfreq.get(i, 0) + 1

#frequency counts of Trigrams for the second corpus
trigramD = []
trigramDfreq = dict()
for i in range(totalDickens-2):
        D1 = Dickenslist[i]
        D2 = Dickenslist[i+1]
        D3 = Dickenslist[i+2]
        trikeyD = (D1, D2, D3)
        trigramD.append(trikeyD)
for i in trigramD:
        trigramDfreq[i] = trigramDfreq.get(i, 0) + 1

uniprobA = dict()
for key, value in freqAusten.items():
        uniprob1 = math.log((value+1)/(totalAusten+len(freqAusten))) #Unigram probability calculation with smoothing
        uniprobA[key] = uniprobA.get(key, uniprob1)

uniprobD = dict()
for key, value in freqDickens.items():
        uniprob2 = math.log((value+1)/(totalDickens+len(freqDickens))) #Unigram probability calculation with smoothing
        uniprobD[key] = uniprobD.get(key, uniprob2)

biprobA = dict()
for key, value in bigramAfreq.items():
        biprob1 = math.log((value+1)/(freqAusten[key[0]]+len(bigramAfreq))) #Bigram probability calculation with smoothing
        biprobA[key] = biprobA.get(key, biprob1)

biprobA = dict()
for key, value in bigramAfreq.items():
        biprob1 = math.log((value+1)/(freqAusten[key[0]]+len(bigramAfreq))) #Bigram probability calculation with smoothing
        biprobA[key] = biprobA.get(key, biprob1)

biprobD = dict()
for key, value in bigramDfreq.items():
        biprob2 = math.log((value+1)/(freqDickens[key[0]]+len(bigramDfreq))) #Bigram probability calculation with smoothing
        biprobD[key] = biprobD.get(key, biprob2)

triprobA = dict()
for key, value in trigramAfreq.items():
        triprob1 = math.log((value+1)/(bigramAfreq[(key[0], key[1])]+len(trigramAfreq))) #Trigram probability calculation with smoothing
        triprobA[key] = triprobA.get(key, triprob1)

triprobD = dict()
for key, value in trigramDfreq.items():
        triprob2 = math.log((value+1)/(bigramDfreq[(key[0], key[1])]+len(trigramDfreq))) #Trigram probability calculation with smoothing
        triprobD[key] = triprobD.get(key, triprob2)

AustenC= "AustenC.txt"
DickensC = "DickensC.txt"
Counts = "Counts.txt"

#writing everything into text files in order to use in the second program required for Q1
writer = open(AustenC, "w")
line = ""
for key, value in uniprobA.items():
        line += str(key) + ": " + str(value) + "\n"
for key, value in biprobA.items():
        line += str(key) + ": " + str(value) + "\n"
for key, value in triprobA.items():
        line += str(key) + ": " + str(value) + "\n"
writer.write(line)
writer.close()

writer = open(DickensC, "w")
line1 = ""
for key, value in uniprobD.items():
        line1 += str(key) + ": " + str(value) + "\n"
for key, value in biprobD.items():
        line1 += str(key) + ": " + str(value) + "\n"
for key, value in triprobD.items():
        line1 += str(key) + ": " + str(value) + "\n"
writer.write(line1)
writer.close()


writer = open(Counts, "w")
line2 = ""

line2 += "Austen unigram: " + str(totalAusten) + "\n"
line2 += "Dickens unigram: " + str(totalDickens) + "\n"
line2 += "Austen bigram: " + str(len(bigramAfreq)) + "\n"
line2 += "Dickens bigram: " + str(len(bigramDfreq)) + "\n"
line2 += "Austen trigram: " + str(len(trigramAfreq)) + "\n"
line2 += "Dickens trigram: " + str(len(trigramDfreq)) + "\n"
writer.write(line2)
writer.close()
