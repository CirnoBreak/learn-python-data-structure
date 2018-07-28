from pythonds.basic.deque import Deque

def palchecker(aString):
    """回文判断
    参数:
        aString: String
            回文字符串
    返回值:
        stillEqual: bool
            是否为回文字符串，True则是，False则不是
    """
    chardeque = Deque()

    # 把回文字符串存放到双端队列
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    # 在双端队列长度大于1时(因为要每次移除队首跟队尾做判断，而回文长度是奇数的时候最后会剩下一个，此时不做操作)
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    
    return stillEqual

print(palchecker('sdfnnkfds'))
print(palchecker('abba'))