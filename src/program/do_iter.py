# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def findMinAndMax(L):

    # 1.空列表
    if len(L) == 0:
        return (None, None)

    # 2.最大值和最小值
    min_value = L[0]
    max_value = L[0]

    # 3.遍历数组，替换最大值最小值
    for num in L[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    return (min_value, max_value)


# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
