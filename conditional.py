"""1. Write a program to find the greatest of four numbers entered by the user.

2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.

3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.

4. Write a program to find whether a given username contains less than 10
characters or not.

5. Write a program which finds out whether a given name is present in a list or not.

6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F

7. Write a program to find out whether a given post is talking about “Harry” or not"""

#1Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))
if a>b & a>c & a>d:
    print("a is the greatest of all")
elif b>a & b>c & b>d:
    print("b is the greatest of all")
elif c>a & c>b & c>d:
    print("c is the greatest of all")
else :
    print("d is the greatest of all")


#2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# Taking input for three subjects
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))


total_percentage = (sub1 + sub2 + sub3) / 3

if (total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("Result: Congratulations! You have PASSED.")
else:
    print("Result: Sorry, you have FAILED.")

#3A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
comment = input("Enter your comment: ")
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
is_spam = False

if ("make a lot of money" in comment.lower()):
    is_spam = True
elif ("buy now" in comment.lower()):
    is_spam = True
elif ("subscribe this" in comment.lower()):
    is_spam = True
elif ("click this" in comment.lower()):
    is_spam = True

if(is_spam):
    print("Warning: This comment is SPAM!")
else:
    print("This comment is safe.")

#4. Write a program to find whether a given username contains less than 10 characters or not.
username = input ("enter your name :")
if len(username) > 10:
    print("not a valid name")
else:
    print("valid name and proceed")

#5. Write a program which finds out whether a given name is present in a list or not.
names = ["omii","rishi","nitesh"]
name = input("enter your name: ")
if name in names:
    print("present")
else:
    print("not present")

"""6Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F"""
marks = int(input("enter your marks: "))
if marks>90 and marks<100 :
    print("Ex")
elif marks>80 and marks<90 :
    print("A")
elif marks>70 and marks<80 :
    print("B")
elif marks>60 and marks<70 :
    print("C")
elif marks>50 and marks<60 :
    print("D")
else:
    print("F")

#7. Write a program to find out whether a given post is talking about “omii” or not
post = input("enter your post: ")
if "omii".lower() in post.lower() :
    print("Talking about omii")
else:
    print("not talking about omii")
