import sqlite3
import sys
import os

db_path = os.path.join(os.path.dirname(sys.path[0]),'database\\assistant.db')
conn = sqlite3.connect(db_path)

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users
    ([username] TEXT PRIMARY KEY, [email] NVARCHAR(255), [password] TEXT)
    ''')

def userExists(username):
    c.execute("SELECT username FROM users where username=?", (username,))
    if(c.fetchone()):
        return True
    else:
        return False
        
def addDetails(username, email, password_hash):
    # print(username, email, password_hash)
    c.execute(''' INSERT INTO users VALUES
                (?, ?, ?)''', (username, email, password_hash))
    conn.commit()

def checkPassword(username, password_hash):
    c.execute("SELECT password FROM users where username=?", (username,))
    password = c.fetchone()[0]
    if password_hash == password:
        return True
    else:
        return False


# c.execute('''
#         DELETE FROM users
#         ''')
# conn.commit()

# c.execute(""" SELECT * FROM users """)

# print(c.fetchone())