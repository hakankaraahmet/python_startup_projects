"""
************************************
Welcome to my Calculator!!!
Operations:
1- Summation
2-Subtraction
3-Multiplication
4-Division
5-Getting Square root of number
6-Factoriel
7-power

In order to quit please enter 'q'
************************************
"""
from math import sqrt,factorial,pow
while True:
  operations = input("Please select an operations: ")
  if operations == "1":
    first = float(input("Please enter number: "))
    second = float(input("Please enter number: "))
    print("Summation of {} and {} is {}".format(first,second,first+second))
  elif operations == "2":
    first = float(input("Please enter number: "))
    second = float(input("Please enter number: "))
    print("Substraction of {} and {} is {}".format(first,second,first-second))
  elif operations == "3":
    first = float(input("Please enter number: "))
    second = float(input("Please enter number: "))
    print("Multiplication of {} and {} is {}".format(first,second,first*second))
  elif operations == "4":
    first = float(input("Please enter number: "))
    second = float(input("Please enter number: "))
    print("Division of {} and {} is {}".format(first,second,first/second)) 
  elif operations == "5":
    first = float(input("Please enter number: "))
    print("Square root of {} is {}".format(first,sqrt(first)))  
  elif operations == "6":
    first = float(input("Please enter number: "))
    print("Factorial of {} is {}".format(first,factorial(first))) 
  elif operations == "7":
    first = float(input("Please enter number: "))
    second = float(input("Please enter number: "))
    print("{} over {} is {}".format(first,second,pow(first,second))) 
  elif operations == "q":
    print("Good Bye")
    break 
  else:
    print("Invalid Operations") 