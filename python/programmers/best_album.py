def solution(genres, plays):
    answer = []
    plays_dic = {}
    genres_dic = {}

    for i, genre in enumerate(genres):
        play = plays[i]

        if genre in genres_dic:
            plays_dic[genre] += play
        else:
            genres_dic[genre] = {}
            plays_dic[genre] = play

        if play in genres_dic[genre]:
            continue
        else:
            genres_dic[genre][play] = i

    print(plays_dic)
    print(genres_dic)
    sorted_plays = sorted(plays_dic.items(), key=lambda x: x[1], reverse=True)

    for play in sorted_plays:
        k = play[0]
        sorted_genres = sorted(genres_dic[k], reverse=True)

        answer.append(genres_dic[k][sorted_genres[0]])

        if len(sorted_plays) > 1:
            answer.append(genres_dic[k][sorted_genres[1]])

    return answer


# {'classic': {'total_play': 1450, 'list': {500: 0, 150: 2, 800: 3}}, 'pop': {'total_play': 5600, 'list': {600: 1, 2500: 4}}}

if __name__ == '__main__':
    solution(['classic', 'pop', 'classic', 'classic', 'pop', 'pop'], [500, 600, 150, 800, 2500, 2500])