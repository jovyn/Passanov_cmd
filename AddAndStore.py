import sqlite3
import os
import datetime
from CheckPasscode import CheckPass
from Encryption import EncryptData

db_name = 'passanov.db'

def CreateDB():
    global db_name
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(''' CREATE TABLE pnov (date text, encryp_data text)''')
    conn.commit()
    conn.close()
    print("\n DB was not present ... DB created !\n")

def AddToDBRecords(encryptstr):
    global db_name
    dtob = str(datetime.datetime.now())
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO pnov (date, encryp_data) VALUES (?,?)",(dtob, encryptstr))
    conn.commit()
    conn.close()
    print("\n Saved to DB :) \n")

def StoreCredentials(acc_name,user,passwd,some_comments, mastercode, secretcode):
    global db_name
    #print("Good to Go ")
    encrypted_string = EncryptData(acc_name, user, passwd, some_comments, mastercode, secretcode)
    #print(encrypted_string)

    if not os.path.exists(db_name):
        CreateDB()

    AddToDBRecords(encrypted_string)



def AddCredentials(master, secret):
    account_name = input("Insert Account/Company name (eg: Facebook): ")
    username = input(f"Insert the username for {account_name}: ")
    passcode = input(f"Insert the password for {account_name}: ")
    comments = input(f"Additional Comments for {username} of {account_name}: ")

    if CheckPass(passcode):
        print("WARNING : Password entered is insecure ")
        reply = input("Do you want to continue ?? [Y/N]")

        if str(reply).upper() == 'Y':
            StoreCredentials(account_name, username, passcode, comments, master, secret)

        else:
            print("\n See ya later ... \n")
            sys.exit(1)



    else:
        print("\n Saving Credentials ... \n")
        StoreCredentials(account_name,username,passcode,comments, master, secret)

