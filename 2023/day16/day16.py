# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [46, 51]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    print("N =", N)
    print(A[:10])
    M = len(A[0])
    fin = 0
    for z in range(N):
        c = [(z,-1, 1)]
        vis = [[[0 for k in range(4)] for j in range(M)] for i in range(N)]
        cnt = 0
        while len(c) > 0:
            cur = c[0]
            if cur[1] != -1 and vis[cur[0]][cur[1]][cur[2]]:
                c = c[1:]
                continue
            if cur[1] != -1:
                vis[cur[0]][cur[1]][cur[2]] = 1
            if cur[0] + chr[cur[2]] >= 0 and cur[0] + chr[cur[2]] < N and cur[1] + chc[cur[2]] >= 0 and cur[1] + chc[cur[2]] < M:
                q = A[cur[0] + chr[cur[2]]][cur[1] + chc[cur[2]]]
                if q == '.':
                    c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '-':
                    if cur[2] == 0 or cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '|':
                    if cur[2] == 1 or cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '/':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                elif q == '\\':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
            c = c[1:]
        ans = 0
        for i in range(N):
            s = ""
            for j in range(M):
                total = 0
                for x in vis[i][j]:
                    if x != 0:
                        total = 1
                s = s + str(total)
                ans = ans + total
        fin = max(fin, ans)

    for z in range(N):
        c = [(z,M, 3)]
        vis = [[[0 for k in range(4)] for j in range(M)] for i in range(N)]
        cnt = 0
        while len(c) > 0:
            cur = c[0]
            if cur[1] != M and vis[cur[0]][cur[1]][cur[2]]:
                c = c[1:]
                continue
            if cur[1] != M:
                vis[cur[0]][cur[1]][cur[2]] = 1
            if cur[0] + chr[cur[2]] >= 0 and cur[0] + chr[cur[2]] < N and cur[1] + chc[cur[2]] >= 0 and cur[1] + chc[cur[2]] < M:
                q = A[cur[0] + chr[cur[2]]][cur[1] + chc[cur[2]]]
                if q == '.':
                    c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '-':
                    if cur[2] == 0 or cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '|':
                    if cur[2] == 1 or cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '/':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                elif q == '\\':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
            c = c[1:]
        ans = 0
        for i in range(N):
            s = ""
            for j in range(M):
                total = 0
                for x in vis[i][j]:
                    if x != 0:
                        total = 1
                s = s + str(total)
                ans = ans + total
        fin = max(fin, ans)

    for z in range(M):
        c = [(-1,z, 2)]
        vis = [[[0 for k in range(4)] for j in range(M)] for i in range(N)]
        cnt = 0
        while len(c) > 0:
            cur = c[0]
            if cur[0] != -1 and vis[cur[0]][cur[1]][cur[2]]:
                c = c[1:]
                continue
            if cur[0] != -1:
                vis[cur[0]][cur[1]][cur[2]] = 1
            if cur[0] + chr[cur[2]] >= 0 and cur[0] + chr[cur[2]] < N and cur[1] + chc[cur[2]] >= 0 and cur[1] + chc[cur[2]] < M:
                q = A[cur[0] + chr[cur[2]]][cur[1] + chc[cur[2]]]
                if q == '.':
                    c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '-':
                    if cur[2] == 0 or cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '|':
                    if cur[2] == 1 or cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '/':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                elif q == '\\':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
            c = c[1:]
        ans = 0
        for i in range(N):
            s = ""
            for j in range(M):
                total = 0
                for x in vis[i][j]:
                    if x != 0:
                        total = 1
                s = s + str(total)
                ans = ans + total
        fin = max(fin, ans)

    for z in range(M):
        c = [(N,z, 0)]
        vis = [[[0 for k in range(4)] for j in range(M)] for i in range(N)]
        cnt = 0
        while len(c) > 0:
            cur = c[0]
            if cur[0] != N and vis[cur[0]][cur[1]][cur[2]]:
                c = c[1:]
                continue
            if cur[0] != N:
                vis[cur[0]][cur[1]][cur[2]] = 1
            if cur[0] + chr[cur[2]] >= 0 and cur[0] + chr[cur[2]] < N and cur[1] + chc[cur[2]] >= 0 and cur[1] + chc[cur[2]] < M:
                q = A[cur[0] + chr[cur[2]]][cur[1] + chc[cur[2]]]
                if q == '.':
                    c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '-':
                    if cur[2] == 0 or cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '|':
                    if cur[2] == 1 or cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                    else:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], cur[2]))
                elif q == '/':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
                elif q == '\\':
                    if cur[2] == 0:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 3))
                    if cur[2] == 3:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 0))
                    if cur[2] == 2:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 1))
                    if cur[2] == 1:
                        c.append((cur[0] + chr[cur[2]], cur[1] + chc[cur[2]], 2))
            c = c[1:]
        ans = 0
        for i in range(N):
            s = ""
            for j in range(M):
                total = 0
                for x in vis[i][j]:
                    if x != 0:
                        total = 1
                s = s + str(total)
                ans = ans + total
        fin = max(fin, ans)
    if LEVEL == 1:
        return ans
    else:
        return fin


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
    assert submit_answer(2023, 16, LEVEL, answer) is True


if __name__ == '__main__':
    main()