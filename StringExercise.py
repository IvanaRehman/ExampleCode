'''
Prompts the user to keep entering strings.
It stops when the user enters "done" and prints 
the lengths of the longest and shortest strings entered.
'''

minlength = 9999999999
maxlength = 0
try:
   while True:
     inputString = input("Enter a string: ")
     if inputString == "done":
         print("Minimum length of strings you entered so far: " + str(minlength))
         print("Maximum length of strings you entered so far: " + str(maxlength))
         break
     lenString  = len(inputString)
     if lenString < minlength:
         minlength = lenString
     if lenString >= maxlength:
         maxlength = lenString

except Exception as E:
    print("Something really unpredictable happened! Here is the description:")
    print(E)
