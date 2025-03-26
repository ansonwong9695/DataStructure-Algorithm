"""
动态数组
"""
# 原生动态数组
list = [0]*5

# 1.增 O(1)
list.append(1)
print(list)

#在中间插入 O(N)
list.insert(3,"x")
print(list)

# 2.删
#删最后一个元素 O(1)
list.pop()
print(list)
#删除指定元素 O(N)
list.pop(3)
print(list)

# 3.改 O(1)
list[2] = 1
print(list)

# 4.查 O(1)
#根据索引查找 O(1)
print(list[2])
# 根据元素查找 O(N)
print(list.index(1))

