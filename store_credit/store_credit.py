import sys

N = int(sys.stdin.readline().strip())


for qw in range(1,N+1):
	total = int(sys.stdin.readline().strip())
	length = int(sys.stdin.readline().strip())
	ll = [int(num) for num in sys.stdin.readline().strip().split()]
	l = ll[:]
	ll.sort()
	i,j = 0,length-1
	amount = 0
	first =0
	last = 0
	while i<j:
		if ll[i]+ll[j]>total:
			j = j-1
			continue
		elif ll[i]+ll[j]>amount:
			amount = ll[i]+ll[j]
			first = ll[i]
			last = ll[j]
		i = i+1
	i = l.index(first)
	l[i] = -1
	j = l.index(last)
	if i>j:
		tmp = i
		i = j
		j = tmp
	print("Case #"+str(int(qw))+": "+str(i+1)+" "+str(j+1))