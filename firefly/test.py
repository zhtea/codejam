import sys
import math
N = int(sys.stdin.readline().strip())
for i in range(1,N+1):
	print("Case #%d:" %i)
	n = int(sys.stdin.readline().strip())
	list = []
	for j in range(n):
		list.append(sys.stdin.readline().strip().split(" "))
    for item in list[1:]:
    	for count in range(6):
    		list[0][count] = int(list[0][count])+int(item[count])
    if (list[0][0]*list[0][3]+list[0][1]*list[0][4]+list[0][2]*list[0][5])/(list[0][3]**2+list[0][4]**2+list[0][5]**2)>0:
    	print("%f 0"%math.sqrt(list[0][0]**2+list[0][1]**2+list[0][2]**2))
    else :
    	print("%f %f"%((list[0][3]**2+list[0][4]**2+list[0][5]**2)*(list[0][0]**2+list[0][1]**2+list[0][2]**2)-(list[0][0]*list[0][3]+list[0][1]*list[0][4]+list[0][2]*list[0][5])**2/(list[0][3]**2+list[0][4]**2+list[0][5]**2)))