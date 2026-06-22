num = int(input('请输入一个三位数：'))

#数值拆分
ones = num % 10
tens = int(num) //10 % 10
hundreds = int(num) // 100 % 10

#输出
print(f'个位数为:{ones},十位数为:{tens},百位数为:{hundreds}')