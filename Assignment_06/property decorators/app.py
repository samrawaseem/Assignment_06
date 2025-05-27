class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Usage
product = Product(100)
print(product.price)   # Access price using getter

product.price = 150    # Update price using setter
print(product.price)

del product.price      # Delete price using deleter