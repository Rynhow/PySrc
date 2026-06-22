def trim(s):

    # 先处理左边界

    left = 0
    while left < len(s) and s[left] == " ":
        left = left + 1

    # 字符串全是空格

    if left == len(s):
        return ""

    # 右边界

    right = len(s) - 1

    while right >= 0 and s[right] == " ":
        right = right - 1

    return s[left : right + 1]


# 测试:
if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")
