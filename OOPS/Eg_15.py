class Product:

    pid = 101
    pName = "Samsung"

    def d1(self):
        print(self.pid, self.pName)

    @classmethod
    def d2(cls):
        print(cls.pid, cls.pName)

    @staticmethod
    def d3():
        print(Product.pid, Product.pName)

Product().d1()
Product.d2()
Product.d3()