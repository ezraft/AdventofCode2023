# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [1320, 145]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.replace("\n", "").split(",")]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    print("N =", N)
    print(A[:10])
    # M = len(A[0])

    for i in range(N):
        print(A[i])
    ans = 0
    Q = [[] for i in range(256)]

    for i in range(N):
        print(A[i])
        if '=' in A[i]:
            B = A[i].split("=")
            # print(B)
            v = 0
            for x in B[0]:
                v = v + ord(x)
                v = v * 17
                v = v % 256
            # print(v)
            ok = False
            for i in range(len(Q[v])):
                if Q[v][i][0] == B[0]:
                    Q[v][i] = (B[0], B[1])
                    # print(v)
                    ok = True
                    break
            if not ok:
                Q[v].append((B[0], B[1]))
                # print(v)
        elif '-' in A[i]:
            B = A[i]
            B = B[:-1]
            print(B)
            v = 0
            for x in B:
                v = v + ord(x)
                v = v * 17
                v = v % 256
            # print(v)
            for e in range(len(Q[v])):
                # print(Q[v][e])
                if Q[v][e][0] == B:
                    # print(v)
                    Q[v] = Q[v][:e] + Q[v][e + 1:]
                    break

    for i in range(len(Q)):
        # print(len(Q[i]))
        for j in range(len(Q[i])):
             print(i + 1, j + 1, int(Q[i][j][1]))
             ans = ans + (i + 1) * (j + 1) * int(Q[i][j][1])
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
    assert submit_answer(2023, 15, LEVEL, answer) is True


if __name__ == '__main__':
    main()