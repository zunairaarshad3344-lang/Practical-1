class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative")

        self.products[name] = {
            "quantity": quantity,
            "price": price
        }

    def sell_product(self, name, quantity):
        if name not in self.products:
            raise KeyError("Product not found")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.products[name]["quantity"]:
            raise ValueError("Not enough stock")

        self.products[name]["quantity"] -= quantity

    def total_value(self):
        total = 0

        for product in self.products.values():
            total += product["quantity"] * product["price"]

        return total

    def display(self):
        for name, details in self.products.items():
            print(
                name,
                "Quantity:", details["quantity"],
                "Price:", details["price"]
            )


inventory = Inventory()

inventory.add_product("Pen", 10, 20)
inventory.add_product("Notebook", 5, 100)

inventory.sell_product("Pen", 2)

inventory.display()
print("Total inventory value:", inventory.total_value())