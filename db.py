import sqlite3 
def get_connection():
    return sqlite3.connect("contact.db")

def create_table(): 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    sno INTEGER PRIMARY KEY ,
    name VARCHAR(70) NOT NULL ,
    phone_number VARCHAR(15) UNIQUE
    )
    """)

    print("created table successfully")

    conn.commit()
    conn.close()


create_table()

