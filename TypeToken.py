from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

#Calculates Type/Token ratio in a given text

inp = input("Enter text: ")

inpLower = inp.lower()
inpNoPunc = re.sub('[,\.:;"\'!-\/]','', inpLower)
inpTokens = word_tokenize(inpNoPunc)
tokens = set(inpTokens)

Lemmas = []
lemmatizer = WordNetLemmatizer()

for token in inpTokens:
    Lemmas.append(lemmatizer.lemmatize(token))
    #print(lemmatizer.lemmatize(token))

types = set(Lemmas)

print(len(tokens))
print(len(types))
