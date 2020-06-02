n,k = map(int,input().split())
listdiv=[]
for i in range(n):
	t = int(input())
	if t%k==0:
		listdiv.append(t)
print(len(listdiv))	
