from pythonds.basic.stack import Stack

def parChecker(symbolString):
    """符号匹配，原理与括号匹配差不多"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closer = ")]}"
    return opens.index(open) == closer.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{(}]'))