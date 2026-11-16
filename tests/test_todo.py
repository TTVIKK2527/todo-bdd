import unittest
from src.todo import TodoList


class TodoTests(unittest.TestCase):
    def test_completion_changes_only_the_selected_task(self):
        todo = TodoList()
        todo.add("Water basil")
        todo.add("Buy soil")
        todo.complete(1)
        self.assertEqual([task["status"] for task in todo.all()], ["done", "open"])

    def test_unknown_id_is_rejected(self):
        todo = TodoList()
        todo.add("Water basil")
        for task_id in (0, -1, 2, True, "1"):
            with self.subTest(task_id=task_id), self.assertRaises(ValueError): todo.complete(task_id)

    def test_add_creates_open_task_with_stable_id(self):
        todo = TodoList()
        task = todo.add("  Water basil  ")
        self.assertEqual(task, {"id": 1, "title": "Water basil", "status": "open"})
        self.assertEqual(todo.all(), [task])

    def test_empty_title_is_rejected(self):
        for title in ("", " ", None):
            with self.subTest(title=title), self.assertRaises(ValueError): TodoList().add(title)

    def test_returned_data_cannot_mutate_the_task_list(self):
        todo = TodoList()
        task = todo.add("Water basil")
        task["title"] = "changed"
        result = todo.all()
        result[0]["title"] = "changed again"
        result.clear()
        self.assertEqual(todo.all()[0]["title"], "Water basil")


if __name__ == "__main__": unittest.main()
