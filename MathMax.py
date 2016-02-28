#--# Python Calculator ENGLISH: By TheRealCodeGamer #--#
import sys


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#opties
print("Choose an option:")
print("---------------")
print("1. +")
print("2. -")
print("3. x")
print("4. :")
print("5. Stop")

choice = input("Choice (1/2/3/4/5): ")

if choice == '1':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1, " + ", num2, " = ", add(num1, num2))
    print("-----------------------")
elif choice == '2':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1, " - ", num2, " = ", subtract(num1, num2))
    print("-----------------------")
elif choice == '3':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1, " x ", num2, " = ", multiply(num1, num2))
    print("-----------------------")
elif choice == '4':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1, " : ", num2, " = ", divide(num1, num2))
    print("-----------------------")
elif choice == '5':
    sys.exit("Thank you for using the MathMax!")

else:
    print("Invalid Option.")
    print("-----------------------")