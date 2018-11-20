Listpython = [2, 45, "Ramesh", 56, "Ramesh"]
Listnumbers = ["guru", "sakhi", "pen", "raj", "Rani", "Roja"]
Listnumber = ["guru", "sakhi", "pen", "raj", "rani", "roja"]

"""print (len(Listpython))
Listpython.append('3')
Listpython.insert(2,8)
print("Listn is " + str(Listpython))
print(Listpython[3:])
print("Ramesh" in Listpython)

for i in (Listpython):

    print (i)"""
print(Listnumbers)
Listnumbers.extend(Listpython)
print(Listnumbers)
Listnumbers.pop(1)
print(Listnumbers)
print(Listnumbers.index("Ramesh"))
print(Listnumbers.count("Ramesh"))
Listnumber.sort()
Listnumber.reverse()
print(Listnumber)
if "Ramesh" in Listnumbers:
    print("yes")
print(Listpython[:])