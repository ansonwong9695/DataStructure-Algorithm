class MyArrayList:
    def __init__(self,init_capacity= None):
        self.data = [None] * (init_capacity if init_capacity is not None else 1)
        # 这个 size 是列表当中，已有元素的数量
        self.size = 0
    #增
    # add last
    def add_last(self,e):
        """
        :param e: 添加的元素
        """
        #1. 检查列表大小，不够的话扩容
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap*2)

        #2. 插入在size 位置
        self.data[self.size] = e
        self.size += 1

    # add first
    def add_first(self,e):
        """
        :param e:添加元素
        """
        #1. 判断，列表大小，不行就扩容
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap*2)
        #2. 够的话， 腾挪列表，让出第一个位置
        for i in range(self.size,0,-1):
            self.data[i]= self.data[i-1]
        #3. 添加元素
        self.data[0] = e
        self.size += 1

    # add, 添加任何指定位置
    def add(self,index,e):
        """
        :param index:
        :param e:
        :return:
        """
        # 1. 判断大小
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap*2)
        # 2. 根据 index 腾挪，index 后面的位置
        for i in range(self.size,index,-1):
            self.data[i] = self.data[i-1]
        #3. 插入数据,size 增加
        self.data[index] = e
        self.size += 1

    # 删
    # del first
    def del_first(self,e):
        pass

    # del last
    def del_last(self,e):
        #1. 检查列表大小，如果 None 占据了列表 3/4 的时候，缩容

        #2. 删除最后一个元素，size-1

    #改
    # set

    #查
    # get

    #工具函数
    def _resize(self,new_cap):
        new_data = [None] * new_cap
        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data




if __name__ == '__main__':
    myarray = MyArrayList()
    myarray.add_last(12)
    myarray.add_last(13)
    myarray.add_last(14)
    myarray.add_last(15)
    myarray.add_first(1)
    myarray.add_first(0)
    myarray.add_first(-1)
    # myarray.add_last(16)
    print(myarray.data)
    myarray.add(3,333)
    myarray.add(4,444)

    print(myarray.size)
    print(myarray.data)
