from BubbleSort import bubble_sort
import re

#Binary search algorithm (no built-ins) that imports a function from file titled BubbleSort

def binarySearch(list1, item):
    first = 0
    last = len(list1) - 1
    there = False
    while first <= last:
        mid = int((first + last)/2)
        if list1[mid+1] == item:
            there = True
            return mid+1
        else:
            if item < list1[mid]:
                last = mid
            else:
                first = mid
            if last == first or last - first == 1:
                if list1[last] == mid or list1[first] == mid:
                    return mid-1
                else:
                    return "Your item is not in the list"

def main():
    try:
        list0 = input("Enter a list of numbers: ")
        if re.search('[^\d,]', list0):
            print("Please, enter a list of numbers only!")
        elif ',' not in list0:
            print("Please, separate your numbers by commas only, or enter more numbers!")
        else:
            newone = (bubble_sort(list0))
            print("Your list is now sorted: ", newone)
            item = int(input("Enter the specific number you are looking for: "))
            print("The index of this item in the list is: ", (binarySearch(newone, item)))
    except:
        print("Please, enter a list of numbers separated by commas only!")

if __name__ == "__main__":
    main()