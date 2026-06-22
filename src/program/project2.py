s = ["f", "123", "abc"]

# 测量s
print(f"长度为：{len(s[2])}")

# 某学校决定，期末考试的成绩不公布具体的分数，而是采取A，B，C，D的等级进行公布。
# 要求使用键盘录入规则如下：
# 1.试卷总分：100分
# 2.A（85~100）
# B（70~84）
# C（60~69）
# D（60以下）

score = input("请输入你的成绩")
if 0 < int(score) > 100:
    print("成绩无效")
elif 85 <= int(score) <= 100:
    print("你的成绩为A")
elif 70 <= int(score) <= 84:
    print("你的成绩为B")
elif 60 <= int(score) <= 69:
    print("你的成绩为C")
else:
    print("你的成绩为D")
