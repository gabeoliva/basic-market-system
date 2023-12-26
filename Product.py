class Product:
    def __init__(self, code, name, price):
        self.code = code

        self.name = name

        self.price = price

    def __str__(self) -> str:
        return f"Code: {self.code}, Name: {self.name}, Price: ${self.price}"