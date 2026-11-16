from src.todo import TodoList

todo = TodoList()
print("Lisa:", todo.add("Kasta basiilikut"))
print("Lisa:", todo.add("Osta mulda"))
todo.complete(1)
print("Kõik:", todo.all())
print("Tegemata:", todo.open_tasks())
