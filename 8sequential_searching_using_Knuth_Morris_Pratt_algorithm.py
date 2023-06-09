def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
    initial_point = []
    pos = []
    m = 0
    n = 0
    while m != a:
        if text[m] == pattern[n]:
            m += 1
            n += 1
        else:
            n = prefix_arr[n-1]
        if n == b:
            initial_point.append((m-n)+1)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
        pos.append((m, n))
    return pos, initial_point


def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr


def kmp_algo():
    S = input('Enter a any Text:\n')
    P = input('Enter a any pattern:\n')
 # print(KMP_String(pat, txt))
    res = KMP_String(P, S)
    return res[1]


res = kmp_algo()
if len(res) == 0:
    print("No Match Found!")
else:
    print("Match Found at:")
    for i in res:
        print(i, end=" ")
