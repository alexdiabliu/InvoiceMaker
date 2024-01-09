

class Stakeholder:
    def __init__(self, name, email, phone, location):
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location

class Payer(Stakeholder):
    def __init__(self, name, email, phone, location, billing_info=None, purchase_history=None):
        super().__init__(name, email, phone, location)
        self.billing_info = billing_info
        self.purchase_history = purchase_history or []

class Payee(Stakeholder):
    def __init__(self, name, email, phone, location, business_info=None, services_offered=None, banking_details=None):
        super().__init__(name, email, phone, location)
        self.business_info = business_info
        self.services_offered = services_offered
        self.banking_details = banking_details or []
