from math import factorial
#kilometers = input("enter kilometers")
#fact = int(input("Enter value:"))
def counter(fact):
    if fact == 0:
        return 1
    else:
        return fact * factorial (fact-1)

counter(0)
print(counter(7))