sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for L in L:
    print(f'Hello,{L}')

#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
