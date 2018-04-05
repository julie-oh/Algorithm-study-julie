def audition_k_pop(voters, score):

    # voter to round
    votersToRound = round(voters / 2)

    # get remaind voter to devide 2
    votersGetRemainder = voters % 2

    # get sum score
    votersGetTotal = 0

    # answers of voters
    numberOfAnswers = len(score)

    for i in range(numberOfAnswers):
        votersGetTotal += score[i]

    if numberOfAnswers < votersToRound:
        returnMessage("어떻게 맞추라는거야, 너 양아취니?")

    # unknown
    if voters / 2 >= numberOfAnswers:
        returnMessage("오스트라다무스 가라사대, 이 친구는 합격일 수도 있고 불합격일 수도 있네")
    else:
        if votersGetTotal > votersToRound:
            returnMessage("오스트라다무스 가라사대, 이 친구 될 친구구만")
        else:
            if votersGetTotal + (voters - numberOfAnswers) >= votersToRound:
                returnMessage("오스트라다무스 가라사대, 이 친구는 합격일 수도 있고 불합격일 수도 있네")
            else:
                returnMessage("오스트라다무스 가라시대, 백프로 안될 친구여")


def returnMessage(message):
    print(message)
    quit()

if __name__ == '__main__':
     audition_k_pop(9, [1,1,0,0,1])
    # audition_k_pop(8, [1,-1,1,1,1])
    # audition_k_pop(7, [1,1,1,-1,1,0,0])
    #audition_k_pop(2,[])
