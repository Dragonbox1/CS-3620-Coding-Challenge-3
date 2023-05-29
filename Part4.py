class Computer:
    def __init__(self):
        self.specs = ""

    def getspecs(self):
        self.specs = input("Enter computer specs: ")

    def displayspecs(self):
        print(self.specs)


class Desktop(Computer):
    def __init__(self):
        self.monitor = ""

    def getmonitor(self):
        self.monitor = input("Enter monitor type: ")

    def displaymonitor(self):
        print(self.monitor)


class Laptop(Computer):
    def __init__(self):
        self.weight = 0

    def getweight(self):
        self.weight = input("Enter laptop weight: ")

    def displayweight(self):
        print(self.weight)


acerDesktop = Desktop()
acerDesktop.getspecs()
acerDesktop.getmonitor()
acerDesktop.displayspecs()
acerDesktop.displaymonitor()

lenovoLaptop = Laptop()
lenovoLaptop.getspecs()
lenovoLaptop.getweight()
lenovoLaptop.displayspecs()
lenovoLaptop.displayweight()