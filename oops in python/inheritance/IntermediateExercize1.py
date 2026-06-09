class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self):
        return self.price


class RegularProduct(Product):
    def get_final_price(self):
        return self.price


class DiscountedProduct(Product):
    def __init__(self, name, price, discount=0.10):
        super().__init__(name, price)
        self.discount = discount

    def get_final_price(self):
        return self.price - (self.price * self.discount)


class TaxExemptProduct(Product):
    def get_final_price(self):
        return self.price


class TaxedProduct(Product):
    def __init__(self, name, price, tax=0.18):
        super().__init__(name, price)
        self.tax = tax

    def get_final_price(self):
        return self.price + (self.price * self.tax)


items = [
    RegularProduct("Notebook", 100),
    DiscountedProduct("Shoes", 2000),
    TaxExemptProduct("Book", 500),
    TaxedProduct("Laptop", 50000)
]

for item in items:
    print(item.name, "Final Price:", item.get_final_price())