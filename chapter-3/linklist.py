class Node:
    """ 链表基本构造块-节点
    参数:
        initdata:
    属性:
        data:
        next:
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newnext):
        self.next = newnext

