Feature: Complete a task
  Scenario: A completed task changes status
    Given a task "Water basil"
    When I complete task 1
    Then task 1 is done
