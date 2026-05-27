import mysql.connector
import csv

def export_table():
    conn = mysql.connector.connect(
        host="192.168.10.21",
        user="wmsuser",
        password="Admin1234@",
        database="wms"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM commandes")

    with open("/opt/ntl-systoolbox/outputs/commandes.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())

    conn.close()
