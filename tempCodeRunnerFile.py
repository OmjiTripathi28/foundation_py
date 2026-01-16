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