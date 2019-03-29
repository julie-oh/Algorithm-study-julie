"""
https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3
"""
def solution(skill, skill_trees):
    skill_dict = {}
    for i, v in enumerate(skill):
        skill_dict[v] = {'isSkillPass':False, 'order': i}

    re = 0

    for sk in skill_trees:
        is_break = False
        rem = 0
        for s in sk:
            if s in skill_dict:
                if skill_dict[s]['order'] == rem:
                    skill_dict[s]['isSkillPass'] = True
                    rem += 1
                else:
                    is_break = True
                    break
        if not is_break:
            re += 1

    return re

if __name__ == '__main__':
    # print(solution('CBD', ['BACDE']))  # 2
    print(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA'])) # 2