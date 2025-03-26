# 长度为 5 的数组
arr = [1, 2, 3, 4, 5]
i = 0
# 模拟环形数组，这个循环永远不会结束
while i < len(arr):
    print(arr[i])
    i = (i + 1) % len(arr)

