import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def read_guest_list(csv_file):
    guests = {}
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            table = row['table_number']
            name = row['name']
            seat = row['seat']
            if table not in guests:
                guests[table] = []
            guests[table].append((name, seat))
    return guests

def generate_pdf(guests, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    for table_number, entries in guests.items():
        # Table header
        header = Paragraph(f"Table {table_number}", styles['Heading2'])
        elements.append(header)
        elements.append(Spacer(1, 12))

        # Table data
        data = [["Name", "Seat"]]
        for name, seat in entries:
            # Wrap long names using Paragraph with a smaller font size
            name_paragraph = Paragraph(name, styles['Normal'])
            data.append([name_paragraph, seat])

        # Create and style the table
        table = Table(data, colWidths=(300, 50))  # Name column is wider to allow wrapping
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#cccccc'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),  # Uniform font size for all rows
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 1, '#dddddd'),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 24))

    doc.build(elements)

if __name__ == "__main__":
    guests = read_guest_list("guest_seat.csv")
    generate_pdf(guests, "guest_seat.pdf")
