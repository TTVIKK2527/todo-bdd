Feature: Add a task
  Scenario: The created task is visible
    Given an empty task list
    When I add "Water basil"
    Then there are 1 tasks
    And task 1 is titled "Water basil"
    And task 1 is open
