import sys
import math

def decide(start,end,count,ll):
	if end <= start:
		return 0
	if count ==1:
		return end-start
	if count == 2:
		if math.fabs(int(ll[0])-(end+start)/2) < math.fabs(int(ll[1])-(end+start)/2):
			return end-start+end-int(ll[0])-1 
		else :
			return end-start+int(ll[1])-start-1
	if count%2 == 1:
		cut = int(ll[count//2])
		return end-start + decide(start,cut-1,count//2,ll[:count//2])+decide(cut+1,end,count//2,ll[count//2+1:])
	else:
		if math.fabs(int(ll[count//2])-(start+end)/2)<math.fabs(int(ll[count//2-1])-(start+end)/2):
			cut = int(ll[count//2])
			return end-start+decide(start,cut-1,count//2,ll[:count//2])+decide(cut+1,end,count//2-1,ll[count//2+1:])
		else:
			cut = int(ll[count//2-1])
			return end-start+decide(start,cut-1,count//2-1,ll[:count//2-2])+decide(cut+1,end,count//2,ll[count//2-1:])





N = int(sys.stdin.readline().strip())
#print("hello")
for qw in range(1, N+1):
	print('Case #%d:' % qw)
	x,y = sys.stdin.readline().strip().split(" ")
	ll = sys.stdin.readline().strip().split(" ")
	print(decide(1,int(x),int(y),ll))



