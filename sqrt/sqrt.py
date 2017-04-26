import sys
import math
from decimal import Decimal
def find(n):
	if n==1:
		return Decimal(3+math.sqrt(5))
	if n%2 == 1:
		return Decimal((3+math.sqrt(5)))*Decimal(Decimal(find(n//2))**2)
	else :
		return Decimal(Decimal(find(n//2))**2)

N= int(sys.stdin.readline().strip())
for qw in range(1,N+1):
	postive = str(find(int(sys.stdin.readline().strip()))).split(".")[0]
	if len(postive) == 1:
		print("Case #%d: 00%s"%(qw,postive[-1:]))
	elif len(postive) == 2:
		print("Case #%d: 0%s"%(qw,postive[-2:]))
	else:
		print("Case #%d: %s"%(qw,postive[-3:]))