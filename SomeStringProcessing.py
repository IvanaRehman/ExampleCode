import re
import math


#Python program that takes as input a string and outputs the following things.
#1. Print the number of occurences of letter ”a” or ”A” in the string
#2. Print all the even alphabets from the string, seperated by a space (even alphabets - 2nd, 4th, 6th.. etc letters of the string if you start counting from 1)
#3. Print first alphabet and every third alphabet from there, seperated by space
#4. Print the string in reverse. (use: len(string) to get the length of the string).
#5. Print a ”Yes” if the string has a digit in it.


def countLetters(string):
    count1 = 0
    count2 = 0
    for x in string:
        if x == 'a':
            count1 = count1 + 1
    for y in string:
        if y == 'A':
            count2 = count2 + 1
    count = count1 + count2
    return "Number of occurrences of A or a in the string: ", str(count)

def evencharacters(string):
    b = ""
    for i in range(len(string)):
        if (i%2)!= 0:
            b+=string[i]
        a = " ".join(b)
    return "Only even alphabets in the string are: ", a

def everyThird(string):
    newword = string[::3]
    a = " ".join(newword)
    return "First alphabet and every third alphabet from there: ", a

def reverse(string):
    list = []
    length = len(string)
    for i in range(length-1, -1, -1):
        list.append(string[i])
    newstring = "".join(list)
    return "Reversed string: ", newstring


def findDigits(string):
    for line in string:
        z = re.findall('\d', string)
        if len(z) > 0:
            return "Does a string have a digit in it? Yes."
            break
        elif len(z) == 0:
            return "Does a string have a digit in it? No."
            break

def main():
    string = input("Please enter a phrase: ")
    print(" ".join(countLetters(string)))
    print(" ".join(evencharacters(string)))
    print(" ".join(everyThird(string)))
    print(" ".join(reverse(string)))
    print(findDigits(string))
if __name__ == "__main__":
    main()