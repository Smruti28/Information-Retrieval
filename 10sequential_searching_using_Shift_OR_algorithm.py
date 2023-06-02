def to_bin(n, width=32):
    "Pad a binary number to WIDTH bits wide"
    s = bin(n).replace("0b", "")
    return (("%0" + str(width) + "d") % int(s))


def neg(x):
    # 0b11111111111111111111111111111111 - x
    return 0b11111111111111111111111111111111 - x


def shift_or():
 # trace = True
    text = input("Enter a text for searing:")
    pattern = input("Enter a pattern:")
    """Same as shift_and, but invert masks and use OR to 
 avoid an | in the inner loop."""
    m = len(pattern)
    n = len(text)
    neg0 = neg(0)
 # build table
    B = {}  # char -> bitmask table
    for i in range(m):
        B[pattern[i]] = (B.get(pattern[i], 0) | (1 << i))
    B = {k: neg(B[k]) for k in B}
 # complement all bit masks in B, complement bit mask
    a = neg0
    hit = (1 << (m - 1))
 # listNodes = Listbox(root, width=80, height=35)
 # listNodes.grid(column=0, row=12)
    notf = 0
    for i in range(n):
        a = (((a << 1) & neg0) | B.get(text[i], neg0))
        if a & hit == 0:
            print("\nPattern Found at %d" % (i - m + 2))
            notf = 1
 # print("found at %d" % (i - m + 2))
    if notf == 0:
        print("\n Pattern Not Found ")


shift_or()
