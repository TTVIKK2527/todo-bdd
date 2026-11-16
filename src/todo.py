def copy_tasks(tasks): return [dict(task) for task in tasks]


class TodoList:
    def __init__(self): self._tasks = []

    def add(self, title):
        if not isinstance(title, str) or not title.strip(): raise ValueError("Title is required")
        task = {"id": len(self._tasks) + 1, "title": title.strip(), "status": "open"}
        self._tasks.append(task)
        return dict(task)

    def all(self): return copy_tasks(self._tasks)

    def _find(self, task_id):
        if type(task_id) is not int: raise ValueError("Unknown task")
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        raise ValueError("Unknown task")

    def complete(self, task_id): self._find(task_id)["status"] = "done"

    def open_tasks(self): return [dict(task) for task in self._tasks if task["status"] == "open"]
