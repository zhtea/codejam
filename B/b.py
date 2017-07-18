import sys
from functools import reduce
def minbig(a,b):
	if a<b:
		tmp = a
		a = b
		b = tmp
	if b==0:
		return a
	else:
		return minbig(b,a%b)


	
N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
	barber, line = [int(num) for num in sys.stdin.readline().strip().split()]
	time = [int(num) for num in sys.stdin.readline().strip().split()]
	ll = [0]*barber
	now = 0
	minbig = 1
	for num in time:
		minbig = int(minbig)*num//int(minbig(minbig,num))
	turn = 0
	for num in time:
		turn +=minbig/num
	line = line%int(turn)
	for i in range(1,line+1):
		small = ll[0]
		for num in ll:
			if num < small:
				small = num
		now = ll.index(small)
		ll[now] +=time[now]
	print("Case #%d: %d"%(qw,now+1))