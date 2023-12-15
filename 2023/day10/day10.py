# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer


MAX = 1000
#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [4, 52]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    N = len(A)
    adj = {}
    val = {}
    val['|'] = [1 ,1 ,0, 0]  # NSEW
    val['-'] = [0, 0, 1, 1]  # NSEW
    val['L'] = [1, 0, 1, 0]  # NSEW
    val['J'] = [1, 0, 0, 1]  # NSEW
    val['7'] = [0, 1, 0, 1]  # NSEW
    val['F'] = [0, 1, 1, 0]  # NSEW
    val['.'] = [0, 0, 0, 0]  # NSEW
    q = [[-1, 0], [1, 0], [0, 1], [0,-1]]
    for i in range(N):
        for j in range(len(A[i])):
            adj[MAX * i + j] = []
    st = (0, 0)
    for i in range(N):
        for j in range(len(A[i])):
            if A[i][j] == 'S':
                st =(i,j)
                continue
            for x in range(4):
                if val[A[i][j]][x] == 1:
                    if i + q[x][0] >= 0 and i + q[x][0] < N and j + q[x][1] >= 0 and j + q[x][1] < len(A[i]):
                        adj[MAX * i + j].append((i + q[x][0], j + q[x][1]))
                        print(i, j, adj[MAX * i + j][-1])
                        if (A[i + q[x][0]][j + q[x][1]] == 'S'):
                            adj[MAX * (i + q[x][0]) + (j + q[x][1])].append((i,j))


    cur = adj[st[0] * MAX + st[1]][1]
    pre = st
    curln = 1
    print(st)
    good = set()
    good.add(st)
    while cur != st:
        print(cur)
        print(len(adj[cur[0] * MAX + cur[1]]))
        for current in adj[cur[0] * MAX + cur[1]]:
            print(current)
        print("done")
        assert(len(adj[cur[0] * MAX + cur[1]]) == 2)
        good.add(cur)
        if adj[cur[0] * MAX + cur[1]][0] == pre:
            pre = cur
            cur = adj[cur[0] * MAX + cur[1]][1]
        else:
            pre = cur
            cur = adj[cur[0] * MAX + cur[1]][0]
        curln += 1
    ins = 2 #NSEW
    cur = adj[st[0] * MAX + st[1]][1]
    pos = set()
    pre = st
    while cur != st:
        if cur[0] + q[ins][0] >= 0 and cur[0] + q[ins][0] < N and cur[1] + q[ins][1] >= 0 and cur[1] + q[ins][1] < len(A[i]) and (cur[0] + q[ins][0], cur[1] + q[ins][1]) not in good:
            pos.add((cur[0] + q[ins][0], cur[1] + q[ins][1]))
        tmp = A[cur[0]][cur[1]]
        print(ins)
        if tmp == 'L' or tmp == '7':
            if ins == 3:
                ins = 1
            elif ins == 1:
                ins = 3
            elif ins == 2:
                ins = 0
            elif ins == 0:
                ins = 2
        if tmp == 'J' or tmp == 'F':
            if ins == 3:
                ins = 0
            elif ins == 0:
                ins = 3
            elif ins == 2:
                ins = 1
            elif ins == 1:
                ins = 2
        if cur[0] + q[ins][0] >= 0 and cur[0] + q[ins][0] < N and cur[1] + q[ins][1] >= 0 and cur[1] + q[ins][1] < len(A[i]) and (cur[0] + q[ins][0], cur[1] + q[ins][1]) not in good:
            pos.add((cur[0] + q[ins][0], cur[1] + q[ins][1]))
        if adj[cur[0] * MAX + cur[1]][0] == pre:
            pre = cur
            cur = adj[cur[0] * MAX + cur[1]][1]
        else:
            pre = cur
            cur = adj[cur[0] * MAX + cur[1]][0]
        if cur[0] + q[ins][0] >= 0 and cur[0] + q[ins][0] < N and cur[1] + q[ins][1] >= 0 and cur[1] + q[ins][1] < len(A[i]) and (cur[0] + q[ins][0], cur[1] + q[ins][1]) not in good:
            pos.add((cur[0] + q[ins][0], cur[1] + q[ins][1]))
    print("N =", N)
    print(A[:10])
    # M = len(A[0])

    for i in range(N + len(A[0])):
        print(i, N)
        for j in range(N):
            for k in range(len(A[j])):
                if (j, k) in pos:
                    continue
                for v in q:
                    if j + v[0] >= 0 and j + v[0] < N and k + v[1] >= 0 and k + v[1] < len(A[j]) and ((j + v[0], k + v[1]) in pos) and (not ((j,k) in good)):
                        # print(j + v[0], k + v[1], j, k)
                        pos.add((j, k))
                        break

    for i in range(N):
        mp = ""
        for j in range(len(A[i])):
            if (i, j) in good:
                mp += A[i][j]
            elif (i, j) in pos:
                mp += 'I'
            else:
                mp += '.'
        print(mp)
    print(len(pos))

    if LEVEL == 1:
        return 3
    else:
        return len(pos)


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read().strip('\n')
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"

    with open("input.txt") as input_file:
        inp = input_file.read().strip('\n')
    answer = solve(inp)
    print("Answer:", answer)
    assert submit_answer(2023, 10, LEVEL, answer) is True


if __name__ == '__main__':
    main()