import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert sample data
users = [
    ('admin', 'password123'),
    ('user1', 'mypassword'),
    ('user2', 'password321')
]

cursor.executemany('''
INSERT INTO users (username, password) VALUES (?,?)
''', users)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database and sample data created successfully.")
