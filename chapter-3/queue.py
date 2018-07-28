class Queue:
    """ 队列
    属性:
        items: list
            队列的列表
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """判断是否为空"""
        return self.items == []

    def enqueue(self, item):
        """进队，index为0的位置是队尾"""
        self.items.insert(0, item)

    def dequeue(self):
        """出队"""
        return self.items.pop()

    def size(self):
        """获取队列长度"""
        return len(self.items)
