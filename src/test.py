def split_str(strs: str, n: int):
    str_list = strs.split("-")
    split_list = []
    for i in range(len(str_list)):
        if i == 0:
            split_list.append(str_list[i])
        else:
            j, k = 0, 0
            curr_str = ""
            while j < len(str_list[i]):
                if k < n:
                    curr_str += str_list[i][j]
                    k += 1
                else:
                    split_list.append(curr_str)
                    curr_str = str_list[i][j]
                    k = 0
                j += 1
            if curr_str != "":
                split_list.append(curr_str)
    return "-".join(map(uni_case, split_list))


def uni_case(strs: str):
    low_cnt, up_cnt = 0, 0
    for x in strs:
        if x.islower():
            low_cnt += 1
        elif x.isupper():
            up_cnt += 1
    if low_cnt > up_cnt:
        return strs.lower()
    elif up_cnt > low_cnt:
        return strs.upper()
    return strs


print(split_str("12abc-abCABc-4aB@", 3))
