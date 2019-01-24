# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
import operator


class Solution:
    def solution(self, sequence):
        hash = {}

        for i in range(0, len(sequence)):
            hash[sequence[i]] = i

        sorted_x = sorted(hash.items(), key=operator.itemgetter(1))

        re_list = [el[0] for el in sorted_x]

        return re_list