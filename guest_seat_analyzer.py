import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV file
df = pd.read_csv('guest_seat.csv')

# Initialize summary dictionary
summary = {}

# Process each table
for table_num, group in df.groupby('table_number'):
    total_guests = len(group)
    simpanan_count = group['name'].str.contains('simpanan', case=False).sum()
    
    summary[table_num] = {
        'total_guests': total_guests,
        'simpanan_count': simpanan_count
    }

# Convert to DataFrame
summary_df = pd.DataFrame.from_dict(summary, orient='index').reset_index()
summary_df.columns = ['Table Number', 'Total Guests', 'Reserved']

# Add adjusted total column (total guests minus simpanan count)
summary_df['Adjusted Total'] = summary_df['Total Guests'] - summary_df['Reserved']

# Add total row
total_row = {
    'Table Number': 'Total',
    'Total Guests': summary_df['Total Guests'].sum(),
    'Reserved': summary_df['Reserved'].sum(),
    'Adjusted Total': summary_df['Adjusted Total'].sum()
}
summary_df = pd.concat([summary_df, pd.DataFrame([total_row])], ignore_index=True)

# Create PDF document
pdf = SimpleDocTemplate("table_summary.pdf", pagesize=letter)
elements = []

# Add title
styles = getSampleStyleSheet()
title_style = styles['Heading1']
title = Paragraph("Tables Summary", title_style)
elements.append(title)
elements.append(Spacer(1, 24))

# Convert DataFrame to list of lists for table
data = [summary_df.columns.tolist()] + summary_df.values.tolist()

# Create table and apply styling
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), '#cccccc'),
    ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), '#ffffff'),
    ('GRID', (0, 0), (-1, -1), 1, '#000000'),
]))

elements.append(table)

# Build PDF
pdf.build(elements)

print("Analysis complete. Results written to table_summary.pdf")
