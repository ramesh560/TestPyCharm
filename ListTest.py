from typing import List, Union

list_one: List[Union[int,str]] = [22,44,"Ramesh"]
list_two =["Hello"+" " +"Guru"+" " +"Preme"+" " +"Kosame"+" " +"Raa"+" " +"jevitham"]
print(len(list_one))
print(list_one[1])
list_one.insert(2,"mahesh")
list_one.append(4)
print(list_one)
print(len(list_one))

list_two = list_one + list_two
print (list_two)
print (list_two[len(list_one)])

for i in range(len(list_one)):
    var = 0
    i+=var
    print (list_one[i])

