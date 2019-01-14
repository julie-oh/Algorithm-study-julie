def min_cost_stair(s):
    s.extend([0, 0])
    return min_cost_claim_stair(s, len(s) - 1, 0)

def min_cost_claim_stair(s, idx, m):
    if idx == 0:
        return m

    m = min(s[idx + 1], s[idx + 2]) + s[idx]
    return min_cost_claim_stair(s, idx - 1, m)

if __name__ == '__main__':
    print(min_cost_stair([1,2,3,4]))
    print(min_cost_claim_stair([10,15,20], 2, 0))
    print(min_cost_claim_stair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 9, 0))