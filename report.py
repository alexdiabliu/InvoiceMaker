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

        # Set font
        c.setFont("Helvetica-Bold", 16)

        # Add title
        c.drawCentredString(letter[0] / 2, letter[1] - 80, "Invoice")

        # Set font for labels
        c.setFont("Helvetica-Bold", 12)

        # Add period label/value
        c.drawRightString(letter[0] / 2 - 10, letter[1] - 120, "Period:")
        c.drawString(letter[0] / 2 + 10, letter[1] - 120, bill.date_supply)

        # Set font for table header
        c.setFont("Helvetica-Bold", 10)

        # Add task and price headers
        c.drawString(100, letter[1] - 160, "Task")
        c.drawString(300, letter[1] - 160, "Price")

        # Set font for table content
        c.setFont("Helvetica", 10)

        # Add task and price
        c.drawString(100, letter[1] - 180, str(tasks.name))
        c.drawString(300, letter[1] - 180, str(tasks.amount))

        # Save the PDF
        c.save()

        # Open the PDF in a web browser
        webbrowser.open(self.filename)
