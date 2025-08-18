import csv
import sys
import requests
from io import StringIO

# Published CSV URL format: https://docs.google.com/spreadsheets/d/e/SPREADSHEET_ID/pub?output=csv
# To generate this URL:
# 1. Open the Google Sheet
# 2. Click "File" > "Publish to the web"
# 3. Select "CSV" format and click "Publish"
# 4. Copy the generated URL

GOOGLE_SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vStwrKnn87_h10mGigKhkuomud58mUJuMlYwPB_KzkvKnacNv0K2JeYvGTZANZNDYnQIRuuh20VOjGh/pub?output=csv"

def main():
    output_file = "guest_seat.csv"

    # Fetch CSV from Google Sheets
    response = requests.get(GOOGLE_SHEETS_URL)
    if response.status_code != 200:
        print(f"Failed to fetch CSV from Google Sheets. Status code: {response.status_code}")
        sys.exit(1)

    # Convert response content to file-like object
    csv_data = StringIO(response.text)

    table_number = 1
    seat_number = 1
    table_guest_count = 0

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['name', 'seat', 'table_number'])
        writer.writeheader()

        reader = csv.DictReader(csv_data)
        for row in reader:
            guest_name = row['Nama']
            phone = row['Telefon']
            value = row['Jumlah Kehadiran'].strip()
            number_guest = int(value) if value else 1

            # Assign guest to table
            if table_guest_count + number_guest <= 10:
                # Add to current table
                for i in range(1, number_guest + 1):
                    if i == 1:
                        writer.writerow({
                            'name': f"{guest_name.title()} (0{phone})",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    else:
                        writer.writerow({
                            'name': f"Ahli Keluarga #{i} {guest_name.title()}",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    seat_number += 1
                table_guest_count += number_guest

            elif table_guest_count < 10:
                # Fill remaining seats with Simpanan and start new table
                remaining = 10 - table_guest_count
                for i in range(1, remaining + 1):
                    writer.writerow({
                        'name': f"Simpanan #{table_number}:{seat_number}",
                        'seat': str(seat_number),
                        'table_number': str(table_number)
                    })
                    seat_number += 1
                table_guest_count = 0
                table_number += 1

                # Process current guest in new table
                for i in range(1, number_guest + 1):
                    if i == 1:
                        writer.writerow({
                            'name': f"{guest_name.title()} (0{phone})",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    else:
                        writer.writerow({
                            'name': f"Ahli Keluarga #{i} {guest_name.title()}",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    seat_number += 1
                table_guest_count = number_guest

            else:
                # Start new table
                table_number += 1
                table_guest_count = number_guest
                for i in range(1, number_guest + 1):
                    if i == 1:
                        writer.writerow({
                            'name': f"{guest_name.title()} ({phone})",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    else:
                        writer.writerow({
                            'name': f"Ahli Keluarga #{i} {guest_name.title()}",
                            'seat': str(seat_number),
                            'table_number': str(table_number)
                        })
                    seat_number += 1

        # Print total tables
        print(f"Total tables: {table_number}")

if __name__ == "__main__":
    main()
