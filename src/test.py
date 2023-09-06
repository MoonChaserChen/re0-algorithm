def calc_min_sum(strs: str):
    abs_current_num, min_sum = 0, 0
    abs_flag = 1
    for x in strs:
        if x == "-":
            min_sum += abs_current_num * abs_flag
            abs_flag = -1
            abs_current_num = 0
        elif x.isnumeric():
            if abs_flag == 1:
                min_sum += abs_current_num
                abs_current_num = int(x)
            else:
                abs_current_num = abs_current_num * 10 + int(x)
        else:
            min_sum += abs_current_num * abs_flag
            abs_current_num = 0
            abs_flag = 1
    min_sum += abs_current_num * abs_flag
    return min_sum


print(calc_min_sum("bb1234"))
print(calc_min_sum("bb12-34aa"))
