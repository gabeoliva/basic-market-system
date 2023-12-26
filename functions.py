import os
from Product import Product


def clear_screen():
      os.system('cls')


def add_product(list): 
        code = int(input("Code:\n"))
        name = input("Name of product:\n")
        price = float(input("Price:\n"))
        prod = Product(code, name, price)
        list.append(prod) 