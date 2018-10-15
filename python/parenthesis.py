'''https://programmers.co.kr/learn/courses/30/lessons/12909'''
def parenthesis(s):
    list = [s[i] for i in range(len(s) - 1, -1, -1)]

    rem = []
    for idx, str in enumerate(list):
        if idx == 0 and str == '(':
            return False
        else:
            if str == ')':
                rem.append(str)
            elif str == '(' and len(rem) > 0:
                rem.pop()
            else:
                return False

    if len(rem) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    parenthesis('()()')
    parenthesis('(())()')
    parenthesis(')()(')
    parenthesis('(()(')
    parenthesis('(((((((((())')
