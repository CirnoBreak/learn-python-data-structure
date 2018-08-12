def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midPoint = (first + last) // 2
        if alist[midPoint] == item:
            found = True
        else:
            if item < alist[midPoint]:
                last = midPoint - 1
            else:
                first = midPoint + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))