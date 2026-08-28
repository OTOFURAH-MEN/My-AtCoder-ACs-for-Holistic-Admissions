M,D=map(int,input().split())
list_S=input()
list_S=list(list_S)
not_see=0
for i in range(M):
    if list_S[i]!="G":
        p=i-D
        q=i+D
        if p<0:
            p=0
        if q>M:
            q=M
        list_S1=list(list_S[p:q+1])
        if "G" not in list_S1:
            not_see+=1
print(not_see)

