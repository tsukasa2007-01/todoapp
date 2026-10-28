import os
import sqlite3

from todoapp.domain.types import Todo


def connect() -> sqlite3.Connection:
    # テストでは環境変数 TODO_DB_PATH で別の DB ファイルに切り替える
    db = sqlite3.connect(os.environ.get("TODO_DB_PATH", "todo.db"))
    db.execute("""
    CREATE TABLE IF NOT EXISTS todos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      done INTEGER NOT NULL DEFAULT 0
    )
    """)
    return db


def todo_from_sqlite_row(row: tuple[int, str, int]) -> Todo:
    return {"id": row[0], "title": row[1], "done": row[2] == 1}


def find_all_todos() -> list[Todo]:
    db = connect()
    rows = db.execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    db.close()
    todos: list[Todo] = []
    for row in rows:
        todos.append(todo_from_sqlite_row(row))
    return todos


def find_todo_by_id(todo_id: int) -> Todo | None:
    db = connect()
    row = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    db.close()
    if row is None:
        return None
    return todo_from_sqlite_row(row)


def insert_todo(title: str) -> Todo:
    db = connect()
    cursor = db.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    db.commit()
    new_id = cursor.lastrowid
    db.close()
    assert new_id is not None
    return {"id": new_id, "title": title, "done": False}


def update_todo_done(todo_id: int, done: bool) -> Todo | None:
    if done:
        done_for_sqlite = 1
    else:
        done_for_sqlite = 0
    db = connect()
    cursor = db.execute(
        "UPDATE todos SET done = ? WHERE id = ?", (done_for_sqlite, todo_id)
    )
    db.commit()
    changed = cursor.rowcount > 0
    db.close()
    if not changed:
        return None
    return find_todo_by_id(todo_id)


def delete_todo_by_id(todo_id: int) -> bool:
    db = connect()
    cursor = db.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    db.commit()
    deleted = cursor.rowcount > 0
    db.close()
    return deleted
