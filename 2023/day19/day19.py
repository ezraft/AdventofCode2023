# from collections import *
# from itertools import *
# from math import *
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [19114, 167409079868000]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]
rules = {}
q = {'x':0, 'm':1, 'a':2, 's':3}
def flow(part, rule):
    print(part, rule)
    if rule == 'A':
        tot = 1
        for i in range(4):
            tot = tot * (part[i][1] - part[i][0] + 1)
        return tot
    elif rule == 'R':
        return 0

    for x in rules[rule]:
        if len(x) == 1:
            return flow(part, x[0])
        elif (x[0][1] == '>'):
            curin = (max(part[q[x[0][0]]][0], int(x[0][2:]) + 1), part[q[x[0][0]]][1])
            cur = max(0, curin[1] - curin[0] + 1)
            print(x[1], part, cur)
            if cur != 0:
                tmp = [part[i] for i in range(len(part))]
                tmp[q[x[0][0]]] = curin
                sm = max(0, flow(tmp, x[1]))
                print("here")
                if curin[0] > part[q[x[0][0]]][0]:
                    tmp = [part[i] for i in range(len(part))]
                    tmp[q[x[0][0]]] = (part[q[x[0][0]]][0], curin[0] - 1)
                    sm = sm + max(0, flow(tmp, rule))
                return sm
        elif x[0][1] == '<':
            curin = (part[q[x[0][0]]][0], min(part[q[x[0][0]]][1], int(x[0][2:]) - 1))
            cur = max(0, curin[1] - curin[0] + 1)
            print(x[1], part, cur)
            if cur != 0:
                tmp = [part[i] for i in range(len(part))]
                tmp[q[x[0][0]]] = curin
                sm = max(0, flow(tmp, x[1]))
                if curin[1] < part[q[x[0][0]]][1]:
                    tmp = [part[i] for i in range(len(part))]
                    tmp[q[x[0][0]]] = (curin[1] + 1, part[q[x[0][0]]][1])
                    sm = sm + max(0, flow(tmp, rule))
                return sm
    return 0



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
    C = []
    ok = False
    for i in range(N):
        if A[i] == "\n" or A[i] == '':
            ok = True
            continue
        if not ok:
            B = A[i].split("{")
            print(B)
            rules[B[0]] = [val.split(":") for val in B[1][:-1].split(',')]
        elif ok:
            C.append([int(v[2:]) for v in A[i][1:-1].split(",")])

    for x in rules.keys():
        print(x, rules[x])
    print()
    for x in C:
        print(x)

    ans = flow([(1, 4000), (1, 4000), (1, 4000), (1, 4000)], "in")



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
    assert submit_answer(2023, 19, LEVEL, answer) is True


if __name__ == '__main__':
    main()