def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += pos
    
    return found

testlist = [1, 4, 6, 2, 4, 67, 123]
print(sequentialSearch(testlist, 4))
print(sequentialSearch(testlist, 13))