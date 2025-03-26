class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None


# 输入一个数组转换成链表
def create_linked_list(arr: list[int]) -> ListNode:
    # 判断链表是不是空
    if arr is None or len(arr) == 0:
        return None

    #循环arr 复制到listNode
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

#查询

# 1. 创建单链表
cur_node = create_linked_list([1,2,3,4,5,6,7,8,9])

# 2. 循环打印单链表
while cur_node is not None:
    # print(cur_node.val)
    cur_node = cur_node.next


#增加

#增加在头部
cur_node = create_linked_list([1,2,3,4,5])
new_head = ListNode(0)
new_head.next = cur_node
cur_node = new_head

#增加在尾部
# 1. 创建
cur_node = create_linked_list([1,2,3,4,5])
head = cur_node
# print(cur_node.val)
# 2. 循环到尾部node
while cur_node.next is not None:
    # print(cur_node.val)
    cur_node = cur_node.next
cur_node.next = ListNode(6)
cur_node = cur_node.next
# print(cur_node.val)
while head is not None:
    # print(head.val)
    head = head.next

#增加在中间
cur_node = create_linked_list([1,2,3,4,5])
head = cur_node

# 1. 判断插入点，进行循环到那个节点
insert = 2
for i in range(insert):
    cur_node = cur_node.next

tmp = cur_node.next

cur_node.next = ListNode(66)

cur_node = cur_node.next

cur_node.next = tmp

while head is not None:
    # print(head.val)
    head = head.next


# 删
cur_node = create_linked_list([1,2,3,66,4,5])
head = cur_node

del_node_index = 3

for i in range(del_node_index-1):
    cur_node = cur_node.next

print(cur_node.val)

cur_node.next = cur_node.next.next

while head is not None:
    print(head.val)
    head = head.next


#删除尾部元素
cur_node = create_linked_list([1,2,3,4,5])

while cur_node.next.next is not None:
    cur_node = cur_node.next

cur_node.next = None


#删除头部元素
cur_node = create_linked_list([1,2,3,4,5])
cur_node = cur_node.next