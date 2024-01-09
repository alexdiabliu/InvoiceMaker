
from bill import Bill, Tasks
from report import PdfReport
from stakeholders import Payee, Payer
import os



# one = Bill("fwwe", "wew", "WEf")
# one.set_invoice_number()

#instantiates basic information


#generates stakeholders
payee = Payee(name="Alex", email="alexdiabliu@gmail.com", phone="6474083375", location="Hamilton, Ontario, Canada")
payer = Payer(name="Leila", email="leila.diabliu77@gmail.com", phone="1234567890", location="Hamilton, Ontario, Canada")

#creates bill
tasks = Tasks(name="Property Management", quantity=1, unit_price=200)
bill = Bill(tasks=tasks, date_supply="Jan 09, 2024", date_invoice="Jan 08, 2024")

#creates pdf report
pdf_report = PdfReport(filename="Invoice.pdf")
pdf_report.generate(payer=payer, payee=payee, bill=bill, tasks=tasks)