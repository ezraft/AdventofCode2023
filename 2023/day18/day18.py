# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [62, 952408144115]
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
    dir = [1, 2, 3, 0]
    c = (0,0)
    coords = [c]
    ans = 0
    for i in range(N):
        B = A[i].split(" ")
        print(B)
        B[2] = B[2][1:-1]
        print(B[2])
        v = int(B[2][1:6], 16)
        q = dir[int(B[2][6])]
        print(v, q)
        cur = (c[0], c[1])
        c = (c[0] + chr[q] * v, c[1] + chc[q] * v)
        ans = (ans + abs(cur[0] - c[0]) + abs(cur[1] - c[1]))
        coords.append(c)
    ans=ans//2+1
    sm = 0
    sm2 = 0
    print(len(coords), N)
    for i in range(len(coords)-1):
        print(coords[i])
        sm = sm + coords[i][0] * coords[(i + 1) % len(coords)][1]
        sm2 = sm2 + coords[i][1] * coords[(i + 1) % len(coords)][0]
    ans = ans + abs(sm - sm2) // 2

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
    assert submit_answer(2023, 18, LEVEL, answer) is True


if __name__ == '__main__':
    main()