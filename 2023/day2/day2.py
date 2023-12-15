# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [8, 2286]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    print("N =", N)
    ans = 0
    for val in A:
        B = val.replace("Game ", "")
        C = B.split(" ")
        id = C[0][:-1]
        C = C[1:]
        c = {}
        c["blue"] = c["green"] = c["red"] = 0
        ok = True
        for x in range(len(C)):
            if x % 2 == 0:
                ty = C[x + 1]
                if ty[-1] == ',' or ty[-1] == ';':
                    ty = ty[:-1]
                    # print(ty)
                c[ty] = max(c[ty], int(C[x]))

                # if ((ty == "blue" and int(C[x]) > 14) or (ty == "green" and int(C[x]) > 13) or (ty == "red" and int(C[x]) > 12)):
                #     ok = False
        # if ok:
        #     print(int(id))
        print(c["blue"])
        print(c["green"])
        print(c["red"])
        ans = ans + c["blue"] * c["green"] * c["red"]


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
    assert submit_answer(2023, 2, LEVEL, answer) is True


if __name__ == '__main__':
    main()