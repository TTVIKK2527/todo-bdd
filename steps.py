import re
from src.todo import TodoList


def dispatch(context, keyword, text):
    if keyword == "Given" and text == "an empty task list": context["todo"] = TodoList()
    elif keyword == "When" and (match := re.fullmatch(r'I add "(.*)"', text)):
        context["todo"].add(match[1])
    elif keyword == "Then" and (match := re.fullmatch(r"there are (\d+) tasks", text)):
        assert len(context["todo"].all()) == int(match[1])
    elif keyword == "Then" and (match := re.fullmatch(r'task (\d+) is titled "(.*)"', text)):
        assert context["todo"].all()[int(match[1]) - 1]["title"] == match[2]
    elif keyword == "Then" and (match := re.fullmatch(r"task (\d+) is open", text)):
        assert context["todo"].all()[int(match[1]) - 1]["status"] == "open"
    else: raise NotImplementedError("Pending: " + keyword + " " + text)
