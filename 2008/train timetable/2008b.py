#coding=utf-8
import sys
class clock:
    def __init__(self,name):
        [self.hour,self.min] =name.split(":")

def isbig(self,a,b): 
    if a.hour > b.hour:
        return 1
    elif a.hour <b.hour:
        return -1
    else:
        if a.min > b.min:
            return 1
        elif a.min < b.min:
            return -1
        else:
            return 0




N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
    T = int(sys.stdin.readline().strip())
    [NA,NB] = [int(a)  for a in sys.stdin.readline().strip().split()]
    [start,dest] = [clock(a) for a in sys.stdin.readline().strip().split()]
    print("Case #%d: %d"%(qw,count))