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