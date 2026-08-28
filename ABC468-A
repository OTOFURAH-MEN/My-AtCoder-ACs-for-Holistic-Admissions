N=input()
list_A=list(map(int, input().split()))
ans=0
for i in range(int(len(list_A))-2):
    if list_A[i]<list_A[i+1] and list_A[i+1]>list_A[i+2]:
        ans+=1
print(ans)

#ABC468-A Maximal Value
#問題文
#[AtCoder ABC468 A](https://atcoder.jp/contests/abc468/tasks/abc468_a)
#提出結果
#[提出#77815040](https://atcoder.jp/contests/abc468/submissions/77815040)

#解法解説
#数列を配列として取得し、条件を満たす項を線形探索、変数ansでカウントする。
#推定計算量
#Time:O(N-2)
#Space: O(N-2)
