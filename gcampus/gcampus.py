import sys

N = int(sys.stdin.readline().strip())

for qw in range(1,N+1):
	ll = [int(num) for num in sys.stdin.readline().strip().split()]
	N = ll[0]
	M = ll[1]
	ll = [[-1]*N]*N
	print("Case #%d:"%qw)
	for i in range(M):
		lm = [int(num) for num in sys.stdin.readline().strip().split()]
		a = lm[0]
		b = lm[1]
		if a > b:
			tmp = a
			a = b
			b = tmp
		tmp = False
		for j in range(N):
			if ll[a][j] != -1 and ll[j][b] !=-1 and (ll[a][j]+ll[j][b])<lm[2]:
				print(i)
				tmp = True
				break
		if not tmp:
			if ll[a][b] ==-1:
				ll[a][b] = lm[2]
			else:
				print(i)

