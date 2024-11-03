class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.amount}, {self.date}, {self.category}, {self.description}"
