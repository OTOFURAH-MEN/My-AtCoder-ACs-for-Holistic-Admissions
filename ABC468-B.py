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

#ABC468-B Corridor Watch
#問題文
#[AtCoder ABC468 B](https://atcoder.jp/contests/abc468/tasks/abc468_b)
#提出結果
#[提出#77841042](https://atcoder.jp/contests/abc468/submissions/77841042)

#解法解説
#廊下について線形探索を行い、それぞれのガードマンGがいない部屋について、その部屋を中心とする視界D分の部屋をスライスし、それらにガードマンがいないならばnot_seeを1増やした。
#推定計算量
#Time:O(M^2)
#Space: O(M^2)
