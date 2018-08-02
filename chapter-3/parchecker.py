from pythonds.basic.stack import Stack

def parChecker(symbolString):
    """括号匹配
    在数学运算里面，括号必须以匹配的方式出现，比如(1 + 1) * 2，
    ()是匹配的，解决方法是把(作为判断条件，如果括号为'('则入栈,
    为')'则出栈，如果最后栈为空则证明括号匹配
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif symbol == ")":
                s.pop()
        
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('()))'))
print(parChecker('((1))'))