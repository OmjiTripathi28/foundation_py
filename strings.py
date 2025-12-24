"""
1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

2.Write a program to fill in a letter template given below with name and date.

Python

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
3.Write a program to detect double space in a string.

4.Replace the double space from problem 3 with single spaces.

5.Write a program to format the following letter using escape sequence characters. Letter = "Dear Harry, this python course is nice. Thanks!"""

#1.Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input ("Enter you name :")
print("Greetings," ,name)

#2.Write a program to fill in a letter template given below with name and date.
Name = input("Enter you name :")
Date = input("Enter date :")
print(f"""Dear {Name},
You are selected!
{Date}""")

#3.Write a program to detect double space in a string. 
statement = "This string contains  double spaces."
print(statement.find("  "))

#4.Replace the double space from problem 3 with single spaces.
print(statement.replace("  "," "))

#5.Write a program to format the following letter using escape sequence characters. Letter = "Dear Harry, this python course is nice. Thanks!
print("Dear omii, \nI'm fine.\nThanks!")