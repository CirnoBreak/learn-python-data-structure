from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    """烫手山芋问题
    类似于约瑟夫问题，游戏规则是孩子们围成一个圈，
    然后从队首开始报数，报到指定数字的孩子出局，
    最后只剩下一个人
    参数:
        namelist: 参与游戏的孩子人名的列表
        num: 报数的数字
    返回值:
        simqueue.dequeue(): String
            胜出的孩子
    """
    simqueue = Queue()

    # 把所有人名放进队列
    for name in namelist:
        simqueue.enqueue(name)

    # 当队列人数大于1的时候执行，因为每一轮报数都会有一个人出队，长度-1
    while simqueue.size() > 1:
        # 每一次报数过程中，队首的人出队然后重新进队
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        # 每一轮报数完后队首的人出队，队列长度-1
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))