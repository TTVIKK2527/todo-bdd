class TodoList:
    def __init__(self): self._tasks = []

    def add(self, title):
        if not isinstance(title, str) or not title.strip(): raise ValueError("Title is required")
        task = {"id": len(self._tasks) + 1, "title": title.strip(), "status": "open"}
        self._tasks.append(task)
        return dict(task)

    def all(self): return [dict(task) for task in self._tasks]
