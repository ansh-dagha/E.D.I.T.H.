import sqlite3
import sys
import os

# db_path = os.path.join(os.path.dirname(sys.path[0]),'database\\assistant.db')
db_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\database\\assistant.db')
conn = sqlite3.connect(db_path)

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users
    ([username] TEXT PRIMARY KEY,
    [email] NVARCHAR(255),
    [password] TEXT,
    [voice] INTEGER DEFAULT 0,
    [addressee] TEXT DEFAULT 'Boss')
    ''')

def userExists(username):
    c.execute("SELECT username FROM users where username=?", (username,))
    if(c.fetchone()):
        return True
    else:
        return False
        
def addDetails(username, email, password_hash):
    # print(username, email, password_hash)
    c.execute(''' INSERT INTO users (username, email, password) VALUES
                (?, ?, ?)''', (username, email, password_hash, ))
    conn.commit()

def updatePreference(voice, addressee, username):
    c.execute(''' UPDATE users SET voice=?, addressee=? WHERE username=?''', (voice, addressee, username,))
    conn.commit()

def checkPassword(username, password_hash):
    c.execute("SELECT password FROM users where username=?", (username,))
    password = c.fetchone()[0]
    if password_hash == password:
        return True
    else:
        return False

def getUserDetails(username):
    c.execute("SELECT * FROM users where username=?", (username,))
    fields = c.fetchone()
    # response = {
    #     'username' : fields[0],
    #     'email' : fields[1],
    #     'voice' : fields[3],
    #     'addressee' : fields[4]
    # }
    return (fields[1], fields[3], fields[4])

def updateEmail(email, username):
    c.execute(''' UPDATE users SET email=? WHERE username=?''', (email, username,))
    conn.commit()

def updatePassword(password_hash, username):
    c.execute(''' UPDATE users SET password=? WHERE username=?''', (password_hash, username,))
    conn.commit()

# c.execute('''
#         DELETE FROM users WHERE username IN ('isha','priya','prachi')
#         ''')
# conn.commit()

# c.execute(""" SELECT * FROM users """)

# print(c.fetchall())