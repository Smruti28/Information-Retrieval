def brut_force_algo():
    S = input("Enter the text:\n")
    P = input("Enter the pattern:\n")
    SL = len(S)
    PL = len(P)
    if PL > SL:
        print("No Match Found")
    else:
        Found = False
        pos = []
        found_pos = []
        for i in range(0, SL-1):
            j = 0
            while j < PL and S[i] == P[j]:
                i = i+1
                j = j+1
                pos.append((i, j))
            if j == PL:
                Found = True
                found_pos.append(i-PL+1)
            if not Found:
                return 'No Matching Found !'

    return found_pos


res = brut_force_algo()
if res == 'No Matching Found !':
    print('No Matching Found !')
else:
    print("The match found at:")
    for i in res:
        print(i, end=" ")
