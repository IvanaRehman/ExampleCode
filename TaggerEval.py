import pprint
from nltk.tag import hmm

"""
Checks accuracy of an example tagger.
"""

train_data1 = open("pos.train.txt")
train_data2 = train_data1.readlines()

wordtag = []

for line in train_data2:
    lines = line.split()
    wordtag.append(lines)
#print(wordtag)
sent = []
train_data = []
for item in wordtag:
    if len(item) != 0:
        sent.append(item)
    else:
        train_data.append(sent)
        sent = []

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

test_data1 = open("pos.test.txt")
test_data2 = test_data1.readlines()

test = []
for line in test_data2:
    lines = line.split()
    test.append(lines)
sent1 = []
test_data = []
for item in test:
    if len(item) != 0:
        sent1.append(item)
    else:
        test_data.append(sent1)
        sent1 = []

acc = 0
total = 0
for sentence in test_data:
    words = []
    tags = []
    for item in sentence:
        words.append(item[0])
        tags.append(item[1])
    total = total + len(words)
    My_Tagger = tagger.tag(words)

    for i in range(len(My_Tagger)):
        if My_Tagger[i][1] == tags[i]:
            acc = acc + 1
eval = acc/total
print("The accuracy of this tagger is: ", eval)
