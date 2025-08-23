import streamlit as st
import pandas as pd
import csv
from datetime import datetime

# Load data from CSV file
def load_data(csv_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({'name': row['name'], 'table#': row['table_number']})
    return pd.DataFrame(data)

# Get DataFrame for guest search
csv_file = 'guest_seat.csv'
data = load_data(csv_file)
df = pd.DataFrame(data)

st.title("Majlis Resepsi Dr Arif ❤️ Yana")

# Countdown to event
event_date = datetime(2025, 9, 27)
now = datetime.now()
delta = event_date - now

if delta.total_seconds() < 0:
    countdown_text = "Event has started!"
else:
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_text = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

st.subheader("WTC 27 Sep 2025")
st.subheader(f"Countdown: {countdown_text}")

# Select column to search
column = st.selectbox("Saring Mengikut", df.columns)

# Input search query
query = st.text_input("Carian")

# Filter DataFrame
if query:
    results = df[df[column].str.contains(query, case=False, na=False)]
else:
    results = df

st.dataframe(results)
