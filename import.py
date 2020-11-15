import cs50
import csv
import sys
import cs50


# Connect to database
db = cs50.SQL("sqlite:///students.db")

# Check if command-line argument was passed
if len(sys.argv) != 2:
    print("Usage: python filename.py filename.csv")
    exit()

# Open provided CSV file
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # Get house of student
        house = row[1]

        # Get student's birth year
        birth_year = row[2]

        # Get student's names
        full_name = row[0].split(' ')

        # Do not include first row
        if len(full_name) == 1:
            continue

        # If middle name
        if len(full_name) == 3:
            first_name = full_name[0]
            middle_name = full_name[1]
            last_name = full_name[2]

            # Insert into database
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (:first, :middle, :last, :house, :birth)",
                       first=first_name, middle=middle_name, last=last_name, house=house, birth=birth_year)

        # If no middle name
        elif len(full_name) == 2:
            first_name = full_name[0]
            last_name = full_name[1]

            # Insert into database
            db.execute("INSERT INTO students (first, last, house, birth) VALUES (:first, :last, :house, :birth)",
                       first=first_name, last=last_name, house=house, birth=birth_year)