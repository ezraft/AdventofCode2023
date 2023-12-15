# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]
VAL = 1000000

LEVEL = 2
SAMPLE_ANSWERS = [374, 82000210]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    M = len(A[0])
    print("N =", N)
    print(A[:10])
    gal = []

    # M = len(A[0])
    v = [0] * N
    q = [0] * M
    c = 0
    for i in range(N):
        ok = True
        for j in range(M):
            if A[i][j] != '.':
                ok = False
        if ok:
            c+=(VAL - 1)
        v[i] = c
        c +=1
    c = 0
    for j in range(M):
        ok = True
        for i in range(N):
            if A[i][j] != '.':
                ok = False
        if ok:
            c+=(VAL - 1)
        q[j] = c
        c +=1
    for i in range(N):
        for j in range(M):
            if A[i][j] != '.':
                gal.append((v[i], q[j]))

    ans = 0
    for i in range(len(gal)):
        print(gal[i][0], gal[i][1])
        for j in range(i + 1, len(gal)):
            ans = ans + abs(gal[i][0] - gal[j][0]) + abs(gal[i][1] - gal[j][1])

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
    assert submit_answer(2023, 11, LEVEL, answer) is True


if __name__ == '__main__':
    main()