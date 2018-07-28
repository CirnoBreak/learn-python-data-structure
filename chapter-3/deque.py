class Deque:
    """ 双端队列
    属性:
        items: list
            双端队列的列表
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """判断是否为空"""
        return self.items == []
    
    def addFront(self, item):
        """往队首添加元素"""
        self.items.append(item)
    
    def addRear(self, item):
        """往队尾添加元素"""
        self.items.insert(0, item)
    
    def removeFront(self):
        """移除队首元素"""
        return self.items.pop()
    
    def removeRear(self):
        """移除队尾元素"""
        return self.items.pop(0)
    
    def size(self):
        """获取双端队列长度"""
        return len(self.items)
