import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn import metrics


class Markov():

    def fasta2np(self, fasta):
        f = open(fasta)
        doc = f.readlines()
        list = []
        for seq in doc:
            if seq.startswith(">"):
                continue
            else:
                flag = seq.strip()
                a = [flag[i:i + 2] for i in range(len(flag) - 1)]
                list.append(a)
        m = np.array(list)
        return m

    '''m:训练集,p训练集中正例的个数'''

    def fit(self, m, p):
        pos = m[:p, :]

        neg = m[p:, :]

        '''pos的初始概率'''
        atgc1 = {}
        for i in range(len(pos)):
            if pos[i][0][0] in atgc1:

                atgc1[pos[i][0][0]] = atgc1[pos[i][0][0]] + 1
            else:
                atgc1[pos[i][0][0]] = 1
        for i, j in atgc1.items():
            atgc1[i] = atgc1[i] / len(pos)

        '''neg的初始概率'''
        atgc2 = {}
        for i in range(len(neg)):
            if neg[i][0][0] in atgc2:

                atgc2[neg[i][0][0]] = atgc2[neg[i][0][0]] + 1
            else:
                atgc2[neg[i][0][0]] = 1
        for i, j in atgc2.items():
            atgc2[i] = atgc2[i] / len(neg)

        '''pos的转移概率'''
        posdict = []
        for j in range(len(pos[0])):
            flag = {}
            a = 0
            t = 0
            g = 0
            c = 0
            for i in range(len(pos)):
                if pos[i][j][0] == "A":
                    a += 1
                elif pos[i][j][0] == "T":
                    t += 1
                elif pos[i][j][0] == "G":
                    g += 1
                else:
                    c += 1

                if pos[i, j] in flag:
                    flag[pos[i, j]] = flag[pos[i, j]] + 1
                else:
                    flag[pos[i, j]] = 1

            for i in flag:

                if i[0] == "A":
                    flag[i] = flag[i] / a
                elif i[0] == "T":
                    flag[i] = flag[i] / t
                elif i[0] == "G":
                    flag[i] = flag[i] / g
                else:
                    flag[i] = flag[i] / c

            posdict.append(flag)

        '''neg的转移概率'''
        negdict = []
        for j in range(len(neg[0])):
            flag = {}
            a = 0
            t = 0
            g = 0
            c = 0
            for i in range(len(neg)):

                if neg[i][j][0] == "A":
                    a += 1
                elif neg[i][j][0] == "T":
                    t += 1
                elif neg[i][j][0] == "G":
                    g += 1
                else:
                    c += 1

                if neg[i, j] in flag:
                    flag[neg[i, j]] = flag[neg[i, j]] + 1
                else:
                    flag[neg[i, j]] = 1

            for i in flag:

                if i[0] == "A":
                    flag[i] = flag[i] / a
                elif i[0] == "T":
                    flag[i] = flag[i] / t
                elif i[0] == "G":
                    flag[i] = flag[i] / g
                else:
                    flag[i] = flag[i] / c

            negdict.append(flag)

        posdict = np.array(posdict)
        negdict = np.array(negdict)

        return posdict, negdict, atgc1, atgc2

    def predict(self, test_set, posdict, negdict, atgc1, atgc2):
        posfea = []
        for i in range(len(test_set)):
            pos = 1
            if test_set[i][0][0] in atgc1:
                pos = pos * atgc1[test_set[i][0][0]]
            for j in range(len(test_set[i])):
                if test_set[i][j] in posdict[j]:
                    pos = pos * (posdict[j][test_set[i][j]])
                else:
                    pos = pos * 1
            posfea.append(pos)

        negfea = []
        for i in range(len(test_set)):
            neg = 1
            if test_set[i][0][0] in atgc1:
                neg = neg * atgc2[test_set[i][0][0]]
            for j in range(len(test_set[i])):
                if test_set[i][j] in negdict[j]:
                    neg = neg * (negdict[j][test_set[i][j]])
                else:
                    neg = neg * 1
            negfea.append(neg)

        label = np.array(posfea) / np.array(negfea)

        return label


def main():
    m = Markov()
    data = m.fasta2np("feature_fasta1.fasta")

    y = np.array([0] * 880 + [1] * 880)


    skf = StratifiedKFold(n_splits=10)
    acc=[]
    for train_index, test_index in skf.split(data, y):

        X_train, X_test = data[train_index], data[test_index]
        y_train, y_test = y[train_index], y[test_index]
        num=0
        for i in y_train:
            if i==0:
                num+=1
        posdict, negdict, atgc1, atgc2=m.fit(data,880)
        label=m.predict( X_test, posdict, negdict, atgc1, atgc2)

        l=[]
        for i in label:
            if i <1:
                l.append(1)
            else:
                l.append(0)

        acc.append(metrics.accuracy_score(y_test, l))
        print("ACC:{}".format(metrics.accuracy_score(y_test, l)))
    print(np.mean(acc))


if __name__ == '__main__':
    main()
