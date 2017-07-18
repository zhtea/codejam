import sys
N = int(sys.stdin.readline().strip())


def num(k):
	i = 1
	while i<k:
		i = i<<1
	if k ==i:
		return 0
	else:
		if num(i-k) ==1:
			return 0
		else:
			return 1





for qw in range(1,N+1):
	k = int(sys.stdin.readline().strip())
	print("Case #%d: %d"%(qw,num(k)))