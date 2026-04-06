#输出
print('hello world')
name = input()
print('你好')
print(name)

a = 10
b = 20
print(f'第一个数字{a},第二个数字{b}')

#练习2.用一个变量表示微信余额
#需求：一开始，微信余额为100元，收到了一个2元的红包，输出目前余额
money = 100#开始金额
money = money + 2#收到红包金额
#输出
print(f'微信余额为{money}')

#练习3.在游戏当中，人物的血量是一个随时会发生变化的数据，定义变量blood去记录假设:
#人物初始血量为:100，对战时，受到80点伤害，自己用技能恢复60点血量，请问:目前人物最终血量为多少?(用变量完成)

#初始血量
blood = 100

#对战
blood = blood -80 + 60

#输出
print(f'目前人物最终血量为:{blood}')
print(f"占{len(str(money).encode('utf-8'))}个字节")

#练习
# 打印Apple
# 打印Python
# 打印Bob
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
#1.apple
print(L[0][0])

#2.python
print(L[1][1])

#3.Bob
print(L[2][2])



