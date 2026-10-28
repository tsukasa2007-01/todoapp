from typing import TypedDict


class Todo(TypedDict):
    id: int
    title: str
    done: bool
