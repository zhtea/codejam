import sys

N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
	falvor = int(sys.stdin.readline().strip())
	customer = int(sys.stdin.readline().strip())
	ll = []
	for i in range(customer):
		customer_row = [int(word) for word in sys.stdin.readline().strip().split()]
		kinds = customer_row[0]
		dic = {}
		for i in range(kinds):
			dic[customer_row[2*i+1]] = customer_row[2*i+2]
		ll.append(dic)
	solution = [0]*falvor
	flag = False
	did =False
	while(solution.count(0)>0 and not flag):
		for dic in ll:
			did = False
			word = ""
			if len(dic) == 1 :
				for key in dic :
					word =int(key)
				if dic[word] ==1:
					did = True
					ll.remove(dic)
					for dic1 in ll:
						dic1.pop(word,0)
					solution[word-1] = 1
		if not did:
			flag =True
			print("Case #%d: %s" %(qw," ".join(str(w) for w in solution)))
	if not flag:
		print("Case #%d: IMPOSSIBLE"%qw)


