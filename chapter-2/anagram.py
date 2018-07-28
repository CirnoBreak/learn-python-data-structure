"""乱数字符串检查
乱数字符串指的是一个字符串是另一个字符串的重新排列,并且都是由26个小写字母的集合组成。
比如: 'heart'跟'earth'
特点: 他们的长度肯定是一样的
"""

def anagramSolution1(s1, s2):
    """方案1:检查,复杂度为O(n^2)
    先把第二个字符串转换成列表，然后检查第一个字符串中每一个元素是否存在于第二个列表，
    如果存在则把对应位置的替换成None，否则直接返回False
    参数:
        s1: 第一个字符串
        s2: 第二个字符串
    """
    # 把第二个字符串转成列表
    alist = list(s2)

    # 第一个字符串列表的当前位置
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        # 第二个字符串列表的当前位置
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            # 如果第一个列表里面的一个字符在第二个列表中找到则found返回True，否则继续
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        
        # 当found为True的时候把第二个列表对应位置的字符替换成None,否则直接跳出循环
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd', 'dcba'))
print(anagramSolution1('sdff', 'dddd'))

def anagramSolution2(s1, s2):
    """方案2:排序和比较, 复杂度为O(n)
    尽管s1与s2不一样，但是如果他们是乱数字符串的话，实际上他们是由完全相同的字符组成
    思路:首先把两个字符串都转成列表，并都进行字母排序，然后进行一对一对比
    参数:
        s1: String
            第一个字符串
        s2: String
            第二个字符串
    返回值:
        matches: bool
            是否匹配
    """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde', 'becda'))

def anagramSolution4(s1, s2):
    """解法4: 记数和比较, 复杂度为O(n)
    由于乱数字符串由26个小写字母的集合组成，
    所以把他们字符串中字母出现的次数放到一个长度为26的数组
    把对应位置的字符转成ASCII与小写a的ASCII相减得出该数组的index，并做对应的记数(+1)
    然后通过对比两个存放两个字符串字母出现次数的数组是否完全一样，完全一样则为乱数字符串
    参数:
        s1: String
            第一个字符串
        s2: String
            第二个字符串
    返回值:
        stillOK: bool
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True

    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    
    return stillOK

print(anagramSolution4('apple', 'pleap'))