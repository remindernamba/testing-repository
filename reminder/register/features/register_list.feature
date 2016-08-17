Feature: Register list

    Scenario: Polls list without any polls
        When I access the "polls list" url
        Then I see a text "We didn't find any polls!"

    Scenario: Polls list with one poll
        Given a poll with the title "Hello world"
        When I access the "polls list" url
        Then I see a text "Hello world"
        And I do not see a text "We didn't find any polls!