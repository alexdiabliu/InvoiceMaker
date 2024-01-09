# Invoice Maker

Invoice Maker is a Python tool for generating PDF invoices with stakeholder details and task information.

## Features

- Create professional-looking invoices with stakeholder information.
- Add tasks, quantities, unit prices, and calculate the total price.
- Generates a PDF invoice for easy sharing and printing.

## Requirements

- Python3
- ReportLab library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/InvoiceMaker.git
    cd InvoiceMaker
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `main.py` file.

2. Customize the stakeholders' details and task information.

3. Run the script:

    ```bash
    python main.py
    ```
    
4. Answer the questions prompted by the program

5. The PDF invoice will be generated and opened in your default PDF viewer.

## Customization

- Modify the stakeholders' details and task information.
- Adjust the layout and appearance of the PDF by modifying the `PdfReport` class in `report.py`.

## Example

<img width="503" alt="image" src="https://github.com/alexdiabliu/InvoiceMaker/assets/88401570/cc43f8bf-a632-4ebf-8896-f39e6876f70d">

## Usage of Object-Oriented Principles

The use of classes and objects facilitates:

- **Code Reusability**: Stakeholder and task details can be reused for multiple invoices.
- **Maintainability**: Changes to the invoice structure can be easily accommodated without extensive modifications

## Code Structure

The codebase is organized into modular components:

- `main.py`: Entry point of the application where stakeholders and tasks are defined.
- `report.py`: Contains the `PdfReport` class responsible for generating the PDF invoice.
- `models.py`: Defines classes for stakeholders (`Payer` and `Payee`), tasks (`Task`), and bills (`Bill`).

## Future Enhancements

Future development may include:

- **User Interface**: Adding a graphical user interface (GUI) for a more user-friendly experience.
- **Database Integration**: Storing and retrieving invoice data from a database.

## Contributing

Contributions to enhance the tool or add new features are welcome
