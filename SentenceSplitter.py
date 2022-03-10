import re

#sentence splitter

#This program, given the name of a text file, is able to write its content with each sentence on a separate line.

inp = input("Enter a text: ")
sentences = re.split(' *(?<![A-Z][a-z])(?<![A-Z][a-z][a-z])(?<![a-z]\.[a-z])([\.\?!][\'"\)\]]*) ', inp)
for i in range(len(sentences)-1):
    if i%2 == 0:
        print(sentences[i] + sentences[i+1])
print(sentences[-1])