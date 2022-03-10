from bs4 import BeautifulSoup
from urllib import request

"""
LanguageTool.org is a open-source proof reading program which does spelling and grammar check, 
in many languages. It is written in Java, but it has a HTTP interface, which can be accessed at: 
https://languagetool.org: 8081/?language=en-US&text=my+text+is+gut, where ”my+text+is+gut” 
in the url is the text you give to it. The program accesses this url, where ”my+text+is+gut” 
is replaced by the user given text, split into tokens, and without those quotes. Also, 
the program returns: a) number of errors identified by LanguageTool for this sentence 
the user gave, and b) error categories for each of the errors.
"""

def A5Q2():
    url = "https://languagetool.org:8081/?language=en-US&text="
    userinput = input("Please enter the text you want to check: ")
    splitit = userinput.split(" ")
    joinit = "+".join(splitit)
    finalerrors = []
    anotherlist = []
    content = request.urlopen(url+joinit).read().decode(encoding="UTF-8")
    soup = BeautifulSoup(content, "html.parser")
    errors = soup.find_all("error")
    number_of_errors = len(errors)
    if len(errors) >= 1:
        for index in range(0, number_of_errors):
            emptyerrors = errors[index].get("category")
            finalerrors.append(emptyerrors)
        whatever = ", ".join(finalerrors)
        anotherlist = [number_of_errors, whatever]
        return anotherlist
    else:
        return "Super awesome grammar!"

def main():
    try:
        newoutput = A5Q2()
        if isinstance(newoutput, list):
            print("Your sentence has ", newoutput[0], " error(s) according to LanguageTool.")
            print("They belong to the categories: ", newoutput[1])
        elif isinstance(newoutput, str):
            print(newoutput)
    except:
        print("What the hell did you do now, for reals?!")

if __name__ == "__main__":
    main()