class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = sum(item['amount'] for item in self.ledger)
        return total

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc:<23}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total withdrawals and percentages
    total_spent = 0
    spent_by_cat = []
    for cat in categories:
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent_by_cat.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100 // 10 * 10) for spent in spent_by_cat]

    # Build chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for percent in percentages:
            line += " o " if percent >= i else "   "
        line += " "
        chart += line + "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line + "\n"

    return chart.rstrip("\n")  # Remove only final newline
