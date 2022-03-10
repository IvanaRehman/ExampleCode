import re
from string import punctuation
import pprint
import math
from bottle import route, run, template, request

"""
Builds a website designed to help users count word frequency of input text in Bosnian, 
Croatian, Montenegrin, or Serbian (BCMS), organized by the number of syllables. 
Users just need to enter the number of syllables they are looking for, and enter the text 
in the corresponding boxes. Then, when they click Count!, users will get a list of words 
with their frequency count.
"""

@route("/add", method="POST")
def getfrequencies():
    fullstring = request.forms.get("message")
    number = request.forms.get("number")
    smallLetters = fullstring.lower()
    string1 = re.sub('[,\.:;"\'!-\/]','', smallLetters)
    wordlist = string1.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    counted = dict(zip(wordlist, wordfreq))
    sortdict = dict([(key, counted[key]) for key in counted])
    sylldict = {}
    for word in wordlist:
        count = 0
        for x in word:
            if re.search('[aeiou]', x):
                count = count + 1
        sylldict[word] = count
    result = []
    for key, value in sylldict.items():
        if value == int(number):
            result.append(key + ' ' + str(sortdict[key]))
    if len(result)>1:
        return '<h3><center><font face="garamond" color="purple"><body bgcolor="#C8FFFF">Here are your words with ' + number + ' syllables, and their frequency counts: <br/>' +'<br/>'.join(result)+'.</center</h3>'
    else:
        return '<h3><center><font face="garamond" color="purple"><body bgcolor="#C8FFFF">Sorry, but your text does not contain any words with the number of syllables you asked for.</center</h3>'


@route('/')
@route('/enterinfo', method="get")
def login():
    return'''

<html>
<body bgcolor="#C8FFFF">
<head>
<title>BCMS Word/Syllable Counter</title>
</head>
<body>


<h1><b><center><font face="garamond" color="purple">Welcome! Dobrodošli! Добродошли!</center<b></h1>
<h2><b><center><font color="purple">This website is designed to help you count word frequency of your text in Bosnian, Croatian, Montenegrin, or Serbian (BCMS), organized by the number of syllables.
You just need to enter the number of syllables found in the words you are looking for, and enter the text in the corresponding boxes. Then, click Count!, and you will get a list of words with their frequency count.</center<b></h2>

<form action="/add" method="post">

        <p><center><b><i><font color="purple">Enter the number of syllables the words you are looking for have: </center</i></b></p>
        <p><center><textarea name="number" rows="2" cols="10"> </textarea></font></center</p>
        <p><center><b><i><font color="purple">Enter your text, and we'll show you the list of words!</center</i></b></p>
        <p><center><textarea name="message" rows="20" cols="100"> </textarea></font></center</p>
        <p><center><br><input type="submit" value="Count!"></center
        </form></p>

<h5><p>***Disclaimer: The word frequency counter will work for any language. However, the syllable counter will work only for BCMS languages. Also, for the convenience and the purpose of this project, the instructions are given in English.</p></h5>

</body>
</html>
'''


run() #this is the command to bottle
login()
getfrequencies(fullstring)