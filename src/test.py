def get_min_str(strs: str):
    sorted_str = sorted(strs)
    change_from, change_to = "", ""
    swapped = False
    result = ""
    for i in range(len(strs)):
        # 从strs找到第一个与sorted_str不同的字符，这两个不同的字符即为要交换的字符change_from, change_to
        # 先替换成change_from
        if change_from == "" and strs[i] != sorted_str[i]:
            change_from = sorted_str[i]
            change_to = strs[i]
            result += change_from
        # 后续找到第一个change_from，修改成change_to即可
        elif not swapped and change_from == strs[i]:
            result += change_to
            swapped = True
        # 已不需要替换，直接追加到result后
        else:
            result += strs[i]
    return result

print(get_min_str("abcdef"))
print(get_min_str("agcdef"))
print(get_min_str("bcdefa"))
print(get_min_str("aaddcc"))
