# favorites0.py
# Task: Print every student's favourite language using csv.reader
#
# Expected output (first few lines):
#   Python
#   C
#   Python
#   ...
#
# Hint: csv.reader returns each row as a LIST.
#       The language column is at index 1.
#       Don't forget to skip the header row with next()

import csv

# Open favorites.csv for reading
with open("favorites.csv", "r") as file:

    # Create a csv.reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Loop over the remaining rows and print the language column
    for row in reader:
        print(row[1])