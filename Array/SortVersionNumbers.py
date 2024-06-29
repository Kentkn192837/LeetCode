from typing import List


def sort_versions(versions: List[str]) -> List[str]:
    def verison_num_list(version):
        return [int(v) for v in version.split('.')]

    versions.sort(key=verison_num_list)
    return versions


print(sort_versions(["10.1.0", "1.1.0", "0.1.1"])) # ['0.1.1', '1.1.0', '10.1.0']
print(sort_versions(["0.12.1", "0.2.1"])) # ['0.2.1', '0.12.1']


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


print(sort_versions(["10.1.0", "1.1.0", "0.1.1"])) # ['0.1.1', '1.1.0', '10.1.0']
print(sort_versions(["0.12.1", "0.2.1"])) # ['0.2.1', '0.12.1']
