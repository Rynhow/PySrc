# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000
num1 = hex(n1)
num2 = hex(n2)
print(f'第一个数:{num1},第二个数{num2}')

#定义函数
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

#验证
print(my_abs(-99))

# 空函数

#
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# def nop():
#     pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：
# if age >= 18:
#     pass
# 缺少了pass，代码运行就会有语法错误。

#Python的函数返回多值其实就是返回一个tuple


# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax2+bx+c=0ax2+bx+c=0 的两个解。
# 提示：
# 计算平方根可以调用math.sqrt()函数：
# >>> import math
# >>> math.sqrt(2)
# 1.4142135623730951

import math

def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return '方程无实数根'
    else:
     x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
     x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1,x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    