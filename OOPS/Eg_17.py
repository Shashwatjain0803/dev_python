from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def d1(self):
        pass

    @abstractmethod
    def d2(self):
        pass

class ProductImpl(Product):

    def d1(self):
            print("d1 method")

    def d2(self):
            print("d2 method")

ProductImpl().d1()
ProductImpl().d2()

