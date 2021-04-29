def barisan_linier(list):
    """rumus un = bn + c, properti berisi [b, c]"""

    # NOTE Un = a + b(n -1)
    a = list[0]
    print(f"a = {a}")
    b = list[1] - list[0]
    print(f"b = {b}")
    c = a - b
    if c < 0:
        Un = f"Un = {b}n {c}"
    else:
        Un = f"Un = {b}n +{c}"

    properti = []
    properti.append(b)
    properti.append(c)

    return Un, properti


def barisan_kuadrat(list):
    """rumus un = an2 + bn + c, properti berisi [a, b, c]"""

    U1 = list[0]
    U2 = list[1]
    U3 = list[2]
    Q1 = U2 - U1
    Q2 = U3 - U2
    P = Q2 - Q1

    # menampilkan step pengerjaan
    a = P / 2
    print(f"2a = {P}")
    print(f"a = {P}/2\na = {a}\n")

    b = Q1 - 3*a
    print(f"3a + b = {Q1}")
    print(f"{3*a} + b = {Q1}")
    print(f"b = {Q1} - {3*a}\nb = {b}\n")

    c = U1 - a - b
    print(f"a + b + c = {U1}")
    print(f"{a} + {b} + c = {U1}")
    print(f"c = {U1} - {a+b}\nc = {c}\n")

    # NOTE Un = an2 + bn + c
    Un = f"Un = {a}n2 + {b}n + {c}"

    properti = []
    properti.append(a)
    properti.append(b)
    properti.append(c)

    return Un, properti


def cari_suku_ke(n, properti, linier):
    if linier:
        b = properti[0]
        c = properti[1]
        result = b * n + c
    elif not linier:
        a = properti[0]
        b = properti[1]
        c = properti[2]
        result = a * n**2 + b * n + c
    print(result)


def cek(list):
    """linier = True"""

    U1 = list[0]
    U2 = list[1]
    U3 = list[2]
    U4 = list[3]
    Q1 = U2 - U1
    Q2 = U3 - U2
    Q3 = U4 - U3
    P1 = Q2 - Q1
    P2 = Q3 - Q2
    linier = True
    if Q1 != Q2 and P1 == P2:
        return not linier
    elif Q1 == Q2:
        return linier
    else:
        print("Ada Kesalahan")
