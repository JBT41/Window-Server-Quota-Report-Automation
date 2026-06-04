import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
import traceback


from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")


from_address = os.getenv("FROM_ADDRESS")
to_address = os.getenv("TO_ADDRESS")



def send(columns, rows):
    msg = EmailMessage()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = "Quota Check"

    html = """
    <html>
    <body>
    <h2>Server Disk Space Report</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Server</th>
            <th>Available (GB)</th>
            <th>Status</th>
        </tr>
    """

    for server, space, date in rows:
        if space <= 20:
            colour = "#ffcccc"
            status = "LOW"
        elif space < 30:
            colour = "#fff3cd"
            status = "WARNING"
        else:
            colour = "#ccffcc"
            status = "OK"

        html += f"""
        <tr style="background-color:{colour}">
            <td>{server}</td>
            <td>{space:.2f}</td>
            <td>{status}</td>
        </tr>
        """

    html += """
    </table>
    <p>Generated: {}</p>
    </body>
    </html>
    """.format(datetime.now())

    msg.add_alternative(html, subtype="html")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.send_message(msg)


