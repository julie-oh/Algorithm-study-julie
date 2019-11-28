import copy


def perm(es: list):
    if len(es) == 1:
        return es

    results = []
    for i, e in enumerate(es):
        remain = copy.deepcopy(es) #!!!
        del remain[i]

        for res in perm(remain): #!!!
            results.append(e + res)
    return results


if __name__ == '__main__':
    print(perm(['a', 'b', 'c']))
