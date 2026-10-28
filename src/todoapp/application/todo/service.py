from todoapp.domain.todo.types import Todo
from todoapp.domain.todo.validate import validate_title
from todoapp.infrastructure.todo.repository import (
    delete_todo_by_id,
    find_all_todos,
    find_todo_by_id,
    insert_todo,
    update_todo_done,
)


def list_todos() -> list[Todo]:
    return find_all_todos()


def create_todo(raw_title: str) -> Todo:
    title = validate_title(raw_title)
    return insert_todo(title)


def toggle_todo_done(todo_id: int) -> Todo | None:
    todo = find_todo_by_id(todo_id)
    if todo is None:
        return None
    return update_todo_done(todo_id, not todo["done"])


def remove_todo(todo_id: int) -> bool:
    return delete_todo_by_id(todo_id)
