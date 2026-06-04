import subprocess
import json
import sqlite3
from datetime import datetime
from DB import *
from smtp_helper import *
conn = sqlite3.connect("quota.db")
cur = conn.cursor()
date = datetime.today().strftime("%Y-%m-%d")


cur.execute("""
CREATE TABLE IF NOT EXISTS quota (
    server TEXT,
    available_gb REAL,
    date TEXT,
    UNIQUE(server, date)
)
""")

if __name__ == '__main__':
    result = subprocess.run(

    ["powershell", "-ExecutionPolicy", "Bypass", "-File",
    r"C:\Users\User\ApplicationSupport\PythonProjects\Quota_Check\src\QuotaCheck.ps1"],
    capture_output=True,
        text=True,
        timeout=300
    )

    data = json.loads(result.stdout)
    rows = []

    for item in data:
        rows.append((item.get("Server"), item.get("AvailableGB"),date))

    cur.executemany("INSERT OR IGNORE INTO quota VALUES (?, ?, ?)", rows)
    conn.commit()
    print("Script finished")

    columns,rows = select_all()
    send(columns,rows)
