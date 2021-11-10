l=list(map(int,input().split()))
q=len(l)
for i in range(0,q-2):
    for j in range(i+1,q-1):
        for k in range(j+1,q):
            if (l[i]+l[j]+l[k]==0):
                print(l[i],l[j],l[k])
"""0 -1  2 -3 1
0 -1 1
2 -3 1"""
