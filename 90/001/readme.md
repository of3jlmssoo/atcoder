```
N 切れ目候補の下図
L 長さ
K 切る数
A 切れ目の位置

短い切れ目を最大長とする

切れ目候補の数 長さ
切る数
切れ目候補の位置

3 34
1
8 13 26 (34)
-------------
8 5 13 8
    8+5=13
    13+8=21

MIN=5
MIN+前、MIN+後を比較
    MIN+前
        8+5 and 13+8
    MIN+後
        8
        5+13+8

7 45
2
7 11 16 20 28 34 38
--------------------
0 1 2 3 4 5 6 7
7 4 5 4 8 6 4 7
MIN選定ロジック
    単純に4を選ぶ
    4の位置取得
        index 1 left = 7
        index 1 righ = 5
        index 3 left = 5
        index 3 righ = 8
        index 6 left = 6
        index 6 righ = -100
    MAX = index 3 right = 8

MIN+前、MIN+後を比較
18 16 20 28 34 38
MIN+前、MIN+後を比較
    MIN+前
        18+16 and 20+
    MIN+後
        18


```