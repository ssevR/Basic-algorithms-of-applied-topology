import numpy as np

def rank_mod2(a, l):
    #m < n
    m = a.shape[0]
    n = a.shape[1]
    res = 0
    for i in range(n):
        flag = 0
        for j in range(res, m):
            if (a[j][i] == 1):
                a[[res, j]] = a[[j, res]]
                flag = 1
                l.append(i)
                break
        if flag:
            for j in range(m):
                if a[j][i] == 1 and j != res:
                    a[j] ^= a[res]
            res += 1
    return res


def is_independent(a):
    return np.linalg.det(np.matrix(a)) % 2 != 0

v = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            if i > 0 or j > 0 or k > 0:
                v.append([i, j, k])

#z = np.matrix(z)

simp_3 = []
simp_2 = [] 


for mask in range(2 ** 7):
    ones = []
    for k in range(7):
        if ((mask >> k) & 1) > 0:
            ones.append(k)
    if len(ones) == 3 and is_independent(np.matrix([v[ones[0]], v[ones[1]], v[ones[2]]])):
        simp_3.append({ones[0], ones[1], ones[2]})

for i in range(7):
    for j in range(i + 1, 7):
        simp_2.append({i, j})

b = np.zeros((len(simp_2), len(simp_3)), dtype=int)

for i in range(len(simp_2)):
    for j in range(len(simp_3)):
        flag = 0
        for x in simp_2[i]:
            if x not in simp_3[j]:
                flag = 1

        if not flag:
            b[i][j] = 1

a = np.zeros((7, len(simp_2)), dtype=int)

for i in range(7):
    for j in range(len(simp_2)):
        if i in simp_2[j]:
            a[i][j] = 1
l1 = []
l2 = []
print('Ранг матрица A:', rank_mod2(a, l1))
print('Ранг матрица B:', rank_mod2(b, l2))
print('Количество независимых троек:', len(simp_3))
