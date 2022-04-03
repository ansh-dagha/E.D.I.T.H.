import sqlite3

conn = sqlite3.connect("assistant.db")
c = conn.cursor()

# c.execute('''
#         CREATE TABLE IF NOT EXISTS users
#         ([username] TEXT PRIMARY KEY, [password] TEXT)
#         ''')


# c.execute(''' INSERT INTO users VALUES
#             ('anshdagha', 'ansh1234')
#             ''')   
# conn.commit()
  

# c.execute('''
#         DELETE FROM users
#         ''')
# conn.commit()

c.execute(""" SELECT * FROM users """)        
    
print(c.fetchone())