import bisect


def find(seq, el):
    pos = bisect.bisect(seq, el)
    if pos == 0 or (pos == len(seq) and seq[-1] != el):
        return -1
    return pos - 1


list = [1, 2, 4, 5]

bisect.insort(list, 3)
print('快速插入一个元素\n', list)

print('快速搜索（对于一个排好序的列表，bisect会采用二分查找）\n', find(list, 4))
