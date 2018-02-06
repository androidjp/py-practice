print('===================================')
print('[排序]')
print('--------------')

l = sorted([3, 1, -1, 0, 1, 9, 7])
print(l)

l2 = sorted([-1, -2, -3, -4])
print(l2)
l2 = sorted([-1, -2, -3, -4], key=abs)
print(l2)

print(sorted(['a', 'C', 'B'], key=str.lower))

print('===================================')
print('[反向排序]')
print('--------------')

print(sorted(['a', 'C', 'B'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(stu):
    return str.lower(stu[0])
def by_score(stu):
    return stu[1]


print(sorted(L, key=by_name))
print(sorted(L, key=by_score , reverse=True))

