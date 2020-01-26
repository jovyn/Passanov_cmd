import sqlite3
from Encryption import DecryptData
from unidecode import unidecode

db_name = 'passanov.db'


def ViewCredentials(master,secret):
    global db_name
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''SELECT * FROM pnov''')

    rows = c.fetchall()

    for row in rows:
        decrypted_data = DecryptData(row[1], master, secret)
        decrypted_data = decrypted_data.decode('utf-8', errors='replace')
        #decrypted_data = unidecode(str(decrypted_data))
        print("------------")
        print(str(row[0])+ "  ---->  " + str(decrypted_data))




