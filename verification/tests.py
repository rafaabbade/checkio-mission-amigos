"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        [
    {
        "input": [6, 2, [0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0]],
        "answer": 3
    },
    {
        "input": [12, 4, [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1]],
        "answer": 7
    },
    {
        "input": [9, 4, [1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0, 1]],
        "answer": 10
    },
    {
        "input": [4, 2, [1, 0, 0, 1], [1, 0, 0, 1]],
        "answer": 0
    },
    {
        "input": [6, 3, [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]],
        "answer": 9
    }
]
    ]
}
