import operator


operator_list = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }


def postfix_notation(d):
    arr = d.split(' ')
    stack = []

    for v in arr:
        if v in operator_list:
            post, pre = stack.pop(), stack.pop()
            stack.append(operator_list[v](pre, post))
        else:
            stack.append(int(v))

    return stack.pop()


if __name__ == '__main__':
    # (2 + 3) * (5 - 6) - (7 + 8)
    print(postfix_notation('2 3 + 5 6 - * 7 8 + -'))