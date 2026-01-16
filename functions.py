"""
1. Write a program using functions to find greatest of three numbers.
2. Write a python program using function to convert Celsius to Fahrenheit.
3. How do you prevent a python print() function to print a new line at the end.
4. Write a recursive function to calculate the sum of first n natural numbers.
5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
6. Write a python function which converts inches to cms.
7. Write a python function to remove a given word from a list ad strip it at the same
time.
8. Write a python function to print multiplication table of a given number.
"""
#1Write a program using functions to find greatest of three numbers.
def max(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greatest")
    if a<b and b>c:
        print(f"{b} is the greatest")
    if c>b and a<c:
        print(f"{c} is the greatest")

    
a = int(input("enter a num: "))
b = int(input("enter a num: "))
c = int(input("enter a num: "))
print(max(a,b,c))

#2. Write a python program using function to convert Celsius to Fahrenheit.
def converter(celsius):
    fahrenheit = ((celsius) * (9/5))+32
    return fahrenheit
print(converter(25.5))

#4. Write a recursive function to calculate the sum of first n natural numbers.
def add(n):
    if(n==1):
        return 1
    return (add(n-1)+n)
print(add(3))

"""5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*"""

def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()

print(pattern(5))

#6. Write a python function which converts inches to cms.
def convert(inches):
    cm = inches*2.54
    return(cm.round())

print(convert(0.393701))

#7.Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(list_data, word_to_remove):
    new_list = [item.strip() for item in list_data if item != word_to_remove]
    return new_list
my_words = [" apple ", "letter", "  name  "]
print(remove_and_strip(my_words, "letter"))

#8. Write a python function to print multiplication table of a given number.
def table_for(n):
    for i in range(1, 11):
        print(n * i)

table_for(2)