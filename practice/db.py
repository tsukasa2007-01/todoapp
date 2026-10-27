import sqlite3

db = sqlite3.connect("todo.db")

db.execute("""
CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0
)
""")
db.execute("INSERT INTO todos (title) VALUES (?)", ("牛乳を買う",))
db.commit()
db.close()
print("追加しました")
