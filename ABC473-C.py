import sys
N,K=map(int,input().split())
A=list(map(int,input().split()))
if K==1:
    print(1)
    sys.exit()
class_member=[0]*K
ans=K
for i in range(N):
    class_member[A[i]-1]+=1
class_member.sort()
for j in range(K):
    if class_member[j]+1<class_member[K-1]:
        ans-=1
print(ans)

#ABC473-C Change Schools
#問題文
#[AtCoder ABC473 C](https://atcoder.jp/contests/abc473/tasks/abc473_c)
#提出結果
#[提出#78804462](https://atcoder.jp/contests/abc473/submissions/78804462)

#解法解説
#まず、クラス人数を記録する配列class_memberを宣言し、在籍状況を表す配列Aからカウント。その後class_memberを昇順にソートすると最後尾に最多人数のクラス人数が現れる。
#後はクラスの人数(ソート済み)を先頭から探索し、「高橋君が悲しむクラスの数」、つまり「自分が所属したとして自分が所属しているクラスより多い人数が所属しているクラス」の数を総クラス数から減算すれば解が求まる。
#参考までに、TLE(実行時間制限超過)で誤答となった提出を下に掲載する。こちらは、ソートの前に逐一人数を加え、その後ソートしたものを別の配列に格納するという処理であるから非効率なのだろうと考えられる。計算量の複雑さ・繊細さを改めて感じた。
#[提出#78800668](https://atcoder.jp/contests/abc473/submissions/78800668)
#推定計算量
#Time:O(NK)
#Space: O(NK)
