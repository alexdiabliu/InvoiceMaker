
from bill import Bill, Tasks
from report import PdfReport
from stakeholders import Payee, Payer
import os


#instantiates basic information


#generates stakeholders
payee = Payee(name="Y", email="Y@gmail.com", phone="456", location="Y,A")
payer = Payer(name="X", email="X@gmail.com", phone="123", location="X,Z")

#creates bill
tasks = []
task_num = 2
for i in range(task_num):
    task = Tasks(name="Property Management", quantity=i+2, unit_price=200)
    task.set_amount()
    tasks.append(task)
bill = Bill(tasks=tasks, date_supply="Jan 09, 2024", date_invoice="Jan 08, 2024")
bill.set_invoice_number()
bill.set_total_price()

#creates pdf report
pdf_report = PdfReport(filename="Invoice.pdf")
pdf_report.generate(payer=payer, payee=payee, bill=bill, tasks=tasks)