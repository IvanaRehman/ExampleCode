'''
python code using beautiful soup, which takes a url from stackoverflow.com as input, and returns the following information as output:
1. title of the post
2. Number of votes the question received
3. Number of stars the question received
4. Number of answers that question received
5. Number of votes the top most displayed answer got.
'''

from urllib import request
from bs4 import BeautifulSoup
import pprint #Stands for pretty print
from urllib.request import Request, urlopen

def getHeadings(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode(encoding="UTF-8")
    soup = BeautifulSoup(html,"html.parser")
    result = []
    tags = soup('title')
    for tag in tags:
        result.append(tag.text)
    return result[0]

def voteNumber(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode(encoding="UTF-8")
    soup = BeautifulSoup(html,"html.parser")
    votes = []
    tags = soup('span')
    for tag in tags:
        if tag.has_attr("class"): #checks if the span tag has a class attribute
            span_class = tag.get("class")[0]
            if span_class == "vote-count-post":
                votes.append(tag.text)
    return votes[0]

def starNumber(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode(encoding="UTF-8")
    soup = BeautifulSoup(html,"html.parser")
    stars = []
    tags = soup('div')
    for tag in tags:
        if tag.has_attr("class"): #checks if the span tag has a class attribute
            span_class = tag.get("class")[0]
            if span_class == "favoritecount":
                stars.append(tag.text)
    return stars[0]

def answerNumber(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode(encoding="UTF-8")
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('span')
    for tag in tags:
        answers = soup(itemprop="answerCount")[0].get_text()
        return answers

def topAnswerNumber(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode(encoding="UTF-8")
    soup = BeautifulSoup(html,"html.parser")
    topvotes = []
    tags = soup('span')
    for tag in tags:
        if tag.has_attr("class"): #checks if the span tag has a class attribute
            span_class = tag.get("class")[0]
            if span_class == "vote-count-post":
                topvotes.append(tag.text)
    return topvotes[1]

def main():
    try:
        url = input("Enter a URL about some topic. ")
        if "stackoverflow.com/questions" in url:
            print("The title of this thread is: ", getHeadings(url))
            print("The number of votes the question recieved is: ", voteNumber(url))
            print("The number of stars the question received is: ", starNumber(url))
            print("The number of answers the question received is: ", answerNumber(url))
            print("The number of votes the top most answer got is: ", topAnswerNumber(url))
        else:
            print("You can only check StackOverflow discussion pages! Be a good user, you :)")
    except:
        print("Something is wrong with your URL!")

if __name__ == "__main__":
    main()