import sqlite3

db = sqlite3.connect("todo.db")
rows = db.execute("SELECT * FROM todos").fetchall()
todos = []
for row in rows:
    todo = {"id": row[0], "title": row[1], "done": row[2] == 1}
    todos.append(todo)


def show_todos(todos) -> None:
    for todo in todos:
        if todo["done"]:
            status = "✅"
        else:
            status = "⬜"
        print(f"{status} [{todo['id']}] {todo['title']}")


show_todos(todos)
db.close()
