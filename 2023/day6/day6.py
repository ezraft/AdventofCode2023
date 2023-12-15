# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [288, 71503]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    s = "Time: "
    t = "Distance: "
    B = [int(line) for line in A[0].replace(s, "").split(" ")]
    C = [int(line) for line in A[1].replace(t, "").split(" ")]
    N = len(B)
    print("N =", N)
    # M = len(A[0])
    ans = 1

    for i in range(N):
        cnt = 0
        for j in range(B[i] + 1):
            if (B[i] - j) * j > C[i]:
                cnt +=1
        ans = ans * cnt
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
    assert submit_answer(2023, 6, LEVEL, answer) is True


if __name__ == '__main__':
    main()