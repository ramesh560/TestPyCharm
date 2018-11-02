from math import factorial

var = int(input("enter value : "))
if var< 0 :
    print("nofactorial for negative numbers")
elif var==0:
    print("factorial is 1")
else:
    sam = var * factorial(var-1)
    print("print factorial is "+str(sam))