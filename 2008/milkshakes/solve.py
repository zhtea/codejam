#coding=utf-8
import sys


  
N = int(sys.stdin.readline().strip())
for i in range(1,N+1):
    flavor = int(sys.stdin.readline().strip())
    customer = int(sys.stdin.readline().strip())
    flavors = [0]*flavor
    r = True
    j = 0
    while j < customer:
        l = [int(i) for i in sys.stdin.readline().strip().split()]
        fl = l[0]
        l = l[1:]
        tmp = -1
        tmp_mark = False
        for k in range(fl):
            if l[k*2+1] == flavors[l[k*2]-1]:
                tmp_mark = True
                break
            if l[k*2+1] == 1:
                tmp = l[k*2]-1
        if not tmp_mark:
            if tmp == -1:
                r = False
            else:
                if flavors[tmp] == 1:
                    r = False
                else:
                    flavors[tmp] = 1
        j += 1
    if not r:
        print("Case #%d: IMPOSSIBLE"%i)
    else:
        print("Case #%d: "%i + " ".join([str(j) for j in flavors]))
