import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos?_limit=5")
todos = response.json()
print(f"{len(todos)} 件取得しました")

for todo in todos:
    if todo["completed"]:
        status = "✅"
    else:
        status = "⬜"
    print(f"{status} [{todo['id']}] {todo['title']}")