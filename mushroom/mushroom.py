import sys

N = int(sys.stdin.readline().strip())

def solve_a(ll):
	sum  = 0
	for i in range(len(ll)-1):
		if ll[i]>ll[i+1]:
			sum +=(ll[i]-ll[i+1])
	return sum

def slove_b(ll):
	speed = 0
	for i in range(len(ll)-1):
		if (ll[i]-ll[i+1]) > speed:
			speed = ll[i]-ll[i+1]
	sum = 0
	for i in range(len(ll)-1):
		if ll[i]<speed:
			sum += ll[i]
		else:
			sum +=speed
	return sum



for qw in range(1,N+1):
	length = int(sys.stdin.readline().strip())
	ll = [int(num) for num in sys.stdin.readline().strip().split()]
	print("Case #%d: %d %d"%(qw,solve_a(ll),slove_b(ll)))
