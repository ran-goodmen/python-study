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
