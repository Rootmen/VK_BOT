import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db_recipient.db")


def createRecipientTable():
    # Подключение к БД
    db = sqlite3.connect(db_path)
    conn = db
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE RecipientTable(id_user String)")
    conn.commit()


def addRecipient(user_id):
    # Подключение к БД
    db = sqlite3.connect(db_path)
    conn = db
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RecipientTable WHERE id_user = '" + user_id + "'")
    if cursor.fetchall():
        return
    cursor.execute("INSERT INTO RecipientTable VALUES (" + user_id + ")")
    conn.commit()


def startRecipientCall(call_fincion, args):
    # Подключение к БД
    db = sqlite3.connect(db_path)
    conn = db
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RecipientTable")
    mysel = cursor.execute("SELECT * FROM RecipientTable")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            call_fincion(row[j], *args)
    conn.close()


if __name__ == '__main__':
    createRecipientTable()
