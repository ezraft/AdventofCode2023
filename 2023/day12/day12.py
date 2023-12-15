# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [21, 525152]
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

    ans = 0
    for i in range(N):
        print(i)
        # print(A[i].split()[0])
        B = A[i].split()[0]
        B = (5 * (B + '?'))[:-1]
        C = [int(x) for x in (A[i].split(" ")[1]).split(",")]
        C = (5 * C)
        C.append(1)
        print(B)
        print(C)
        M = len(B)
        Q = len(C)
        dp = [[]] * (M + 1)

        for j in range(M + 1):
            dp[j] = [[]] * (Q + 1)
            for k in range(0, Q + 1):
                if k == 0:
                    dp[j][k] = [[]] * 1
                    dp[j][k][0] = [0] * 2
                else:
                    dp[j][k] = [[]] * (C[k-1] + 1)
                    for q in range(C[k-1]):
                        dp[j][k][q] = [0] * 2
        # print(len(dp))
        # print(len(dp[0]))
        # print(len(dp[0][0]))
        dp[0][0][0][0] = 1
        for j in range(M):
            for k in range(Q):
                q = 1
                if k != 0:
                    q = C[k-1]
                for z in range(q):
                    # assert(dp[5][3][2][1] == 0)
                    # if dp[j][k][z] != 0:
                        # print("setup: ", j, k, z, dp[j][k][z])
                    # print(B[j])
                    # print(j, k, z, dp[j][k][z])
                    if B[j] == '.' or B[j] == '?':
                        # print("here")
                        dp[j + 1][k][z][0] += (dp[j][k][z][0] + dp[j][k][z][1])

                    if B[j] == '#' or B[j] == '?':
                        if k == Q and z == C[k-1]:
                            continue

                        if k == 0 or z + 1 == C[k-1]:
                            # print("here")
                            # print(j + 1, k + 1, 0, dp[j][k][z][0], "here")
                            # print(len(dp[5][3]))
                            dp[j + 1][k + 1][0][1] += dp[j][k][z][0]
                            # assert (dp[5][3][2][1] == 0)
                            # print("woo")
                        else:
                            # print(j + 1, k, z + 1, dp[j][k][z][1], "here")

                            dp[j + 1][k][z + 1][1] += dp[j][k][z][1]

        # print(dp[M][Q-1][C[-2]-1][0] + dp[M][Q-1][C[-2]-1][1])
        ans = ans + dp[M][Q-1][C[-2]-1][0] + dp[M][Q-1][C[-2]-1][1]

    # M = len(A[0])

    # for i in range(N):


    # for i in range(N):

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
    assert submit_answer(2023, 12, LEVEL, answer) is True


if __name__ == '__main__':
    main()