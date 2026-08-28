N=int(input())
list_C=list(map(int,input().split()))
most_color=0
max_count=0
for i in range(len(list_C)):
    if list_C.count(i+1)>=max_count:
        most_color=i
        max_count=list_C.count(i+1)
print(len(list_C)-max_count)

#ABC470-B Monocolor
#問題文
#[AtCoder ABC470 B](https://atcoder.jp/contests/abc470/tasks/abc470_b)
#提出結果
#[提出#78205265](https://atcoder.jp/contests/abc470/submissions/78205265)

#解法解説
#それぞれのボールについて、その色のボールが何個あるかを.count(i+1)でカウント、最大ならば更新していく。その後、総個数から最大個数(max_count)を引き、解答を求める。
#なお、most_colorは最大個数のボールが何色なのかを記録するが、不要である。
#推定計算量
#Time:O(N^2)
#Space: O(N^2)
