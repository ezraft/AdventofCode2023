# from collections import *
# from itertools import *
# from math import *
import math

from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [2, 6]
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
    # M = len(A[0])
    X = {}
    instr = A[0]
    for i in range(2, N):
        B = A[i].split()
        print(B[2][1:-1])

        X[B[0]] = [B[2][1:-1], B[3][:-1]]

    cur = []
    for x in X.keys():
        if x[-1] == 'A':
            cur.append(x)
    cnt = 0
    ans = 1
    tot = []

    for i in range(len(cur)):
        sm = 0
        while cur[i][-1] != 'Z':
            if instr[cnt] == 'L':
                cur[i] = X[cur[i]][0]
            else:
                cur[i] = X[cur[i]][1]
            print(cur[i][-1])
            cnt = (cnt + 1) % len(instr)
            sm = sm + 1
        tot.append(sm)
    # for i in range(N):
    for q in tot:
        print(q)
        ans = math.lcm(ans, q)

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
    assert submit_answer(2023, 8, LEVEL, answer) is True


if __name__ == '__main__':
    main()