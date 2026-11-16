import re
from src.todo import TodoList


def dispatch(context, keyword, text):
    if keyword == "Given" and text == "an empty task list": context["todo"] = TodoList()
    elif keyword == "Given" and (match := re.fullmatch(r'a task "(.*)"', text)):
        context["todo"] = TodoList()
        context["todo"].add(match[1])
    elif keyword == "Given" and (match := re.fullmatch(r'I also have a task "(.*)"', text)):
        context["todo"].add(match[1])
    elif keyword == "When" and (match := re.fullmatch(r'I add "(.*)"', text)):
        context["todo"].add(match[1])
    elif keyword == "Then" and (match := re.fullmatch(r"there are (\d+) tasks", text)):
        assert len(context["todo"].all()) == int(match[1])
    elif keyword == "Then" and (match := re.fullmatch(r'task (\d+) is titled "(.*)"', text)):
        assert context["todo"].all()[int(match[1]) - 1]["title"] == match[2]
    elif keyword == "When" and (match := re.fullmatch(r"I complete task (\d+)", text)):
        context["todo"].complete(int(match[1]))
    elif keyword == "Then" and (match := re.fullmatch(r"task (\d+) is (open|done)", text)):
        assert context["todo"].all()[int(match[1]) - 1]["status"] == match[2]
    elif keyword == "Then" and (match := re.fullmatch(r'the open list contains only "(.*)"', text)):
        assert [task["title"] for task in context["todo"].open_tasks()] == [match[1]]
    else: raise NotImplementedError("Pending: " + keyword + " " + text)
