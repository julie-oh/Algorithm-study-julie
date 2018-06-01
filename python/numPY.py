''' https://programmers.co.kr/learn/challenge_codes/97 '''
def numPY(s):
    flag = False
    string_p = 0
    string_y = 0
    
    for idx, idx_str in enumerate(s):
        if idx_str == 'p' or idx_str == 'P':
            string_p += 1
        if idx_str == 'y' or idx_str == 'Y':
            string_y += 1
    
    if string_p == string_y:
        flag = True
    
    return flag
    
    
    
print( numPY("pPoooyY") )
print( numPY("Pyy") )