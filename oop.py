"""
1. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
2. Write a class “Calculator” capable of finding square, cube and square root of a
number.
3. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?
4. Add a static method in problem 2, to greet the user with hello.
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
6. Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.
"""

"""1. Create a class “Programmer” for storing information of few programmers
working at Microsoft."""
class programmer :
    company = "Microsoft"
    def __init__(self , name , salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("omii","2000000","401303")
print(p.name,p.salary,p.pin,p.company)


"""2. Write a class “Calculator” capable of finding square, cube and square root of a
number."""
class calculator: 
    def __init__(self, n):
        self.n = n
    def square(self):
        print(self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    def squareroot(self):
        print(self.n**1/2)
    
c = calculator(20)
c.square()
c.cube()
c.squareroot()

"""3. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?"""
class demo: 
    a = 5

b = demo()
b.a = 0 
print(b.a)
print(demo.a)

"""4. Add a static method in problem 2, to greet the user with hello."""
class calculator: 
    
    def __init__(self, n):
        self.n = n
    def square(self):
        print(self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    def squareroot(self):
        print(self.n**1/2)
    @staticmethod 
    def greet():
        print("Hello user")
    
c = calculator(20)
c.greet()
c.square()
c.cube()
c.squareroot()

