# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]
pos = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

LEVEL = 2
SAMPLE_ANSWERS = [142, 281]
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
    for i in range(N):
        fir = 0
        en = 0
        for j in range(len(A[i])):
            if A[i][j] >= '1' and A[i][j] <= '9':
                if fir == 0:
                    fir = ord(A[i][j]) - ord('0')
                en = ord(A[i][j]) - ord('0')
            elif j + 4 <= len(A[i]) and A[i][j:j+5] in pos:
                for k in range(len(pos)):
                    if pos[k] == A[i][j:j+5]:
                        print("here")
                        if fir == 0:
                            fir = k + 1
                        en = k + 1
            elif j + 3 <= len(A[i]) and A[i][j:j+4] in pos:
                for k in range(len(pos)):
                    if pos[k] == A[i][j:j+4]:
                        if fir == 0:
                            fir = k + 1
                        en = k + 1
            elif j + 2 <= len(A[i]) and A[i][j:j+3] in pos:
                for k in range(len(pos)):
                    if pos[k] == A[i][j:j+3]:
                        if fir == 0:
                            fir = k + 1
                        en = k + 1
        print(10*fir+en)
        ans += 10 * fir + en

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
    assert submit_answer(2023, 1, LEVEL, answer) is True


if __name__ == '__main__':
    main()