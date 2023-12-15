# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer
from functools import cmp_to_key


#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [6440, 5905]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]
alph = "J23456789TQKA"
def val (hand : str) -> int:
    if (len(set(hand)) == 1 or (len(set(hand)) == 2 and 'J' in hand)):
        return 1
    elif (len(set(hand)) == 2 or (len(set(hand)) == 3 and 'J' in hand)):
        for e in hand:
            if e != 'J' and hand.count(e) == 1:
                return 2
        return 3
    elif (len(set(hand)) == 3 or (len(set(hand)) == 4 and 'J' in hand)):
        cur = []
        for e in hand:
            cur.append(hand.count(e))
        if sorted(cur)[2] == 3 or 'J' in hand:
            return 4
        else:
            return 5
    elif (len(set(hand)) == 4 or (len(set(hand)) == 5 and 'J' in hand)):
        return 6
    else:
        return 7

def comp (pos, pos2):
    pos = pos[0]
    pos2 = pos2[0]
    if (val(pos) == val(pos2)):
        for i in range(len(pos)):
            if alph.index(pos[i]) == alph.index(pos2[i]):
                continue
            if alph.index(pos[i]) > alph.index(pos2[i]):
                return -1
            else:
                return 1
    else:
        if val(pos) < val(pos2):
            return -1
        else:
            return 1
    return 0
def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]

    N = len(A)
    B = []
    for i in range(N):
        B.append([line for line in A[i].split()])
    for i in range(N):
        print(B[i][0])

    print("N =", N)
    print(A[:10])

    B = sorted(B, key=cmp_to_key(comp))
    for e in B:
        print(e[0])
    ans = 0
    for e in range(len(B)):
        ans = ans + (e + 1) * int(B[len(B) - e - 1][1])
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
    assert submit_answer(2023, 7, LEVEL, answer) is True


if __name__ == '__main__':
    main()