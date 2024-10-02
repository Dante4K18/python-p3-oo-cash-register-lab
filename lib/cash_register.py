class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.last_transaction_amount = 0.0

    def add_item(self, price: float, quantity: int = 1):
        """Add items to the total."""
        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    def apply_discount(self, discount: float):
        """Apply a discount to the total."""
        if discount > 0:
            discount_amount = (discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}"
        else:
            return "Discount must be greater than 0."

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0.0
