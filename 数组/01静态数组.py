'''
静态数组
增：
- 在末尾追加元素：O(1)。
- 在中间（非末尾）插入元素：O(N)

删：
- 删除末尾元素：O(1)。
- 删除中间（非末尾）元素：O(N)。

查：给定指定索引，查询索引对应的元素的值，时间复杂度 O(1)

改：给定指定索引，修改索引对应的元素的值，时间复杂度 O(1)。
'''

list = [0]*10

for i in range(4):
    list[i] = i+1

#在末尾加入元素
list[4] = 5
print(list)

#在中间插入元素
for index in range(5,2,-1):
    list[index] = list[index-1]

list[2] = 2.5

print(list)

#数组空间满了
# 1创建新数组
list2 = list + [0]*5
print(list)
list2[14] = 14
print(list2)

#查 比如查 index 2
print(list[2])

#改 比如改 index 5
list[5] = 5.5
print(list)


