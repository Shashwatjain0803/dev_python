# static method


class product:

    pid = 101
    pname = "nokia"

    @staticmethod
    def getproductdeails():
        print(product.pid , product.pname)

product.getproductdeails()