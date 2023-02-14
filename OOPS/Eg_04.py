

# class method
class product:

    pid = 101
    pname = "Mi"

    @classmethod
    def getproductdetails(cls):
        print(cls.pid, cls.pname)

product.getproductdetails()