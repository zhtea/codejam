import sys

N = int(sys.stdin.readline().strip())
dic = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',' ':'0'}

for qw in range(1,N+1):
	s = sys.stdin.readline().strip('\n')
	p = ''
	r = ''
	for q in s:
		if dic[q][0] == p:
			r = r+' '+dic[q]
		else:
			r = r+dic[q]
		p = dic[q][0]
	print("Case #%d: %s"%(qw,r))



