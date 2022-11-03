import re
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 载入数据集
def load_dataset(filename):
    df = pd.read_csv(filename, sep='\s+', header=None)
    x_mat = np.mat(df.iloc[:, 0: -1])
    y_mat = np.mat(df.iloc[:, -1]).T
    return x_mat, y_mat


def rand_j(i, m):
    """随机选择一个不等于i的整形下标j"""
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j


def clip_alpha(alpha, H, L):
    if alpha > H:
        alpha = H
    if L > alpha:
        alpha = L
    return alpha


def smo_simple(data_mat, label_mat, C, toler, max_iter):
    b = 0
    m, n = data_mat.shape
    alphas = np.mat(np.zeros((m, 1)))
    iter = 0
    while iter < max_iter:
        alpha_pairs_changed_num = 0
        for i in range(m):
            # 将xi向量带入现有的模型计算f(xi)
            fXi = float(np.multiply(alphas, label_mat).T*(data_mat*data_mat[i,:].T)) + b
            Ei = fXi - float(label_mat[i])
            # 检查alphas[i]是否违反了KKT条件
            # yi*Ei = yi*(fxi - yi) = yi*fxi - yi*yi = yi*fxi - 1
            if (label_mat[i]*Ei < -toler and alphas[i] < C) or \
                (label_mat[i]*Ei > toler and alphas[i] > 0):
                j = rand_j(i, m)
                fXj = float(np.multiply(alphas, label_mat).T * (data_mat*data_mat[j, :].T)) + b
                Ej = fXj - float(label_mat[j])
                old_alpha_i = alphas[i].copy()
                old_alpha_j = alphas[j].copy()
                if label_mat[i] != label_mat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L==H")
                    continue
                eta = data_mat[i, :]*data_mat[i, :].T + data_mat[j, :]*data_mat[j, :].T - \
                      2.0 * data_mat[i, :]*data_mat[j, :].T

                if eta <= 0:
                    print("eta<=0")
                    continue
                alphas[j] += label_mat[j]*(Ei - Ej) / eta
                alphas[j] = clip_alpha(alphas[j], H, L)
                if abs(alphas[j] - old_alpha_j) < 1.0e-6:
                    print("j not moving enough")
                    continue
                alphas[i] += label_mat[j]*label_mat[i]*(old_alpha_j - alphas[j])

                b1 = b - Ei - label_mat[i]*(alphas[i]-old_alpha_i)*data_mat[i,:]*data_mat[i,:].T - \
                     label_mat[j]*(alphas[j]-old_alpha_j)*data_mat[i, :]*data_mat[j, :].T
                b2 = b - Ej - label_mat[i]*(alphas[i]-old_alpha_i)*data_mat[i,:]*data_mat[j,:].T - \
                     label_mat[j]*(alphas[j]-old_alpha_j)*data_mat[j, :]*data_mat[j, :].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2) / 2.0
                alpha_pairs_changed_num += 1
                print("iter: %d i:%d, pairs changed %d" % (iter,i,alpha_pairs_changed_num))
        if alpha_pairs_changed_num == 0:
            iter += 1
        else:
            iter = 0
        print("iteration number: %d" % iter)
    return b, alphas


def calc_ws(alphas, data_mat, label_mat):
    m, n = data_mat.shape
    w = np.zeros((n, 1))
    for i in range(m):
        w += np.multiply(alphas[i] * label_mat[i], data_mat[i, :].T)

    return w


if __name__ == "__main__":
    data_mat, label_mat = load_dataset('testSet.txt')
    b, alphas = smo_simple(data_mat, label_mat, 0.6, 0.001, 100)
    b = b.flatten().A[0]
    print(b)
    print(alphas)

    # 找出所有alpha > 0的支持向量
    # 注意alphas是mat类型, 为了能够得到有效索引, 需要先将它转成array
    index = (alphas.getA().flatten() > 0.0)
    v = np.array(data_mat[index])
    print(v)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    ax.scatter(data_mat[:, 0].flatten().A[0], data_mat[:, 1].flatten().A[0],
               c=label_mat.getA().flatten(), marker='.')

    w = calc_ws(alphas, data_mat, label_mat)
    split_boundary_func = lambda x: (-b - w[0][0] * x) / w[1][0]
    xx = np.linspace(2.5, 6, 10)
    yy = split_boundary_func(xx)
    ax.plot(xx, split_boundary_func(xx), c='red')

    ax.scatter(v[:, 0], v[:, 1], marker='o', color='none', edgecolor='red', s=200)

    plt.show()
