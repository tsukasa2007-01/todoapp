import sqlite3

db = sqlite3.connect("practice.db")

db.execute("""
CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0
)
""")

db.execute("DELETE FROM todos")
db.execute("INSERT INTO todos (title) VALUES (?)", ("牛乳を買う",))
db.execute("INSERT INTO todos (title) VALUES (?)", ("日報を書く",))
db.execute("INSERT INTO todos (title) VALUES (?)", ("掃除をする",))
db.commit()
print("最初:", db.execute("SELECT * FROM todos").fetchall())

db.execute("UPDATE todos SET done = ? WHERE id = ?", (1, 2))
db.commit()
print("直した後:", db.execute("SELECT * FROM todos").fetchall())

db.execute("DELETE FROM todos WHERE id = ?", (1,))
db.commit()
print("消した後:", db.execute("SELECT * FROM todos").fetchall())

db.close()