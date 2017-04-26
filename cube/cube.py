import sys
import decimal
import math

N = int(sys.stdin.readline().strip())

for qw in range(1,N+1):
	ll = [int(num) for num in sys.stdin.readline().strip().split()]
	N,M = ll[0],ll[1]
	ll = [int(num) for num in sys.stdin.readline().strip().split()]
	print("Case #%d:"%qw)
	for i in range(M):
		lm = [int(num) for num in sys.stdin.readline().strip().split()]
		total = 1
		for j in ll[lm[0]:(lm[1]+1)]:
			total = total*j
		total = decimal.Decimal(total)
		decimal.getcontext().prec = 9
		c=decimal.Decimal(str(1/(lm[1]-lm[0]+1)))
		print(pow(total,c))

