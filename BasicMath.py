import math

#Python program that takes as input a whole number (say X), and does the following:
#1. Check whether X is a prime number.
#2. Sum of all numbers up to X
#3. Print the square of the number (X*X)
#4. Print the cube of a number (X*X*X)
#5. Print the sum of all digits in the number


def prime(n):
     if n > 1:
        y = 1
        for i in range(2, n):
            if (n % i) == 0:
                y = 0
                break
            else:
                y = 1
        if y == 0:
            return str(n) + " is not a prime number."
        elif y == 1:
            return str(n) + " is a prime number."

def summing(n):
    upto = range(0, n+1)
    uptoSum = sum(upto)
    return "The sum of all numbers up to " + str(n) + " is " + str(uptoSum)

def square(n):
    z = n*n
    return "The square of ", str(n), " is: ", str(z)

def cube(n):
    c = n*n*n
    return "The cube of " + str(n) + " is: " + str(c)

def digitSum(n):
    num = str(n)
    newnum = []
    for digit in num:
        newnum.append(int(digit))
    return "Sum of all digits in ",  str(n), " is ", str(sum(newnum))

def main():
    try:
        n = int(input("Enter a number: "))
        if isinstance(n, float) or isinstance(n, str):
            print("Please enter a whole number. That is, a positive number without decimals.")
        elif n < 1:
            print("Please enter a whole number. That is, a positive number without decimals.")
        else:
            print(prime(n))
            print(summing(n))
            print(" ".join(square(n)))
            print(cube(n))
            print(" ".join(digitSum(n)))
    except:
        print("Please enter a whole number. That is, a positive number without decimals.")
if __name__ == "__main__":
    main()