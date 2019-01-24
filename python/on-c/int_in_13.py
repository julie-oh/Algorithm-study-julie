# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
# 13이 들어가는 갯수
class Solution:
    def solution(self, a):
        total = 0

        for i in range(13, a + 1):
            int_to_str = str(i)

            for j in range(0, len(int_to_str)):
                if int_to_str[j] == '1' and j != len(int_to_str) - 1:
                    if int_to_str[j+1] == '3':
                        total += 1
                        break

        return total

if __name__ == '__main__':
    print(Solution().solution(200))