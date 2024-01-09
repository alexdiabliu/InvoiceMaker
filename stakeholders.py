
class Stakeholder:
    """
    Contains generic user data of all parties involved
    """
    def __init__(self, name, email, phone, location):
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location

class Payee(Stakeholder):
    """
    Inherits generic data from stakeholder and also holds payee-specific information
    """
    def oi(self):
        pass

class Payer(Stakeholder):
    """
     Inherits generic data from stakeholder and also holds payer-specific information
    """
    def iu(self):
        pass