"""Chapter 5 – Practice Set
1.Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

2.Write a program to input eight numbers from the user and display all the unique numbers (once).

3.Can we have a set with 18 (int) and “18” (str) as a value in it?

4.What will be the length of following set S:

Python

s = Set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
S = {} What is the type of S?

5.Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

6.If the names of 2 friends are same; what will happen to the program in problem 6?

7.If languages of two friends are same; what will happen to the program in problem 6?

8.Can you change the values inside a list which is contained in set S? S = {8, 7, 12, "Harry", [1,2]}"""

#1.Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide user with an option to look it up!
words = {
    "chairs" = "kursi",
    "animal" = "janwar",
    "lion" = "sher"
}
word = input("enter the translation u wanna do : ")