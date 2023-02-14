from abc import ABC , abstractmethod


class Product(ABC):

    @abstractmethod
    def d1(self):
        pass

    @classmethod
    @abstractmethod
    def d2(cls):
        pass

    @staticmethod
    @abstractmethod
    def d3():
        pass


class productImpl(Product):

    def d1(self):
        print("d1 method")

    @classmethod
    def d2(cls):
        print("d2 method")

    @staticmethod
    def d3():
        print("d3 method")


p = productImpl()
p.d1()

productImpl.d2()
productImpl.d3()