__author__ = 'Anastasiya'

"""print("Hello World")

name =  input("What is your name?")
print("Hey" + name)

total = 0
number = int(input("Please enter a number"))
for i in range(number+1):
    total += i
print(total)

total = 0
number = int(input("Enter a number: "))
for i in range(number+1):
    if i%3==0 or i%5==0 or i%6==0 or i%9==0 or i%10 == 0 or i%12==0 or i%15==0 or i%17==0:
        total+=i

print("the sum is : " + str(total))"""
from time import time
total = 0
number = int(input("Enter a number: "))
choice = input("Do you want to compute a sum (enter sum) or a product (enter product)")
print(time())
for i in range(1, number+1):
    if choice == 'sum':
        total+=i
    elif choice == 'product':
        total = 1
        total*=i
    else:
        print("Incorrect choice")
print(total)
print(time())