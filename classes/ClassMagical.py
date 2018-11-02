class Magic():
    def __init__(self, i1, i2):
        self.i1 = i1
        self.i2 = i2

    def __add__(self, other):
        i1 = self.i1 + other.i1
        i2 = self.i2 + other.i2
        return Magic(i1, i2)

    def __sub__(self, other):
        i1 = self.i1 - other.i1
        i2 = self.i2 - other.i2
        return Magic(i1, i2)

    def __gt__(self, other):
        s1 = self.i1 + self.i2
        s2 = other.i1 + other.i2
        if s1 > s2:
            return True
        else:
            return False
    def __str__(self):
        return self.i1,self.i2


number = Magic(120, 15)
number2 = Magic(39, 33)
number3 = number + number2
number4 = number2 - number
print(number4.i1)
print(number4.__str__())

if number > number2:
    print("number is bigger")
else:
    print("number2 is bigger")
