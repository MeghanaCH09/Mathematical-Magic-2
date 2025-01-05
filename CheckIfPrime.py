from math import sqrt

num=int(input("Enter a number to check whether it is a prime number of not: "))

if num>1:
    for i in range(2,int(sqrt(num))+1):
        if (num%i==0):
            print(f"{num} is not a prime number")
            break
        else: 
            print(f"{num} is a prime number")
else: 
    print(f"{num} is not a prime number...")