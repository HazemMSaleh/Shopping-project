import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, date_opened TEXT, date_fulfilled_TEXT, other TEXT, frequent_item_id INTEGER)')
print ("Table created successfully");
conn.close()