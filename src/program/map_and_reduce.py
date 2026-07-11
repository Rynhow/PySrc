# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

DIGITS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def char2(ch):
    return DIGITS[ch]


def str2float(s):
    parts = s.split(".")
    left_part = parts[0]  # 整数部分字符串
    right_part = parts[1]

    int_num = reduce(lambda x, y: x * 10 + y, map(char2, left_part))
    frac_num = reduce(lambda x, y: x * 10 + y, map(char2, right_part))

    frac_num = frac_num / 10 ** len(left_part)
    return frac_num + int_num


pass


L = "123.456"
print(str2float(L))

print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
