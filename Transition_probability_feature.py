import numpy as np
from Prcessing.multipleclassifier import multiclassifier


def marko(fasta):
    '''分词'''
    f = open(fasta)
    doc = f.readlines()
    list = []
    for seq in doc:
        if seq.startswith(">"):
            pass
        else:
            flag = seq.strip()
            a = [flag[i:i + 2] for i in range(len(flag) - 1)]
            list.append(a)
    m = np.array(list)
    '''计算首字母的频率'''
    atgc = {}
    for i in range(len(m)):
        if m[i][0][0] in atgc:

            atgc[m[i][0][0]] = atgc[m[i][0][0]] + 1
        else:
            atgc[m[i][0][0]] = 1
    for i, j in atgc.items():
        atgc[i] = atgc[i] / len(m)


    # ll = ["aa", "at", "ag", "ac", "ta", "tt", "tg", "tc", "ga", "gt", "gg", "gc", "ca", "ct", "cg", "cc"]
    '''计算转移概率'''
    dict = []
    for j in range(len(m[0])):
        flag = {}
        a = 0
        t = 0
        g = 0
        c = 0
        for i in range(len(m)):

            if m[i][j][0] == "A":
                a += 1
            elif m[i][j][0] == "T":
                t += 1
            elif m[i][j][0] == "G":
                g += 1
            else:
                c += 1

            if m[i, j] in flag:
                flag[m[i, j]] = flag[m[i, j]] + 1
            else:
                flag[m[i, j]] = 1
        for i in flag:

            if i[0] == "A":
                flag[i] = flag[i] / a
            elif i[0] == "T":
                flag[i] = flag[i] / t
            elif i[0] == "G":
                flag[i] = flag[i] / g
            else:
                flag[i] = flag[i] / c

        dict.append(flag)

    '''将转移概率当feature，频闭部分为首字母的出现概率'''
    l = []
    for i in range(len(m)):
        flag = []
        # if m[i][0][0] in atgc:
        #     flag.append(atgc[m[i][0][0]])
        for j in range(len(m[i])):
            if m[i][j] in dict[j]:
                flag.append(dict[j][m[i][j]])
            else:
                flag.append(0)
        l.append(flag)
    fea = np.array(l)

    return fea

# k=marko(fasta="fasta")

