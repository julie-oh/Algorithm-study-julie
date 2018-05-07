def stack_1(command):

    # push on stack-box
    stackBox = [1, 2, 3]

    # print message to User
    message = ''

    # devibe command and integer
    command = command.split()
    commandLine = command[0]
    commandInt = command[1]

    # length of stackBox
    lenOfstackbox = len(stackBox)

    # look at command
    if commandLine == 'pop':
        if lenOfstackbox > 0:
            message = stackBox.pop()
            print(message)

        else:
            print(-1)
    elif commandLine == 'size':
        print(len(stackBox))
    elif commandLine == 'empty':
        if lenOfstackbox == 0:
            print(1)
        else:
            print(0)
    elif commandLine == 'top':
        if lenOfstackbox == 0:
            print(-1)
        else:
            print(stackBox[-1])
    elif commandLine == 'push':
        if commandInt.isdigit():
            stackBox.append(int(commandInt))

    return stackBox

if __name__ == '__main__':
    # print(stack_1('push 10'))
    # print(stack_1('push -1'))
    # print(stack_1('empty'))
    print(stack_1('size'))