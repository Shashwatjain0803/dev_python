# single level inheritance

class parent:

    def d1(self):
        print("d1 method")

class child(parent):
    def d2(self):
        print("d2 method")

c = child()
c.d1()
c.d2()