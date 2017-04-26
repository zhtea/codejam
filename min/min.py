#更改两个向量的坐标排列，以获得最小的乘积
import sys
N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
	length = int(sys.stdin.readline().strip())
	la = [int(word) for word in sys.stdin.readline().strip().split()]
	lb = [int(word) for word in sys.stdin.readline().strip().split()]
	la.sort()
	lb.sort(reverse=True)
	sum = 0
	for i in range(length):
		sum+=la[i]*lb[i]
	print("Case #%d: %d" % (qw,sum))
