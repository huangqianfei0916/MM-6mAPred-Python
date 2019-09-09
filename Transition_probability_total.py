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
    atgc={}
    for i in range(len(m)):
        if m[i][0][0] in atgc:

            atgc[m[i][0][0]]=atgc[m[i][0][0]]+1
        else:
            atgc[m[i][0][0]]=1

    print(atgc)

    # ll = ["aa", "at", "ag", "ac", "ta", "tt", "tg", "tc", "ga", "gt", "gg", "gc", "ca", "ct", "cg", "cc"]
    '''计算转移概率，具体的是先计算出现次数，在除以样本总数'''
    dict = []
    for j in range(len(m[0])):
        flag = {}
        for i in range(len(m)):
            if m[i, j] in flag:
                flag[m[i, j]] = flag[m[i, j]] + 1
            else:
                flag[m[i, j]] = 1
        dict.append(flag)

    '''将转移概率当feature，频闭部分为首字母的出现概率'''
    l=[]
    for i in range(len(m)):
        flag=[]
        # if m[i][0][0] in atgc:
        #     flag.append(atgc[m[i][0][0]])
        for j in range(len(m[i])):
            if m[i][j] in dict[j]:
                flag.append(dict[j][m[i][j]])
            else:
                flag.append(0)
        l.append(flag)
    fea=np.array(l)
    fea=fea/len(m)

    return fea

marko(fasta="fasta")