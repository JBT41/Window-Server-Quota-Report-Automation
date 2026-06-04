import sqlite3
from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")

def select_all():
    conn = sqlite3.connect("quota.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT * 
    FROM quota
    WHERE date = ?
    """, (today,))

    rows = cur.fetchall()
    columns =[desc[0] for desc in cur.description]

    cur.close()
    conn.close()
    return columns,rows
