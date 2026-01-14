"""
1. Write a program to print multiplication table of a given number using for loop.
2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
3. Attempt problem 1 using while loop.
4. Write a program to find whether a given number is prime or not.
5. Write a program to find the sum of first n natural numbers using while loop.
6. Write a program to calculate the factorial of a given number using for loop.
7. Write a program to print the following star pattern.
 *
***
***** for n = 3
8. Write a program to print the following star pattern:
*
**
*** for n = 3
9. Write a program to print the following star pattern.
* * *
* * for n = 3
* * *
10. Write a program to print multiplication table of n using for loops in reversed
order.


#1. Write a program to print multiplication table of a given number using for loop.
n = int(input("enter a number :"))
for i in range(1,11):
    a = n*i
    print(f"{2}*{i}={a}")

#2Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
names = ["omii","sahil","sekhar sir"]
for name in names:
    if (name.startswith("s")):
        print(f"Greetings, {name}")

#3. Attempt problem 1 using while loop.
n = int(input("enter a number :"))
i = 0
a = 0
while (i<11):
    print(f"{2}*{i}={a}")
    i = i+1

#4. Write a program to find whether a given number is prime or not.
n = int(input("enter a number :"))
for i in range (2,n):
    if (n % i) == 0:
        print("not prime")
    break; 

#5.Write a program to find the sum of first n natural numbers using while loop.
n = int(input("enter a number :"))
sum = 0 
i = 1
while (i<n+1):
    sum= i + sum
    i+=1
print(sum)"""

#6. Write a program to calculate the factorial of a given number using for loop.
n = int(input("enter a number: "))
fact=1
for i in range (1,n+1):
    fact= fact*i
    i-=1
print(fact)
