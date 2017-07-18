#coding=utf-8
import sys


  
N = int(sys.stdin.readline().strip())
for i in range(1,N+1):
    count = 0
    S = int(sys.stdin.readline().strip())
    engines = []
    for j in range(S):
        engines.append(sys.stdin.readline().strip())
    Q = int(sys.stdin.readline().strip())
    tmp_engines = engines[:]
    tmp_string = ''
    for j in range(Q):            
        tmp_string = sys.stdin.readline().strip()
        if len(tmp_engines) == 1 and tmp_engines[0] == tmp_string:
            tmp = engines.index(tmp_string)
            tmp_engines = engines[:tmp] + engines[tmp+1:]
            count += 1
        elif tmp_string in tmp_engines:
            tmp = tmp_engines.index(tmp_string)
            tmp_engines = tmp_engines[:tmp] + tmp_engines[tmp+1:]
    print("Case #%d: %d"%(i,count))