import random as rand

def mat(a, b):
    mat_c = [len(mat_b[0]) * [0] for i in range(len(mat_a))]

    for i in range(len(mat_c)):
        for j in range(len(mat_c[i])):
            for k in range(len(mat_a[i])):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j]

    mat_t = [[0 for _ in range(len(mat_c))] for _ in range(len(mat_c[0]))]
    for i in range(len(mat_c)):
        for j in range(len(mat_c[0])):
            mat_t[j][i] = mat_c[i][j]


    return print(f'행렬의 곱: {mat_c},\n'
                 f'결과 행렬의 전치행렬: {mat_t}')



mat_a = [[rand.randint(1, 9) for _ in range(0,3)] for _ in range(0, 3)]
mat_b = [[rand.randint(1, 9) for _ in range(0,3)] for _ in range(0, 3)]
mat(mat_a, mat_b)

def marathon(p, c):
    for i in c:
        if i in p:
            p.remove(i)
    return p


count = 0
while count < 1:
    p = [x for x in input("enter name >> ").split()]
    c = [x for x in input("enter name >> ").split()]
    if len(p) - len(c) == 1:
            count += 1
    if True:
        for i in c:
            if i not in p:
                count = 0
                break

result = marathon(p,c)
print(f' 미완주자: {result}')


def st_sort(a, n):
    a.sort(key=lambda x: (x[n:n+1], x))

    return a

ct = 0
while ct < 1:
    ct2 = 0
    while ct2 < 1:
        num = int(input("입력할 문자열의 개수 >> "))
        if num >= 3 and num <= 10:
            ct2 += 1
    pb3 = [str(input("string >> ")).lower() for _ in range(num)]
    ct += 1
    for i in pb3:
        if len(i) < 2 or len(i) > 30:
            ct = 0
            break

print(st_sort(pb3, 1))