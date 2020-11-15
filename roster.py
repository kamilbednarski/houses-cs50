import cs50
import csv
import sys
import cs50


# Connect to database
db = cs50.SQL("sqlite:///students.db")

# Check if command-line argument was passed
if len(sys.argv) != 2 or (sys.argv[1].lower() != 'gryffindor' and sys.argv[1].lower() != 'slytherin' and sys.argv[1].lower() != 'ravenclaw' and sys.argv[1].lower() != 'hufflepuff'):
    print("Usage: python filename.py name-of-house")
    print("where name-of-house is Gryffindor, Slytherin, Ravenclaw, Hufflepuff")
    exit()

# Get results from database
result = db.execute("SELECT first, middle, last, birth FROM students WHERE LOWER(house) = :house ORDER BY last",
                    house=sys.argv[1].lower())

# Print results
for row in result:
    if not row['middle']:
        print(f'{row["first"]} {row["last"]}, born {row["birth"]}')
    else:
        print(f'{row["first"]} {row["middle"]} {row["last"]}, born {row["birth"]}')