from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser

class PdfReport:
    """
    Generates the PDF Invoice file which contains all relevant data regarding stakeholders and bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, payer, payee, bill, tasks):
        # Create a PDF document
        c = canvas.Canvas(self.filename, pagesize=letter)

        # Set font for the page header
        c.setFont("Helvetica-Bold", 16)

        # Add "Invoice" title to the page header
        c.drawCentredString(letter[0] / 2, letter[1] - 30, "Invoice")

        # Calculate the center of the page for the row
        center_y = (letter[1] - 50 + letter[1] - 65 + letter[1] - 80) / 3

        # Add invoice number, date, and period on the centered row
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(letter[0] / 2 - 150, center_y, f"Invoice Number: {bill.invoice_number}")
        c.drawCentredString(letter[0] / 2, center_y, f"Invoice Date: {bill.date_invoice}")
        c.drawCentredString(letter[0] / 2 + 150, center_y, f"Period: {bill.date_supply}")

        # Add "Bill To" information with dark blue background
        c.setFillColorRGB(0, 0, 0.5)  # Dark Blue
        c.rect(50, letter[1] - 120, 250, 15, fill=True)
        c.setFillColorRGB(1, 1, 1)  # White font color
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, letter[1] - 120, "Bill To:")

        # Add "Payee" information with dark blue background
        c.setFillColorRGB(0, 0, 0.5)  # Dark Blue
        c.rect(300, letter[1] - 120, 250, 15, fill=True)
        c.setFillColorRGB(1, 1, 1)  # White font color
        c.setFont("Helvetica-Bold", 12)
        c.drawString(300, letter[1] - 120, "Payee:")

        # Set font for subfields
        c.setFillColorRGB(0, 0, 0)  # Reset color to black
        c.setFont("Helvetica", 8)
        c.drawString(50, letter[1] - 135, f"Name: {payer.name}")
        c.drawString(50, letter[1] - 150, f"Email: {payer.email}")
        c.drawString(50, letter[1] - 165, f"Phone: {payer.phone}")
        c.drawString(50, letter[1] - 180, f"Location: {payer.location}")

        c.drawString(300, letter[1] - 135, f"Name: {payee.name}")
        c.drawString(300, letter[1] - 150, f"Email: {payee.email}")
        c.drawString(300, letter[1] - 165, f"Phone: {payee.phone}")
        c.drawString(300, letter[1] - 180, f"Location: {payee.location}")

        # Set font for table header
        c.setFont("Helvetica-Bold", 10)

        # Adjust y_position for space above the headers
        y_position = letter[1] - 250  # Adjust the value as needed

        # Add task, quantity, unit price, and price headers
        task_header_width = 150
        c.drawString(100, y_position, "Task")
        c.drawString(100 + task_header_width, y_position, "Quantity")
        c.drawString(200 + task_header_width, y_position, "Unit Price")
        c.drawString(300 + task_header_width, y_position, "Price")

        # Set font for table content
        c.setFont("Helvetica", 10)

        # Add each task in the list
        y_position = letter[1] -270

        for task in tasks:
            task_text_object = c.beginText(100, y_position)
            task_text_object.setFont("Helvetica", 10)
            task_text_object.setTextOrigin(100, y_position)
            task_text_object.textLines(str(task.name))
            c.drawText(task_text_object)

            c.drawString(100 + task_header_width, y_position, str(task.quantity))
            c.drawString(200 + task_header_width, y_position, f"${task.unit_price:.2f}")
            c.drawString(300 + task_header_width, y_position, f"${task.amount:.2f}")

            y_position -= 18  # Adjust the vertical position for the next task

        # Add total price
        c.setFont("Helvetica-Bold", 12)
        c.drawString(300 + task_header_width, y_position - 30, f"Total Price: ${bill.total_price:.2f}")

        # Save the PDF
        c.save()

        # Open the PDF in a web browser
        webbrowser.open(self.filename)
