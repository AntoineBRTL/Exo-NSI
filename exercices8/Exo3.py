def fusion(t, g, m, d):
    n1 = m - g + 1
    n2 = d - m

    lg = t[0:n1]
    ld = t[n1:d]

    lg.append(max(lg[-1], ld[-1]) + 1)
    ld.append(max(lg[-1], ld[-1]) + 1)

    i = 0
    j = 0

    for k in range(g, d):
        if lg[i] <= ld[j]:
            t[k] = lg[i]
            i += 1
        else:
            t[k] = ld[j]
            j += 1