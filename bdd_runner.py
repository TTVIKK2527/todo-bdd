"""Small explicit Gherkin subset runner: Feature, Scenario, Given, When, Then, And.

This is not a full Cucumber implementation: outlines, tags and data tables are unsupported.
"""
from pathlib import Path
import re
import steps


def run_feature(path):
    scenarios = []
    current = None
    previous = None
    saw_feature = False
    for number, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"): continue
        if line.startswith("Feature:"):
            if saw_feature or not line[8:].strip(): raise ValueError(f"{path}:{number}: invalid Feature")
            saw_feature = True
        elif line.startswith("Scenario:"):
            if not saw_feature: raise ValueError("Scenario before Feature")
            current = {"name": line[9:].strip(), "steps": []}
            scenarios.append(current)
            previous = None
        else:
            match = re.fullmatch(r"(Given|When|Then|And) (.+)", line)
            if not match or current is None: raise ValueError(f"{path}:{number}: unsupported syntax")
            keyword, text = match.groups()
            if keyword == "And":
                if previous is None: raise ValueError("And requires an earlier step")
                keyword = previous
            current["steps"].append((keyword, text))
            previous = keyword
    if not scenarios: raise ValueError("Feature has no scenarios")
    for scenario in scenarios:
        keywords = [key for key, _ in scenario["steps"]]
        if not all(key in keywords for key in ("Given", "When", "Then")):
            raise ValueError("Every scenario requires Given, When, Then")
        if keywords != sorted(keywords, key={"Given": 0, "When": 1, "Then": 2}.get):
            raise ValueError("Steps must follow Given, When, Then order")
        context = {}
        for keyword, text in scenario["steps"]: steps.dispatch(context, keyword, text)
        print("PASS:", path.name, "-", scenario["name"])
    return len(scenarios)


def main():
    count = sum(run_feature(path) for path in sorted(Path("features").glob("*.feature")))
    if not count: raise ValueError("No BDD scenarios found")
    print(f"PASS: {count} BDD scenarios")


if __name__ == "__main__": main()
