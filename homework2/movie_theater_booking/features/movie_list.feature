Feature: Movie listings

  Scenario: View the movie listings page
    Given the movie listing page is available
    When I request the movie listing page
    Then the page should respond successfully
