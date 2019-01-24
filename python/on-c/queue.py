# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, cmds):
        queue = []
        for i in range(0, len(cmds)):
            if len(queue) > 0 and cmds[i] == 'POP':
                queue.pop(0)
            else:
                if cmds[i][:4] == 'PUSH':
                    queue.append(int(cmds[i][5:]))

        return queue