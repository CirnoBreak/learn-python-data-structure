from pythonds.basic.stack import Stack

def dividedby2(decNumber):
    """十进制转二进制
    把要转换的数字除以2得到的余数压入栈，得到的商向下取整作为循环的条件
    最后把栈里面的数字通过不断出栈做字符串连接操作最后得到二进制字符串
    """
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())

    return binString

print(dividedby2(42))
