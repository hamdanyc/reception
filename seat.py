import pandas as pd
import csv

# Function to assign guests to tables based on family_id
# Each table can accommodate 10 guests

def assign_guests_to_tables(csv_file):
    tables = []
    family_members = {}

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            family_id = int(row['family_id'])

            if family_id not in family_members:
                family_members[family_id] = []

            family_members[family_id].append(name)

    guests = []
    for family_id, members in family_members.items():
        guests.extend(members)

    tables = [guests[i:i+10] for i in range(0, len(guests), 10)]

    # Write seating assignments to guest_seat.csv
    with open('guest_seat.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'table_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for table_number, table in enumerate(tables, start=1):
            for guest in table:
                writer.writerow({'name': guest, 'table_number': table_number})

def main():     
    csv_file = 'guest_list.csv'
    assign_guests_to_tables(csv_file)
    
# Main function to run the assignment 
if __name__ == "__main__":
    main()  