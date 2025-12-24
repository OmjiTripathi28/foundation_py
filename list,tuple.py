"""Chapter 4 – Practice Set
Write a program to store seven fruits in a list entered by the user.

Write a program to accept marks of 6 students and display them in a sorted manner.

Check that a tuple type cannot be changed in python.

Write a program to sum a list with 4 numbers.

Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)"""

#1Write a program to store seven fruits in a list entered by the user.
fruits = []

for i in range(0,7):
    fruit= input("enter the fruit you wanna add in the list:")
    fruits.append(fruit)
print(fruits)

#2Write a program to accept marks of 6 students and display them in a sorted manner.
Marks = []
for i in range (0,6):
    mark=int(input("enter marks: "))
    Marks.append(mark)
Marks.sort()
print(Marks)

#3Check that a tuple type cannot be changed in python.
"""nums = (1,2,3)
nums[0] = 10"""


#4Write a program to sum a list with 4 numbers.
nums = []
for i in range (0,4):
    num = int(input("enter a number :- "))
    nums.append(num)
print(sum(nums))

#5 Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))