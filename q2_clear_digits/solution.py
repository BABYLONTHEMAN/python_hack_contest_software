from test import check

def solution(s: str) -> str:
    stack = []

    for c in s:
        if not c.isnumeric():
            stack.append(c)
        else:
            stack.pop()

    return "".join(stack)

check(solution)
