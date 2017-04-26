import sys
N = int(sys.stdin.readline().strip())
for qw in range(1,N+1):
    ll = sys.stdin.readline().strip().split()
    print("Case #%d: %s"%(qw," ".join(word for word in ll[::-1])))
