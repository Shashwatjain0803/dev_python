# method Overriding

class RBI:

    def rateofinterest(self):
        return 0

class AXIS:

    def rateofinterest(self):
        return 5

class ICICI:

    def rateofinterest(self):
        return 10


a = AXIS()
print(a.rateofinterest())

i = ICICI()
print(i.rateofinterest())