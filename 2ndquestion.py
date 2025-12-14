n=int(input())
L=[]
for i in range(n):
    x=int(input())
    L.append([x,list(map(int,input().split()))])
for i in range(len(L)):
    print("YES" if len(set(L[i][1]))<L[i][0] else "NO")
