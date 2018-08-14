def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startpotision in range(sublistcount):
            gapInsertionSort(alist, startpotision, sublistcount)
        print("After increments of size",sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        
        alist[position] = currentValue
alist = [54,26,93,17,77,31, 22,44,55,20]
shellSort(alist)
print(alist)