# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, a):
        cnt = 0
        for i in range(2, a):
            t = i

            int_to_str = str(i)
            for j in range(0, len(int_to_str)):
                t += int(int_to_str[j])

            if t == a:
                cnt += 1

        return cnt

if __name__ == '__main__':
    print(Solution().solution(101))