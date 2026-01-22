"""
1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.

2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

3. Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.

4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.

5. Repeat program 4 for a list of such words to be censored.

6. Write a program to mine a log file and find out whether it contains ‘python’.

7. Write a program to find out the line number where python is present from ques 6.

8. Write a program to make a copy of a text file “this. txt”

9. Write a program to find out whether a file is identical & matches the content of
another file.

10. Write a program to wipe out the content of a file using python.

"""

"""
1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
"""
f = open("poems.txt")
lines = f.readline()
print(lines)
if("twinkle" in lines):
    print("Yes twinkle is present in the file")
else:
    print("no it's not present in the file")
f.close()

"""2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score."""
import random
def game():
    print("You are playing the game...")
    score = random.randint(1,100)
    f = open("hiscore.txt")
    hiscore = f.read()
    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0
    
    print(f"Your score is {score}")
    if score>hiscore:
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))
    
    return score

game()

"""
3. Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
"""
def generate_table(n):
    table = ""
    for i in range(1,11):
        table+= (f"{n} * {i} = {n*i}")

    with open(f"tables/table_{n}" , "w") as f :
        f.write(str(table))
        print("TABLES PRINTED SUCCESSFULLY !")

for i in range (2,21):
    generate_table(i)

"""4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file."""
word = "donkey" 
with open("donkey.txt" , "r") as f :
    content = f.read()

new = content.replace(word,"######")

with open("donkey.txt","w") as f :
    f.write(new)


"""5. Repeat program 4 for a list of such words to be censored."""
words = ["donkey" , "affectionately"]

with open("donkey copy.txt" , "r") as f :
    content2 = f.read()

for word in words:
    new2 = content.replace(word , "#####")
    with open("donkey copy.txt" , "w") as f :
        f.write(new2)

"""6. Write a program to mine a log file and find out whether it contains ‘python’."""
with open("python.txt") as f :
    content3 = f.read()
if ("python" in content3):
    print("YES python is in the file")
else:
    print("No")

"""7. Write a program to find out the line number where python is present from ques 6."""
with open("python.txt") as f :
    lines = f.readlines()

lineno = 1 
for line in lines:
    if "python" in line:
        print(f"yes it is present it is on line : {lineno}")
        lineno+=1
        break
    else:
        print("no python is not present")




"""8. Write a program to make a copy of a text file “this. txt”"""
with open("this.txt") as f:
    content = f.read()

with open("text_copy.txt", "w") as f:
    f.write(content)

"""9. Write a program to find out whether a file is identical & matches the content of
another file."""
with open("this.txt") as f:
    content = f.read()

with open("text_copy.txt") as f:
    content2 = f.read()
if content == content2:
    print("yes the content matches")
else:
    print("no match")

"""10. Write a program to wipe out the content of a file using python."""
with open("this.txt") as f:
    content = f.read()

with open("this.txt", "w") as f:
    f.write("")  

