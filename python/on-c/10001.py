def diet(diet, b, l):
    t = b + l

    for i in t:
        if not i in diet:
            diet = 'CHEATER'
            break

        diet = diet.replace(i, '')

    print(diet)


if __name__ == '__main__':
    diet('ABCD', 'AB', 'C') # D
    diet('ABEDCS', '', '') # ABCDES
    diet('EDSMB', 'MSD', 'A') # CHEATER
    diet('', '', '') # ''
