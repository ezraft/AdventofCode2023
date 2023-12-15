# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [114, 2]
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
    ans = 0
    for i in range(N):
        c = [[int(line) for line in reversed(A[i].split())]]
        while True:
            c.append([])
            ok = True
            for j in range(len(c[-2]) - 1):
                c[-1].append(-c[-2][j + 1] + c[-2][j])
                if c[-1][-1] != 0:
                    ok = False
            if ok:
                break

        for k in range(1, len(c)):
            z = len(c) - k
            c[z - 1].append(-c[z][-1] + c[z - 1][-1])
        print(c)
        print(c[0][-1])
        ans = ans + c[0][-1]
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
    assert submit_answer(2023, 9, LEVEL, answer) is True


if __name__ == '__main__':
    main()