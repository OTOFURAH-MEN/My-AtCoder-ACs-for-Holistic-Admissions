N,M,K=map(int,input().split())
A=list(map(int,input().split()))
ate=[0]*N
cal=0
for i in range(N):
    if i>=M:
        if ate[i-M]==1:
            cal-=A[i-M]
    if cal+A[i]<=K:
        print("Yes")
        cal+=A[i]
        ate[i]=1
    else:
        print("No")

#ABC472-C On a Diet
#問題文
#[AtCoder ABC472 C](https://atcoder.jp/contests/abc472/tasks/abc472_c)
#提出結果
#[提出#78612303](https://atcoder.jp/contests/abc472/submissions/78612303)

#解法解説
#変数calには条件日数内で摂取した総カロリーを記録する。
#それぞれのループの最初で、M日前に何かを食べたのならその分のカロリーを減算する必要があるが、食べたかの管理をフラグ配列ateに記録している。これの対応する番地に記録があれば、その日のカロリーを減算する。
#その後、それぞれの食べ物について、calとその食べ物のカロリーの和がKを超えないならば変数calに加算し、ateに記録する。
#推定計算量
#Time:O(N)
#Space:O(N)
