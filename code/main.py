import numpy as np
import pandas as pd


data1 = pd.read_csv('submission.csv')

data2 = pd.read_csv('submission_imp.csv')


def generation(main, support, cor):
    data1 = support.copy()
    data1v = data1.values

    data2 = main.copy()
    data2v = data2.values

    temp = main.copy()
    tempv = temp.values
    NCLASS = 7
    number = 0

    for i in range(len(main)):

        row1 = data1v[i, 1:]
        row2 = data2v[i, 1:]
        row1_sort = np.sort(row1)
        row2_sort = np.sort(row2)

        row = (row2 * cor) + (row1 * (1.0 - cor))
        row_sort = np.sort(row)

        for j in range(NCLASS):
            if ((row2[j] == row2_sort[8]) and (row1[j] != row1_sort[8])):
                row = row2
                number = number + 1
        tempv[i, 1:] = row
    temp.iloc[:, 1:] = tempv[:, 1:]
    return temp

sub = generation(data2, data1, 0.45)

sub_ens = sub

sub_ens.to_csv("new.csv",index=False)