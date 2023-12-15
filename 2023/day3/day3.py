# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [4361, 467835]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    print("N =", N)
    # print(A[:10])
    # M = len(A[0])
    ans = 0
    d = {}
    sm = {}
    for i in range(N):
        M = len(A[i])
        mx = 0
        for j in range(M):
            j = max(j, mx)
            if j >= M:
                break
            if A[i][j] >= '0' and A[i][j] <= '9':
                ok = -1
                for x in range(8):
                    if i + chr[x] >= 0 and i + chr[x] < N and j + chc[x] >= 0 and j + chc[x] < M and A[i + chr[x]][j + chc[x]] != '.' and (A[i + chr[x]][j + chc[x]] == '*'):
                        ok = N * (i + chr[x]) + (j + chc[x])
                if ok != -1:
                    s = A[i][j]
                    k = j
                    while k - 1 >= 0 and A[i][k-1] >= '0' and A[i][k - 1] <= '9':
                        s = A[i][k-1] + s
                        k = k - 1
                    k = j
                    while(k + 1 < M and A[i][k + 1] >= '0' and A[i][k + 1] <= '9'):
                        s += A[i][k + 1]
                        k += 1
                    mx = max(k + 1, mx)
                    if not (ok in d.keys()):
                        d[ok] = 0
                    d[ok] = d[ok] + 1
                    if not (ok in sm.keys()):
                        sm[ok] = 1
                    sm[ok] = sm[ok] * int(s)
                    print(ok)
                    print(d[ok])
                    print(sm[ok])
                    print(s)
    # for i in range(N):
    for key in d.keys():
        if d[key] == 2:
            ans = ans + sm[key]
    if LEVEL == 1:
        return ans
    else:
        return ans


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
    assert submit_answer(2023, 3, LEVEL, answer) is True


if __name__ == '__main__':
    main()