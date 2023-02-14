class Product:

    def __init__(self):
        print("special method")

    # def __new__(cls):
    #     print("magic method")


    def __del__(self):
        print(" del method")


Product()


