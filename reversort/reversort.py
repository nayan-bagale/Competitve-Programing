import os
import sys

if not os.environ.get("ONLINE_JUDGE"):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')



def reverseSort(a):
    cost =0
    for i in range(len(a) - 1):
        mini_value = min(a[i:])
        value_index = a[i:].index(mini_value)
        a[i:value_index + 1 + i] = a[i:value_index + 1 + i][::-1]
        cost += len(a[i:value_index + 1 + i])

    return cost



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print('Case #', _ + 1, ': ', reverseSort(a), sep='')
