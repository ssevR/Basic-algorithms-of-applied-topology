import numpy as np

def rank_mod2(a, l):
    #m < n+
    m = a.shape[0]
    n = a.shape[1]
    res = 0
    for i in range(m):
        flag = 0
        for j in range(i, m):
            if a[j][i] == 1:
                res += 1
                a[[i, j]] = a[[j, i]] 
                l.append(i)
                flag = 1 
                break
        if flag:
            for j in range(i + 1, m):
                if a[j][i] == 1:
                    a[j] ^= a[i]
    return res


a = np.zeros((5, 10), dtype=int)

e = []

for i in range(5):
    for j in range(i + 1, 5):
        e.append([i, j]);



for i in range(0, 5):
    for j in range(10):
        if i == e[j][0] or i == e[j][1]:
            a[i][j] = 1

b = np.zeros((10, 10), dtype=int)
trig = []
def is_in(a, b):
    return a[0] in b and a[1] in b

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            trig.append({i, j, k})

for i in range(10):
    for j in range(10):
        if is_in(e[i], trig[j]):
            b[i][j] = 1


l1 = []
l2 = []
print('Ранг матрица A:', rank_mod2(a, l1))
print('Ранг матрицы B:', rank_mod2(b, l2))
