"""
挿入ソート
① 左手にすでに並んだ状態のカードをもつ（最初は，1 枚のカードから始める）．
② 並べたい 1 枚のカードを右手に持ち，すでに並んでいる左手のカードの数字を右から左へ見て，カードが挿入されるべき場所を探す．
③ 右手のカードを左手の並んだカードに挿入する．

アルゴリズム中で配列を使って挿入ソートを行う場合は，挿入するデータの格納場所を空ける必要がある．そこで，以下に示す挿入ソートのアルゴリズムでは，“挿入場所を探す” ということと，“挿入する場所を空ける” ということを同時に行うことにより挿入操作を実現している．

time: 3.337860107421875e-05

入力データは長さnの配列を想定している。
17 39 1 9 5 24 2 11 23 6
"""

def insert_sort(data):
    n = len(data)
    for i in range(1, n):
        x = data[i] # data配列のi番目の要素を抑える
        j = i       # そこのインデックス番号を控える
        while data[j - 1] > x and j > 0:
            data[j] = data[j - 1] # j-1の方が大きければ、値を右にずらす
            j -= 1
        data[j] = x
    return data

if __name__ == '__main__':
    import time

    data = input().split(' ')
    data = [int(x) for x in data]
    start = time.time()
    result = insert_sort(data)
    duration = time.time() - start
    print(result)
    print("time:", duration)
