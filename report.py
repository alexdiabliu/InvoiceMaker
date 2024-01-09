from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser


class PdfReport:
    """
    Generates the PDF Invoice file which contains all relevant data regarding stakeholders and bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, payer, payee, bill, tasks, invoice_number=0):
        # Create a PDF document
        c = canvas.Canvas(self.filename, pagesize=letter)

        # Set font
        c.setFont("Helvetica-Bold", 16)

        # Add title
        c.drawCentredString(letter[0] / 2, letter[1] - 80, "Invoice")

        # Add "Bill To" information
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, letter[1] - 120, "Bill To:")
        c.setFont("Helvetica", 8)
        c.drawString(50, letter[1] - 135, f"Name: {payer.name}")
        c.drawString(50, letter[1] - 150, f"Email: {payer.email}")
        c.drawString(50, letter[1] - 165, f"Phone: {payer.phone}")
        c.drawString(50, letter[1] - 180, f"Location: {payer.location}")

        # Add "Payee" information
        c.setFont("Helvetica-Bold", 12)
        c.drawString(300, letter[1] - 120, "Payee:")
        c.setFont("Helvetica", 8)
        c.drawString(300, letter[1] - 135, f"Name: {payee.name}")
        c.drawString(300, letter[1] - 150, f"Email: {payee.email}")
        c.drawString(300, letter[1] - 165, f"Phone: {payee.phone}")
        c.drawString(300, letter[1] - 180, f"Location: {payee.location}")

        # Add period label/value
        c.setFont("Helvetica-Bold", 10)
        c.drawRightString(letter[0] / 2 - 10, letter[1] - 200, "Period:")
        c.drawString(letter[0] / 2 + 10, letter[1] - 200, bill.date_supply)

        # Add date invoice label/value
        c.setFont("Helvetica-Bold", 10)
        c.drawRightString(letter[0] / 2 - 10, letter[1] - 220, "Invoice Date:")
        c.drawString(letter[0] / 2 + 10, letter[1] - 220, bill.date_invoice)

        # Add invoice number
        c.setFont("Helvetica-Bold", 10)
        c.drawRightString(letter[0] / 2 - 10, letter[1] - 240, "Invoice Number:")
        c.drawString(letter[0] / 2 + 10, letter[1] - 240, str(invoice_number))

        # Set font for table header
        c.setFont("Helvetica-Bold", 10)

        # Add task, quantity, unit price, and price headers
        task_header_width = 150
        c.drawString(100, letter[1] - 260, "Task")
        c.drawString(100 + task_header_width, letter[1] - 260, "Quantity")
        c.drawString(200 + task_header_width, letter[1] - 260, "Unit Price")
        c.drawString(300 + task_header_width, letter[1] - 260, "Price")

        # Set font for table content
        c.setFont("Helvetica", 10)

        # Add each task in the list
        y_position = letter[1] - 280
        for task in tasks:
            task_text_object = c.beginText(100, y_position)
            task_text_object.setFont("Helvetica", 10)
            task_text_object.setTextOrigin(100, y_position)
            task_text_object.textLines(str(task.name))
            c.drawText(task_text_object)

            c.drawString(100 + task_header_width, y_position, str(task.quantity))
            c.drawString(200 + task_header_width, y_position, f"${task.unit_price:.2f}")
            c.drawString(300 + task_header_width, y_position, f"${task.amount:.2f}")

            y_position -= 30  # Adjust the vertical position for the next task

        # Add total price
        c.setFont("Helvetica-Bold", 12)
        c.drawString(200, y_position - 30, "Total Price:")
        c.drawString(300 + task_header_width, y_position - 30, f"${bill.total_price:.2f}")

        # Save the PDF
        c.save()

        # Open the PDF in a web browser
        webbrowser.open(self.filename)
