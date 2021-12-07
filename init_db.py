import sqlite3

#crea tion de la base de donné
connection = sqlite3.connect('database.db')

with open('shema.sql') as f:
    connection.executescript(f.read())

#vous créez un objet Cursor qui vous permet d'utiliser sa méthode execute()
# cur = connection.cursor()
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )
#
# connection.commit()
# connection.close()