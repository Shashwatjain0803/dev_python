from  abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def d1(self):
        pass

Product().d1() #TypeError: Can't instantiate abstract class Product with abstract method d1