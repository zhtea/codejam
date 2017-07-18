import sys

N = int(sys.stdin.readline().strip())

for qw in range(1,N+1):
	line = [letter for letter in sys.stdin.readline().strip().split()]
	print("Case #%d: "%(qw)+' '.join(line[::-1]))