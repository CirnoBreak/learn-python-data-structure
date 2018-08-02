from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    """十进制转其他(2-16)进制，原理与十进制转二进制差不多"""
    digits = "0123456789ABCDEF"

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
    
    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))