N=int(input())
list_S=list(input())
ans=0
for i in range(len(list_S)):
    if list_S[i]=="x":
        if i==0:
            if N==1:
                ans+=1
            elif list_S[i+1]=="x":
                ans+=1
        elif i==len(list_S)-1:
            if list_S[i-1]=="x":
                ans+=1
        elif list_S[i-1]=="x" and list_S[i+1]=="x":
            ans+=1
print(ans)

#ABC469-B Isolated Seats
#問題文
#[AtCoder ABC468 B](https://atcoder.jp/contests/abc469/tasks/abc469_b)
#提出結果
#[提出#77815040](https://atcoder.jp/contests/abc469/submissions/78018734)

#解法解説
#座席を配列として取得し、条件を満たす項を線形探索、変数ansでカウントする。この際、条件分岐を組み合わせることで、エラー回避と処理速度の向上を図った。
#推定計算量
#Time:O(N)
#Space: O(N)
