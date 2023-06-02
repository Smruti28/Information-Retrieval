res_list = []
NO_OF_CHARS = 256


def badCharHeuristic(string, size):
 # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS
 # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i
 # retun initialized list
    return badChar


def search(txt, pat):
    res_list = []
    if (txt == "" or pat == ""):
        print("Empty fields", "Fill out the fields")
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
 # s is shift of the pattern with respect to text
    s = 0
    while (s <= n - m):
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
         # print("Pattern occur at = {}".format(s))
            res_list.append(s+1)
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
    if res_list == []:
        print("No Match found")
    else:
        text = "Pattern found at : " + ",".join(map(str, res_list))
        print(text)


txt = input("Enter a Text:\n")
pat = input("Enter a Pattern:\n")
search(txt, pat)
