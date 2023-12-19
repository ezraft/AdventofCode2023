# from collections import *
# from itertools import *
# from math import *
import heapq
from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]
INF = int(1e9 + 7)


LEVEL = 2
SAMPLE_ANSWERS = [102, 94]
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
    print(M)
    dist = [[[[INF for _ in range(4)] for k in range(10)] for j in range(M)] for _ in range(N)]
    # for i in range(N):

    pq = []

    heapq.heappush(pq, ((0,0), (0, 0), -1))
    dist[0][0][0][0] = dist[0][0][0][1] = dist[0][0][0][2] = dist[0][0][0][3] = 0  # The shortest path from a node to itself is 0
    ok = True
    while pq:
        print(len(pq))
        if len(pq) > 7000:
            ok = False
        cdist, node, dir = heapq.heappop(pq)
        # print(cdist, node, dir)
        # print(dist[node[0]][node[1]][cdist[1]])
        if cdist[0] != dist[node[0]][node[1]][cdist[1]][dir]:
            continue


        for i in range(4):
            if dir != -1 and abs(i - dir) == 2:
                continue
            if node[0] + chr[i] >= 0 and node[0] + chr[i] < N and node[1] + chc[i] >= 0 and node[1] + chc[i] < M:
                v = int(A[node[0] + chr[i]][node[1] + chc[i]])
                # print(node[0] + chr[i], node[1] + chc[i], v)
                if dir == -1 or i == dir:
                        # print(node, cdist)
                        # print(dist[node[0]][node[1]][cdist[1]])
                        # assert cdist[0] >= dist[node[0]][node[1]][cdist[1]]
                        j = cdist[1]
                        if j + 1 >= 10:
                            continue
                        if cdist[0] + v < dist[node[0] + chr[i]][node[1] + chc[i]][j + 1][i]:
                            dist[node[0] + chr[i]][node[1] + chc[i]][j + 1][i] = cdist[0] + v
                            heapq.heappush(pq, ((dist[node[0] + chr[i]][node[1] + chc[i]][j + 1][i], j + 1), (node[0] + chr[i], node[1] + chc[i]), i))
                elif cdist[1] >= 3 and cdist[0] + v < dist[node[0] + chr[i]][node[1] + chc[i]][0][i]:
                    # print(node, cdist)
                    # print(dist[node[0]][node[1]][cdist[1]])
                    # assert cdist[0] >= dist[node[0]][node[1]][cdist[1]]
                    # print(node, dir, i)
                    dist[node[0] + chr[i]][node[1] + chc[i]][0][i] = cdist[0] + v
                    heapq.heappush(pq, ((dist[node[0] + chr[i]][node[1] + chc[i]][0][i], 0), (node[0] + chr[i], node[1] + chc[i]), i))

    for i in range(N):
        for j in range(M):
            for k in range(4):
                print(i, j, k, dist[i][j][0][k], dist[i][j][1][k], dist[i][j][2][k])
    ans = INF
    for k in range(4):
        for j in range(3, 10):
            ans = min(ans, dist[N-1][M-1][j][k])

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
    assert submit_answer(2023, 17, LEVEL, answer) is True


if __name__ == '__main__':
    main()