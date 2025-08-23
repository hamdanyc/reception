import csv
from collections import defaultdict

def summarize_guests_by_table(input_file, output_file):
    table_counts = defaultdict(int)

    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_number = int(row['table_number'])
            table_counts[table_number] += 1

    # Sort tables by number
    sorted_tables = sorted(table_counts.items())

    # Generate markdown table
    markdown_table = "| Table Number | Number of Guests |\n"
    markdown_table += "|--------------|----------------|\n"
    for table_number, count in sorted_tables:
        markdown_table += f"| {table_number} | {count} |\n"

    with open(output_file, mode='w', encoding='utf-8') as mdfile:
        mdfile.write(markdown_table)

if __name__ == '__main__':
    summarize_guests_by_table('guest_seat.csv', 'table_summary.md')
