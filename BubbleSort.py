import re

#a program that takes a list of numbers and produces a sorted list as output w/o built-ins.

def bubble_sort(list0):
    length = len(list0)-1
    sorted = False
    list1 = list0.split(',')
    for index in range(0, len(list1)):
        list1[index] = int(list1[index])
    while not sorted:
        sorted = True
        for item in range(0,len(list1)-1):
            if (list1[item]) > (list1[item +1]):
                sorted = False
                list1[item], list1[item+1] = list1[item+1], list1[item]
    return list1

def main():
    try:
        list0 = input("Enter a list of numbers: ")
        if re.search('[^\d,]', list0):
            print("Please, enter a list of numbers only!")
        elif ',' not in list0:
            print("Please, separate your numbers by commas only!")
        else:
            newone = bubble_sort(list0)
            print(newone)
    except:
        print("Please, enter a list of numbers separated by commas only!")

if __name__ == "__main__":
    main()
