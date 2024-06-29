from typing import List


def sort_versions(versions: List[str]) -> List[str]:
    def verison_num_list(version):
        return [int(v) for v in version.split('.')]

    print(verison_num_list(versions[0]))
    print(verison_num_list(versions[1]))
    print(verison_num_list(versions[2]))
    versions.sort(key=verison_num_list)
    return versions


print(sort_versions(["10.1.0", "1.1.0", "0.1.1"])) # ['0.1.1', '1.1.0', '10.1.0']
print(sort_versions(["0.12.1", "0.2.1"])) # ['0.2.1', '0.12.1']

# version_num_listの出力を使うと、なぜソートされるのかは、下の例を見るとわかる
A = [[1, 9, 2], [1, 4, 3], [5, 8, 7], [5, 8, 3], [5, 2, 9]]
# x[0]の要素から比較を行う。x[0]が同じだったらx[1]の要素で比較を行う。x[1]が同じだったらx[2]の要素で比較を行う。
print(sorted(A, key=lambda x: (x[0], x[1], x[2])))
# 出力: [[1, 4, 3], [1, 9, 2], [5, 2, 9], [5, 8, 3], [5, 8, 7]]


from functools import cmp_to_key


def sort_versions(versions: List[str]) -> List[str]:
    def compare(v1, v2):
        a = [int(v) for v in v1.split('.')]
        b = [int(v) for v in v2.split('.')]
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1

    versions.sort(key=cmp_to_key(compare))
    return versions


# print(sort_versions(["10.1.0", "1.1.0", "0.1.1"])) # ['0.1.1', '1.1.0', '10.1.0']
# print(sort_versions(["0.12.1", "0.2.1"])) # ['0.2.1', '0.12.1']
