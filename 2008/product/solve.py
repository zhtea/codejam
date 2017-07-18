#coding=utf-8
import sys


  
N = int(sys.stdin.readline().strip())
for j in range(1,N+1):
    length = int(sys.stdin.readline().strip())
    l1 = [int(i) for i in sys.stdin.readline().strip().split()]
    l2 = [int(i) for i in sys.stdin.readline().strip().split()]
    l1.sort()
    l2.sort()
    l1 = l1[::-1]
    s = 0
    for i in range(length):
        s += l1[i] * l2[i]
    print("Case #%d: %d"%(j,s))