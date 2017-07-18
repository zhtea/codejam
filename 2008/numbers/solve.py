#coding=utf-8
import sys
import math
from decimal import *
  
N = int(sys.stdin.readline().strip())
k = Decimal(3+math.sqrt(5))
for i in range(1,N+1):
    n = Decimal(sys.stdin.readline().strip())
    tmp = str(k**n).split(".")[0][-3:]
    if len(tmp) == 2:
        tmp = "0"+tmp
    elif len(tmp) == 1:
        tmp ="00"+tmp 
    print("Case #%d: %s"%(i,tmp))
