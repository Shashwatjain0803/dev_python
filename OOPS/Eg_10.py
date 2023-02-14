# multi level inheritance

class grandparent:

    def d1(self):
        print("d1 method")

class parent(grandparent):

    def d2(self):
        print("d2 method")

class child(parent):

    def d3(self):
       print("d3 method")


c = child()
c.d1()
c.d2()
c.d3()