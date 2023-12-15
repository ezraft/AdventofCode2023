# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]
MAX = 1000000000

LEVEL = 2
SAMPLE_ANSWERS = [136, 64]
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

    Q = []
    for cur in range(MAX):
        print(cur)
        B = []
        for i in range(N):
            B.append([])
            for j in range(M):
                B[-1].append(A[i][j])
        q = False
        for p in range(len(Q)):
            ok = True
            for i in range(N):
                for j in range(M):
                    if B[i][j] != Q[p][i][j]:
                        ok = False
            if ok:
                print(cur)
                print(p)
                print(len(Q))
                A = Q[p + (MAX-p) % (len(Q) - p)]
                q = True
                break
        if q:
            break
        Q.append(B)
        for i in range(N):
            for j in range(M):
                if (A[i][j] == 'O'):
                    c = i
                    while c - 1 >= 0 and A[c-1][j] == '.':
                        A[c-1] = A[c-1][:j] + 'O' + A[c-1][j + 1:]
                        A[c] = A[c][:j] + '.' + A[c][j + 1:]
                        c = c - 1
        for j in range(M):
            for i in range(N):
                if (A[i][j] == 'O'):
                    c = j
                    while c - 1 >= 0 and A[i][c-1] == '.':
                        A[i] = A[i][:c-1] + 'O' + '.' + A[i][c+1:]
                        c = c - 1

        for i in range(N-1, -1, -1):
            for j in range(M):
                if (A[i][j] == 'O'):
                    c = i
                    while c + 1 < N and A[c+1][j] == '.':
                        A[c+1] = A[c+1][:j] + 'O' + A[c+1][j + 1:]
                        A[c] = A[c][:j] + '.' + A[c][j + 1:]
                        c = c + 1

        for j in range(M - 1, -1, -1):
            for i in range(N):
                if (A[i][j] == 'O'):
                    c = j
                    while c + 1 < M and A[i][c+1] == '.':
                        A[i] = A[i][:c] + '.' + 'O' + A[i][c+2:]
                        c = c + 1
        # for i in range(N):
        #     print(A[i])
        # print()
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 'O':
                ans = ans + (N - i)
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
    assert submit_answer(2023, 14, LEVEL, answer) is True


if __name__ == '__main__':
    main()