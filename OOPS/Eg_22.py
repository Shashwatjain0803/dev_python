class Product:

    def setdetails(self,id,name):
        self.__id = id
        self.__name = name




    def getdetails(self):
        return self.__id , self.__name


p = Product()
p.setdetails(101,"samsung")
print(p.getdetails())