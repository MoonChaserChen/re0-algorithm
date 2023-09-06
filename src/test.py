def longest_sub_str(strs: str):
    # 最大长度
    max_len, current_len = 0, 0
    for x in strs:
        if x.isnumeric():
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len


def assert_equals(expression, expected_value):
    assert expression == expected_value, f"expected value: {expected_value}, but got: {expression}"


assert_equals(longest_sub_str("abcd"), 0)
assert_equals(longest_sub_str("a5"), 1)
assert_equals(longest_sub_str("aa5"), 1)
assert_equals(longest_sub_str("aa5a"), 1)
assert_equals(longest_sub_str("aa5aa"), 1)
assert_equals(longest_sub_str("1234"), 4)
assert_equals(longest_sub_str("a1234"), 4)
assert_equals(longest_sub_str("a12a3456"), 4)
