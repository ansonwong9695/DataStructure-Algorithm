"""
动态数组关键点
1. 自动扩容 缩容，当 size 和 数组一样大时候扩容两倍，如果size 等于 数组尺寸//4 缩容一半
2. 检查索引越界否
3. 模拟防止内存泄露，给删除的值赋予 none
"""

import copy


class MyArrayList:
    INIT_CAP = 1

    def __init__(self,init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0

    #增
    #增尾
    def add_last(self,element):
        # 1. 测量大小
        cap = len(self.data)
        # 2. 判断容量够不够
        if cap == self.size :
            # 扩容
            self._resize(2*cap)
        # 3. 添加元素在末尾,size+1
        self.data[self.size] = element
        self.size += 1

    #随处增
    def add(self,index,element):
        # 1. 查看index 是不是在区间
        self._check_position_index(index)
        # 2. 判断数组大小，是否扩容
        cap = len(self.data)
        if cap == self.size:
            self._resize(cap*2)
        # 3. 搬迁元素给插入元素留下空间
        tmp_list = copy.deepcopy(self.data)
        for i in range(self.size-1,index-1,-1):
            self.data[i+1] = tmp_list[i]
        # 4. 插入元素
        self.data[index] = element
        self.size += 1

    #增加在头部
    def add_first(self,element):
        self.add(0,element)

    #删除
    #删除最后一个
    def del_last(self):
        # 1.检查 size，如果0数组不存在
        if self.size == 0:
            raise StopIteration
        # 2.看看是否要缩容
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap//2)
        # 3.删除元素
        del_index = self.size - 1
        deleted_val = self.data[del_index]
        self.data[self.size-1] = None

        self.size -= 1

        return deleted_val

    #删除
    def del_ele(self,index):
        # 1.检查 index 在不在范围内
        self._check_element_index(index)
        # 2.看是否要缩容
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap//2)
        # 3.搬迁元素，删除元素

        for i in range(index,self.size):
            self.data[i] = self.data[i+1]

        self.size -= 1

    #删除第一个
    def del_first(self):
        self.del_ele(0)

    #获取
    def get_ele(self,index):
        # 1. 判断索引是否越界
        self._check_element_index(index)
        # 2. 获取元素
        return self.data[index]

    #修改
    def set_ele(self,index,element):
        #1.判断索引是否越界
        self._check_element_index(index)
        #2.修改元素
        old_element = self.data[index]
        self.data[index] = element
        return old_element


    #工具函数
    def _resize(self,new_cap):
        # 1. 创建一个新的 cap 数组
        temp_arr = [None] * new_cap
        # 2. 搬迁数据从旧的
        for index,values in enumerate(self.data):
            temp_arr[index] = values
        # 3. self.data 替换成新的数组
        self.data = temp_arr

    def _check_position_index(self,index):
        # 如果不在范围 报错
        if not self.is_position_index(index):
            raise IndexError(f" Index {index}, Size: {self.size}")

    def _check_element_index(self,index):
        # 如果不在范围 报错
        if not self.is_element_index(index):
            raise IndexError(f" Index {index}, Size: {self.size}")


    def is_position_index(self,index):
        return 0 <= index  <= self.size

    def is_element_index(self,index):
        return 0 <= index  < self.size

if __name__ == '__main__':
    #测试 add
    my_array = MyArrayList()
    my_array.add_last(1)
    my_array.add_last(2)
    my_array.add_last(3)
    my_array.add(1,1.5)
    my_array.add(0,0)
    # my_array.add_first(0)
    print(my_array.data)
    #测试 del
    my_array.del_last()
    my_array.del_ele(3)
    my_array.del_first()
    print(my_array.data)
    print(my_array.get_ele(0))
    my_array.set_ele(0,1.1)
    print(my_array.data)







