def merge_arr(num_arr):
    result = []
    num_arr.sort(key=lambda y: y[0])
    for x in num_arr:
        if not result or result[-1][1] < x[0]:
            result.append(x)
        else:
            result[-1][1] = max(result[-1][1], x[1])
    return result


assert merge_arr([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_arr([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_arr([[1, 4], [2, 3]]) == [[1, 4]]
