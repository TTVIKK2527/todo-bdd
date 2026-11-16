Feature: List remaining tasks
  Scenario: Completed tasks are absent from the open list
    Given a task "Water basil"
    And I also have a task "Buy soil"
    When I complete task 1
    Then the open list contains only "Buy soil"
