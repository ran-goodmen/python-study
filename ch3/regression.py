import re
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# matplotlib 的 backend的默认渲染器是agg，agg是一个没有图形显示界面的终端，如果要图像正常显示，则需要切换为图形界面显示的终端TkAgg

# 载入数据集
def load_dataset(filename):
    df = pd.read_csv(filename, sep='\s+', header=None)
    x_mat = np.mat(df.iloc[:, 0: -1])
    y_mat = np.mat(df.iloc[:, -1]).T
    return x_mat, y_mat

def line_regression(x_mat, y_mat):
    xTx = x_mat.T*x_mat
    if np.abs(np.linalg.det(xTx)) < 1e-8:
        print("This matrix is singular, cannot do inverse")
        return

    ws = xTx.I * (x_mat.T * y_mat)
    return ws


def line_regression_test(data_file):
    x_mat, y_mat = load_dataset(data_file)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_mat[:, 0].flatten().A[0], y_mat[:, 0].flatten().A[0])

    ws = line_regression(x_mat, y_mat)
    x_copy = x_mat.copy()
    x_copy.sort(1)
    y_hat = x_copy * ws
    ax.plot(x_copy[:, 0], y_hat, color='red')
    plt.show()


def lwl_regression(point, x_mat, y_mat, sigma=1.0):
    m = x_mat.shape[0]
    weights = np.mat(np.eye((m)))           # 权值矩阵, 计算每个样本点与输入向量point的高斯权值
    for j in range(m):                      #next 2 lines create weights matrix
        diff_mat = point - x_mat[j, :]     #
        weights[j, j] = np.exp(diff_mat * diff_mat.T / (-2.0*sigma**2))
    xTx = x_mat.T * (weights * x_mat)
    if np.abs(np.linalg.det(xTx)) < 1e-8:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (x_mat.T * (weights * y_mat))
    return point * ws


def lwl_regression_test(data_file, sigma):
    x_mat, y_mat = load_dataset(data_file)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_mat[:, 0].flatten().A[0], y_mat[:, 0].flatten().A[0])

    x_copy = np.linspace(0, 1.0, 101)
    x_copy = np.vstack((x_copy, np.ones((x_copy.shape[0])))).T
    #x_copy = x_mat.copy()
    #x_copy.sort(0)
    y_hat = np.zeros(x_copy.shape[0])
    for i in range(x_copy.shape[0]):
        y_hat[i] = lwl_regression(x_copy[i], x_mat, y_mat, sigma)

    ax.plot(x_copy[:, 0], y_hat, color='red')
    plt.show()

if __name__ == "__main__":
    line_regression_test('ex0.txt')
    #lwl_regression_test('ex0.txt', 0.02)