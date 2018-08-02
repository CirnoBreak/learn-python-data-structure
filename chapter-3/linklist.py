class Node:
    """ 链表基本构造块-节点
    参数:
        initdata
    属性:
        data: 当前节点数据
        next: 当前节点的下一个指向
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

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """表头引用head为None则链表为空"""
        return self.head == None

    def add(self, item):
        """链表的头部为链表的入口点，访问其他节点只能从第一个节点开始搜索，
        一直跟随下一个节点搜索，即最简单的方法是在链表头部添加。
        第一个添加的节点会成为链表最后一个节点，因为每一个节点都在它前面添加。
        temp.setNext(self.head)不能在self.head = temp之后执行，
        因为head是链表节点的唯一外部引用，如果这样做所有原始节点将会丢失并且不能访问。
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """从链表头部开始寻找，next不为None(链表尾部)的情况记数+1"""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count

    def search(self, item):
        """从链表头部开始寻找对应元素"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found

    def remove(self, item):
        """在删除节点的时候，链表需要两个外部引用。
        current依然是当前节点的引用，而previous是current前一个节点的引用，初始值为None。
        在执行搜索删除节点过程中，previous和current都会跟随移动，当找到对应节点的时候，
        (当前节点的)previous的引用会变成(当前节点的)next，从而完成删除操作
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList:
    def __init__(self):
        self.head = None
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
            
            return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

mylist = UnorderedList()

mylist.add(1)
mylist.add(3)

mylist.add(6213)
print(mylist.search(2))
mylist.remove(3)
print(mylist.size())