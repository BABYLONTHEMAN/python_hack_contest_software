# Teacher/platform test file for Q1: Goal Parser Interpretation

def check(solution):
    tests = [
        ("G()(al)", "Goal"),
        ("G()()()()(al)", "Gooooal"),
        ("(al)G(al)()()G", "alGalooG"),
        ("G", "G"),
        ("()", "o"),
        ("(al)", "al"),
    ]

    passed = 0

    for index, (input_value, expected) in enumerate(tests, start=1):
        try:
            actual = solution(input_value)

            if actual == expected:
                print(f"Test {index}: PASS")
                passed += 1
            else:
                print(f"Test {index}: FAIL")
                print("Input:   ", input_value)
                print("Expected:", expected)
                print("Actual:  ", actual)
                print()

        except Exception as error:
            print(f"Test {index}: ERROR")
            print("Input:", input_value)
            print("Error:", error)
            print()

    print("----------------------")
    print(f"Passed {passed} / {len(tests)} tests")
