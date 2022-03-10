import re

#a Python program that accepts a text file name from the user, builds a frequency listing 
#of the alphabetic characters contained in the file, and prints a sorted and nicely 
#formatted character frequency table to the screen.

def readTheFile(filepath):
    fullstring = open(filepath).read()
    return fullstring

def getfrequencies(fullstring):
    smallLetters = fullstring.lower()
    frequencies = dict()
    for x in smallLetters:
        if re.search('[a-z]', x):
            frequencies[x] = frequencies.get(x, 0) +1
    return frequencies

def main():
    filepath = input("Enter the path where your text file is: ")
    try:
        fullstring = readTheFile(filepath)
        frequencies = getfrequencies(fullstring)
        allLetters = frequencies.items()
        for key, value in (sorted(allLetters)):
            print("The character", key, "appeared", value, "times in this text.")
    except:
        return("File ", fullstring, "cannot be opened.")

if __name__ == "__main__":
    main()