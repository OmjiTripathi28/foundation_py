"""
1. Write a python program to add two numbers.

2. Write a python program to find remainder when a number is divided by z.

3. Check the type of variable assigned using input () function.

4. Use comparison operator to find out whether a given variable a is greater than 'b' or not. Take a = 34 and b = 80

5. Write a python program to find an average of two numbers entered by the user.

6. Write a python program to calculate the square of a number entered by the user."""

# 1. Write a python program to add two numbers.
a= 10 
b= 20
print("Sum of two numbers:", a + b)

# 2. Write a python program to find remainder when a number is divided by z.
num1 = 29
num2 = 5
remainder = num1 % num2
print("Remainder when", num1, "is divided by", num2, "is:", remainder)

# 3. Check the type of variable assigned using input () function.
user_input = input("Enter something: ")
print("The type of the variable assigned using input() function is:", type(user_input))

# 4. Use comparison operator to find out whether a given variable a is greater than 'b' or not. Take a = 34 and b = 80
numA = 34
numB = 80
is_greater= numA > numB
print("A is greater than B: ", is_greater)

#5. Write a python program to find an average of two numbers entered by the user.
num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))
avg = (num3+num4)/2
print("Average of numbers you entered is :",avg)

#6. Write a python program to calculate the square of a number entered by the user.
num5 = int(input("Enter a num :"))
sq = num5*num5
print("square of the number is : ",sq)