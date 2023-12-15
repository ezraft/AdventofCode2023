# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [35, 46]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    N = len(A)
    print("N =", N)
    seeds1 = [int(line) for line in A[0][7:].split(" ")]
    seeds = []
    for i in range(0, len(seeds1), 2):
        seeds.append([seeds1[i], seeds1[i] + seeds1[i + 1] - 1])
    vis = [0] * len(seeds)
    for i in range(1, N):
        if A[i] == "" or A[i][0].isalpha():
            vis = [0] * len(seeds)
            continue
        b, a, c = [int(line) for line in A[i].split(" ")]
        print(a)
        print(a + c)
        for k in range(len(seeds)):
            if vis[k] != 0 or seeds[k][0] == -1:
                continue
            ok = 0
            if seeds[k][0] < a and seeds[k][1] >= a + c:
                seeds.append([seeds[k][0], a - 1])
                seeds.append([b, b + c - 1])
                vis[k] = 1
                seeds.append([a + c, seeds[k][1]])
                vis.append(0)
                vis.append(1)
                vis.append(0)
                ok = 1
            if seeds[k][0] >= a and seeds[k][1] < a + c:
                vis[k] = 1
                seeds.append([b + seeds[k][0] - a, b + seeds[k][1] - a])
                vis.append(1)
                ok = 1
            if seeds[k][0] >= a and seeds[k][0] < a + c and seeds[k][1] >= a + c:
                ok = 1
                vis[k] = 1
                seeds.append([b + seeds[k][0] - a, b + c - 1])
                seeds.append([a + c, seeds[k][1]])
                vis.append(1)
                vis.append(0)
            if seeds[k][0] < a and seeds[k][1] >= a and seeds[k][1] < a + c:
                ok = 1
                vis[k] = 1
                seeds.append([seeds[k][0], a - 1])
                seeds.append([b, b + seeds[k][1] - a])
                vis.append(0)
                vis.append(1)
            if ok:
                seeds[k][0] = -1
        for k in seeds:
            print(k)
        print("")
    # M = len(A[0])
    seeds.sort()
    ans = 1e18
    for e in seeds:
        if e[0] != -1 and e[1] > e[0]:
            ans = min(ans, e[0])
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
    assert submit_answer(2023, 5, LEVEL, answer) is True


if __name__ == '__main__':
    main()