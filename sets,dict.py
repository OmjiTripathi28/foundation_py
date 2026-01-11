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

8.Can you change the values inside a list which is contained in set S? S = {8, 7, 12, "omii", [1,2]}"""

#1.Write a program to create a dictionary of Hindi words with values as their English translation. 
words = {
    "madad"  : "help",
    "kurshi" : "chair",
    "kitaab" : "book"
}

word = input("enter the word you want the meaning of : ")
print(words[word])

#2 Write a program to input eight numbers from the user and display all the unique numbers (once).
nums = set()
for i in range (0,7):
    num = int(input("enter a number you want in a set: "))
    nums.add(num)

print(nums)

#3.Can we have a set with 18 (int) and “18” (str) as a value in it?
mix = set ()
mix.add(18)
mix.add("18")
print(mix)

#4.What will be the length of following set S:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s) #length is 2

#5.Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
fav_lang = {

}
for i in range (0,4):
    name = input("enter your name :")
    lang = input("enter your fav lang :")
    fav_lang.update({name : lang})

print(fav_lang)

#6.If the names of 2 friends are same; what will happen to the program in problem 6?
fav_lan = {

}
for i in range (0,4):
    name = input("enter your name :")
    lang = input("enter your fav lang :")
    fav_lan.update({name : lang})

print(fav_lan)

#7.If languages of two friends are same; what will happen to the program in problem 6?
fav_lang3 = {

}
for i in range (0,4):
    name = input("enter your name :")
    lang = input("enter your fav lang :")
    fav_lang3.update({name : lang})

print(fav_lang3)

#8.Can you change the values inside a list which is contained in set S? S = {8, 7, 12, "omii", [1,2]}
#no as the set don't have indexing method in it
