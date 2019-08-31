"""
    http://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
"""
def solution(genres, plays):
    # d = {a: {'total': '', max: [{'dd':'dd'}, {'aa':'cc'}]}}

    d = {}

    for i, g in enumerate(genres):
        plays = plays[int(i)]

        if g in d:
            d[g]['total'] += plays

            m_items = d['g']['max'].items()
            if len(m_items) > 1:
                is_update = False
                waste_key = 0
                for item in m_items:
                    if is_update == False and item[0] < plays:
                        waste_key = item[0]
                    elif is_update == True and item[0] < plays:
                        if item[0] < d[g]['max'][waste_key]:
                            waste_key = item[0]
            else:
                d[g]['max'][plays] = i
        else:
            d[g] = {}
            d[g]['total'] = plays
            d[g]['max'] = [{plays: i}]

    print(d)
    # order = []
    # for item in d:
    #     item = {item['total']: item}
    #     for o in len(order):



# [classic, pop, classic, classic, pop]
# [500, 600, 150, 800, 2500]
# [4, 1, 3, 0]


if __name__ == '__main__':
    solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])