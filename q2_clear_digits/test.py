# Teacher/platform test file for Q2: Clear Digits

def check(solution):
    tests = [
        ("abc", "abc"),
        ("cb34", ""),
        ("a1b2c3", ""),
        ("abc123", ""),
        ("x1yz", "yz"),
        ("leetcode", "leetcode"),
        ("a2bc3d", "bd"),
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
