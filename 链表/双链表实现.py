"""
双链表实现的几个注意事项
1. 必须要有 头尾节点的应用，让我们在实际使用中 能快速访问到节点，因为在使用链表时特别是尾部插入，这个是高频操作，如果每次都循环一边链表进行插入是非常费事 时间复杂度 为O(n)
2. 创建虚拟的头节点(dummy_head)和尾节点(dummy_tail),这个有助于减少边界情况的判断和空指针的问题，并且统一插入方法
3. 还有就是内存泄露问题，当你移除节点之间的连接，废弃的节点上的连接，最好移除，在 python java 语言有垃圾回收机制去处理这些，可以不做处理
链表的特点
1. 链表不需要连续的内存空间，去实现，可以散布在内存空间的任意位置，节点之间，通过指针相互连接，提高内存使用效率
2. 节点之间不需要连接，可以直接拆掉，不需要考虑扩容缩容，数据搬迁等问题
3. 缺点是无法像数组一样通过索引快速访问，要通过循环节点，得知想要的节点
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    #加
    def add_first(self,val):
        new_head = Node(val)

        # 给新的 node 建立连接
        # dummy_head <-- new_head --> prev_head
        prev_head = self.dummy_head.next
        new_head.next = prev_head
        new_head.prev = self.dummy_head

        # dummy_head <--> new_head <--> prev_head
        prev_head.prev = new_head
        self.dummy_head.next = new_head

        self.size += 1

    def add_last(self,val):
        new_tail = Node(val)

        #给新的 node 建立连接
        # prev_tail<-- new_tail -->dummy_tail
        prev_tail = self.dummy_tail.prev
        new_tail.prev = prev_tail
        new_tail.next = self.dummy_tail

        #修改 prev_tail 和 dummy_tail 的连接
        # prev_tail<--> new_tail <-->dummy_tail
        prev_tail.next = new_tail
        self.dummy_tail.prev = new_tail

        self.size += 1

    def add(self,index,val):
        #检查 index 是否合规
        self.check_position_index(index)

        #如果index 是最后一个直接调用 add_last
        if index == self.size:
            self.add_last(val)
            return

        #在 index 位置插入,先循环到 index 位置的Node
        node = self.get_node(index)

        #创建插入 Node
        new_node = Node(val)
        #连接新节点
        #prev_node --> new_node --> node
        prev_node =node.prev
        new_node.next = node
        new_node.prev = prev_node

        #修改 prev/next node的连接
        # prev_node <--> new_node <--> node
        prev_node.next = new_node
        node.prev = new_node

        self.size += 1

    #删
    def remove_first(self):
        #判断是否有node 可以移除
        if self.size < 1:
            raise IndexError(f"No element to remove")

        #获取当前头节点，以及获取头节点连接节点
        head = self.dummy_head.next
        next_node = head.next

        #去除互相的连接,把后节点与dummy_head 相连
        # dummy_head <--> next_node
        self.dummy_head.next = next_node
        next_node.prev = self.dummy_head

        self.size -= 1
        return head.val
    def remove_last(self):
        if self.size <1:
            raise IndexError(f"No element to remove")

        #获取尾部节点，获取尾部节点前一个节点
        tail = self.dummy_tail.prev
        prev_node = tail.prev

        #去除尾部节点与 dummy_tail 的连接，把前节点与 dummy_tail相连
        # prev_node <--> dummy_tail
        prev_node.next = self.dummy_tail
        self.dummy_tail.prev = prev_node

        self.size -= 1
        return tail.val

    def remove(self,index):
        #判断 index 是否在合规范围
        self.check_element_index(index)

        # 如果是最后一个直接调用，remove_last
        if index == self.size -1:
            value = self.remove_last()
            return value

        #获取对应 index 的 node
        node = self.get_node(index)

        #获取 node 的前节点，后节点
        prev_node = node.prev
        next_node = node.next

        #去除 前后节点之间的连接，前后节点互相连接
        # prev_node <--> next_node
        prev_node.next = next_node
        next_node.prev = prev_node

        # size -1
        self.size -= 1
        return node.val

    #查
    def get(self,index):
        self.check_element_index(index)
        node = self.get_node(index)
        return node.val

    def get_first(self):
        if self.size < 1:
            raise IndexError(f"No element in the list")

        return self.dummy_head.next.val

    def get_last(self):
        if self.size < 1:
            raise IndexError(f"No element in the list")

        return self.dummy_tail.prev.val

    #改
    def set(self,index,val):
        #检查 index 合规性
        self.check_element_index(index)

        #获取 node
        node = self.get_node(index)

        #创建新的 node
        new_node = Node(val)

        #获取 node 的前后节点
        next_node = node.next
        prev_node = node.prev

        #修改前后节点的连接，到new_node
        prev_node.next = new_node
        next_node.prev = new_node

        #修改 new_node 的连接
        new_node.next = next_node
        new_node.prev = prev_node


        #删除 node 的连接
        node.next = None
        node.prev = None

        return node.val


    #工具函数
    def check_position_index(self,index):
        if not self.is_position(index):
            raise IndexError(f"Index: {index}, Size : {self.size}")

    def check_element_index(self,index):
        if not self.is_element(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def is_element(self,index):
        return 0 <= index < self.size

    def is_position(self,index):
        return 0 <= index <= self.size

    #获取对应 index 的 node
    def get_node(self,index):
        node = self.dummy_head.next
        for _ in range(index):
            node = node.next
        return node

    def display(self):
        print(f"size = {self.size}")
        p = self.dummy_head.next
        while p != self.dummy_tail:
            print(f"{p.val} <-> ", end="")
            p = p.next
        print("null\n")




if __name__ == "__main__":
    list = LinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    #删
    # list.remove_first()
    # list.remove_last()
    # list.remove(2)

    #查
    # print(list.get(4))

    #改
    list.set(2,200)

    list.display()


