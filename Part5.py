class Addition:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return self.num + other.num


num1 = Addition(7)
num2 = Addition(5)
num3 = (num1 * num2)
print(num3)