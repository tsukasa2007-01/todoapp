from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from todoapp.application.todo.service import (
    create_todo,
    list_todos,
    remove_todo,
    toggle_todo_done,
)
from todoapp.domain.todo.types import Todo

app = FastAPI()


class TodoCreate(BaseModel):
    title: str


@app.get("/api/todos")
def get_todos() -> list[Todo]:
    return list_todos()


@app.post("/api/todos", status_code=201)
def post_todo(body: TodoCreate) -> Todo:
    try:
        return create_todo(body.title)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.put("/api/todos/{todo_id}")
def put_todo(todo_id: int) -> Todo:
    todo = toggle_todo_done(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="見つかりません")
    return todo


@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int) -> dict[str, str]:
    if not remove_todo(todo_id):
        raise HTTPException(status_code=404, detail="見つかりません")
    return {"message": "削除しました"}


app.mount("/", StaticFiles(directory="public", html=True), name="public")
