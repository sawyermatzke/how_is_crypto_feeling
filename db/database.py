import sqlite3
from datetime import datetime

def connect_to_db():
    return sqlite3.connect('db/bitcoin_prices.db')

def create_table():
    conn = connect_to_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices
                 (timestamp TEXT, price REAL)''')
    conn.commit()
    conn.close()

def insert_price(price):
    conn = connect_to_db()
    c = conn.cursor()
    c.execute("INSERT INTO prices VALUES (?, ?)", (datetime.now(), price))
    conn.commit()
    conn.close()
