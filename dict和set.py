s = {'a':1,'b':2,'c':3}#dict字典
print(s['c'])
s['a'] = 5#覆盖原有值
print(s['a'])

#删除dict里面的元素
'''s.pop('a')
print(s['a'])'''


#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
k = {1, 2, 3}  #set

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
k.add(4)
print(k)

# 通过remove(key)方法可以删除元素：
k.remove(4)
print(k)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：