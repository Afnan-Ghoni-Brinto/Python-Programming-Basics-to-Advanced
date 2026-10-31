import sqlite3
from pathlib import Path

database = Path(__file__).with_name("students.db")
with sqlite3.connect(database) as connection:
    connection.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL)""")
    connection.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Rahim", 20))
    for row in connection.execute("SELECT id, name, age FROM students"):
        print(row)
# Each run inserts another demonstration record.
