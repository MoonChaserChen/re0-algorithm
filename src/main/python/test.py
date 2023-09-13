def solve(num: int):
    result = []
    left, right = 1, 2
    while left < right:
        s = sum(range(left, right + 1))
        if s == num:
            result.append((left, right))
            left += 1
        elif s < num:
            right += 1
        else:
            left += 1
    return result

print(solve(9))
