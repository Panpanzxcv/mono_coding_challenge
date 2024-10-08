import csv
import sqlite3
from datetime import datetime, timedelta

# Connect to or create the SQLite database named 'weddings.db'
conn = sqlite3.connect('weddings.db')
cur = conn.cursor()

# Create the Users table if it doesn't exist. 
# The table has two columns: user_id (the primary key) and user_name.
cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id TEXT PRIMARY KEY,
    user_name TEXT
)
''')

# Create the Weddings table if it doesn't exist. 
# The table has two columns: user_id and wedding_date.
# The user_id is a foreign key that references the Users table.
cur.execute('''
CREATE TABLE IF NOT EXISTS Weddings (
    user_id TEXT PRIMARY KEY,
    wedding_date DATE,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)
''')

# Open the Users_Data.csv file in read mode
with open('Users_Data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        cur.execute('INSERT OR IGNORE INTO Users (user_id, user_name) VALUES (?, ?)', (row[0], row[1]))

# Open the Weddings_Data.csv file in read mode
with open('Weddings_Data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        cur.execute('INSERT OR IGNORE INTO Weddings (user_id, wedding_date) VALUES (?, ?)', (row[0], row[1]))

conn.commit()

# Task1: Query the database for users whose weddings are in June 2024
cur.execute('''
SELECT user_name FROM Users
JOIN Weddings ON Users.user_id = Weddings.user_id
WHERE strftime('%Y', wedding_date) = '2024' AND strftime('%m', wedding_date) = '06'
''')
june_weddings = cur.fetchall()

# Task2: Query the database for users whose weddings are in June 2024
today = datetime.now().date()
two_weeks_later = today + timedelta(weeks=2)

cur.execute('''
SELECT user_name FROM Users
JOIN Weddings ON Users.user_id = Weddings.user_id
WHERE wedding_date BETWEEN ? AND ?
''', (today, two_weeks_later))
upcoming_weddings = cur.fetchall()

# Write the results
with open('wedding_results.txt', 'w') as f:
    f.write('Weddings in June 2024:\n')
    for user in june_weddings:
        f.write(f'{user[0]}\n')
    
    f.write('\nWeddings in the next 2 weeks:\n')
    for user in upcoming_weddings:
        f.write(f'{user[0]}\n')

# Close the database connection
conn.close()

print("Results have been saved to 'wedding_results.txt'.")
