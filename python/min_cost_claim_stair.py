def min_cost_claim_stair(s):
    case_1 = 0
    case_2 = 0

    for i in range(len(s)-1, -1, -1):
        current = s[i] + min(case_1, case_2)

        case_2 = case_1
        case_1 = current


    return min(case_1, case_2)

if __name__ == '__main__':
    print(min_cost_claim_stair([1,2,3,4]))
    print(min_cost_claim_stair([10,15,20]))
    print(min_cost_claim_stair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))