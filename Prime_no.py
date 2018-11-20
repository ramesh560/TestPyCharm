'''num = int(input("Enter value :"))

if num > 0:
    for i in range(2, num - 1):
        if (num % i == 0):
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is proper number ")'''

lower = int(input("Enter lower number: "))
higher = int(input("Enter higher number: "))

for i in range(lower, higher):
    for j in range(2, i ):
        if (i % j == 0):
           # print(i, "is not a prime number")
            #print(i, "times", i // i, "is", i)
            break
    else:
        print(i, "is a prime number")
