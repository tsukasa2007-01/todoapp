from typing import TypedDict

class Todo(TypedDict):
    id: int
    title: str
    done: bool
todos: list[Todo]=[{"id":1,"title":"牛乳を買う","done":False},{"id":2,"title":"日報を書く","done":True},{"id":3,"title":"Typescriptを学ぶ","done":False}]
def show_todos(todos: list[Todo]) -> None:
    for todo in todos:
        if todo["done"]:
            status = "✅"
        else:
            status = "⬜"
        print(f"{status} [{todo["id"]}] {todo["title"]}")

print("=== TODO 一覧 ===")
show_todos(todos)
def add_todo(todos: list[Todo], title: str) -> list[Todo]:
    new_id = len(todos)+1
    new_todo: Todo = {"id":new_id, "title": title, "done": False}
    return [*todos, new_todo]

updated_todos = add_todo(todos, "掃除をする")

print("")
print("=== 追加後の TODO 一覧 ===")
show_todos(updated_todos)
