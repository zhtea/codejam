	combine = []
	for ite in range(2**K):
		ll = []
		tmp = ite
		while len(ll)<K:
			ll.append(tmp%2)
			tmp = tmp//2
		final = ll#final to save final list
		middle = ll# middle to save middle list
		for i in range(C-1):
			final =[]
			for element in ll:
				if element == 0:
					for num in middle:
						final.append(num)
				else:
					for num in middle:
						final.append(1)
			middle = final
		combine.append(final)
	for line in combine:
		print("%s\n"%" ".join(str(num) for num in line))



