# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, stats):
        area = 0
        compare = 0

        for i in range(0, len(stats)):
            now_cnt = 0
            for j in range(0, len(stats[i])):
                if stats[i][j] == '1':
                    now_cnt += 1

            per = 100 * int(now_cnt) / int(len(stats[i]))

            if i == 0:
                compare = per
            else:
                if compare > per:
                    area = i
                    compare = per

        return area
