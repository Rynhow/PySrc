num = int(input('请输入一个三位数：'))

#数值拆分
ge = num % 10
shi = int(num) //10 % 10
bai = int(num) // 100 % 10

#输出
print(f'个位数为:{ge},十位数为:{shi},百位数为:{bai}')