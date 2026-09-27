class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        print("\n========== FINAL BILL ==========")
        print("{:<20} {:<10} {:<10} {:<10}".format(
            "Product", "Price", "Quantity", "Total"
        ))

        subtotal = 0

        for product in self.products:
            total = product.total()
            subtotal += total

            print("{:<20} {:<10.2f} {:<10} {:<10.2f}".format(
                product.name,
                product.price,
                product.quantity,
                total
            ))

        tax = subtotal * 0.05
        final_total = subtotal + tax

        print("------------------------------------------")
        print("Subtotal:", subtotal)
        print("Tax (5%):", tax)
        print("Final Total:", final_total)
        print("==========================================")


# Create products
p1 = Product("Pen", 10, 2)
p2 = Product("Notebook", 50, 3)
p3 = Product("Bag", 500, 1)

# Create bill
bill = Bill()

bill.add_product(p1)
bill.add_product(p2)
bill.add_product(p3)

# Display final bill
bill.display_bill()