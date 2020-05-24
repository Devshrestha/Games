a = [['a']*2]*2
b = [[0, 1], [1, 1]]
for x in range(len(b)):
    a[b[x][0]][b[x][1]] = '*'

print(a)
