# Hierarchical Inheritance

class grandparent:

    def d1(self):
        print("d1 method")

class parent(grandparent):

    def d2(self):
        print("d2.method")

class child(grandparent):

    def d3(self):
        print("d3 method")

c = child()
c.d1()
c.d3()

p = parent()
p.d2()
p.d1()