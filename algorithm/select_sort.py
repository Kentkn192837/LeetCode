"""
選択ソート
① 入力データの中から最大のデータをみつける．
② みつけた最大のデータをソートの対象から除外する．
③ ①，②の操作を n − 1 回繰り返す．

rangeの指定の仕方
range(9, -1, -1) (start, stop, step) stopに指定する値に注意 9,8,7,...,0
range(9)[::-1] 8,7,6,...,0

time: 5.698204040527344e-05

入力データは長さnの配列を想定している。
17 39 1 9 5 24 2 11 23 6
"""

def select_sort(data):
    n = len(data)
    for i in range(n)[::-1]:
        max = data[0]
        max_index = 0
        for j in range(0, i + 1, 1):
            if data[j] >= max:
                max = data[j]
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]
    return data

if __name__ == '__main__':
    import time

    data = input().split(' ')
    data = [int(x) for x in data]
    start = time.time()
    result = select_sort(data)
    duration = time.time() - start
    print(result)
    print("time:", duration)
