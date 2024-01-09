
class Tasks:
    """
    Contains data regarding invoice
    """
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.description = ""
        self.unit_price = unit_price
        self.amount = 0

    def set_description(self, description):
        self.description = description
        return
    
    def __set_amount(self):
        self.amount = self.quantity*self.unit_price
        return
    
class Bill:
    def __init__(self, tasks, date_supply, date_invoice):
        self.tasks = tasks
        self.date_supply = date_supply
        self.date_invoice = date_invoice
        self.invoice_number = 0
        self.subtotal = 0
        self.taxes = 0.00
        self.total = 0

    def set_invoice_number(self):
        with open("current_invoice_number.txt", "r") as invoice_num_file:
            self.invoice_number = int(invoice_num_file.read())

        with open("current_invoice_number.txt", "w") as invoice_num_file:
            invoice_num_file.write(str(self.invoice_number+1))
        return