import sqlite3

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from validate import validate_title

app = FastAPI()


def create_table():
    db = sqlite3.connect("todo.db")
    db.execute("""
    CREATE TABLE IF NOT EXISTS todos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      done INTEGER NOT NULL DEFAULT 0
    )
    """)
    db.commit()
    db.close()


create_table()


def find_all_todos():
    db = sqlite3.connect("todo.db")
    rows = db.execute("SELECT * FROM todos").fetchall()
    db.close()
    todos = []
    for row in rows:
        todos.append({"id": row[0], "title": row[1], "done": row[2] == 1})
    return todos


@app.get("/api/todos")
def list_todos():
    return find_all_todos()


def find_todo_by_id(todo_id):
    db = sqlite3.connect("todo.db")
    row = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    db.close()
    if row is None:
        return None
    return {"id": row[0], "title": row[1], "done": row[2] == 1}


def update_todo_done(todo_id, done):
    if done:
        done_for_sqlite = 1
    else:
        done_for_sqlite = 0
    db = sqlite3.connect("todo.db")
    db.execute("UPDATE todos SET done = ? WHERE id = ?", (done_for_sqlite, todo_id))
    db.commit()
    db.close()
    return find_todo_by_id(todo_id)


class TodoCreate(BaseModel):
    title: str


def insert_todo(title):
    db = sqlite3.connect("todo.db")
    cursor = db.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    db.commit()
    new_id = cursor.lastrowid
    db.close()
    return {"id": new_id, "title": title, "done": False}


@app.post("/api/todos", status_code=201)
def create_todo(body: TodoCreate):
    try:
        title = validate_title(body.title)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    return insert_todo(title)


def delete_todo_by_id(todo_id):
    db = sqlite3.connect("todo.db")
    cursor = db.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    db.commit()
    deleted = cursor.rowcount > 0
    db.close()
    return deleted


@app.put("/api/todos/{todo_id}")
def toggle_todo(todo_id: int):
    todo = find_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="見つかりません")
    return update_todo_done(todo_id, not todo["done"])


@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    if not delete_todo_by_id(todo_id):
        raise HTTPException(status_code=404, detail="見つかりません")
    return {"message": "削除しました"}


app.mount("/", StaticFiles(directory="public", html=True), name="public")
