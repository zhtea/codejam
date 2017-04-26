import sys

N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
#	print("Case #%d: " % qw)
	target = int(sys.stdin.readline().strip())
	length = int(sys.stdin.readline().strip())
	ll = sys.stdin.readline().strip().split()#最后一个\n要不要处理呢？
	dic = {}
	count = 1
	for element in ll:
		num  = int(element)
		if (target - num) in dic :
			print("Case #%d: %d %d" %(qw,dic[target-num],count))
			break
		if not num in dic:
			dic[num] = count
		count +=1

