
from bill import Bill, Tasks
from report import PdfReport
from stakeholders import Payee, Payer
import os


#user input section
payee_name = input("Please enter the Payee Name: ")
payee_email = input("Please enter the Payee Email: ")
payee_phone = input("Please enter the Payee Phone Number: ")
payee_location = input("Please enter the Payee Location: ")

payer_name = input("Please enter the Payer Name: ")
payer_email = input("Please enter the Payer Email: ")
payer_phone = input("Please enter the Payer Phone Number: ")
payer_location = input("Please enter the Payer Location: ")



#generates stakeholders
payee = Payee(name=payee_name, email=payee_email, phone=payee_phone, location=payee_location)
payer = Payer(name=payer_name, email=payer_email, phone=payer_phone, location=payer_location)



#creates bill
tasks = []
task_num = int(input("Please Enter Number of Tasks: "))

for i in range(task_num):
    task_name = input(f"Please Enter the Name of Task {i+1}: ")
    task_quantity = int(input(f"Please Enter the Quantity of Task {i+1}: "))
    task_unit_price = int(input(f"Please Enter the Unit Price of Task {i+1}: "))
    task = Tasks(name=task_name, quantity=task_quantity, unit_price=task_unit_price)
    task.set_amount()
    tasks.append(task)

supply = input("What is the Period of the Invoice? ")
current_date = input("What is the current date? ")

bill = Bill(tasks=tasks, date_supply=supply, date_invoice=current_date)
bill.set_invoice_number()
bill.set_total_price()


#creates pdf report
pdf_report = PdfReport(filename="Invoice.pdf")
pdf_report.generate(payer=payer, payee=payee, bill=bill, tasks=tasks)