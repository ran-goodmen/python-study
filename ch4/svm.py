import re
import random
import numpy as np
import matplotlib.pyplot as plt


class SVM:
    def __init__(self):
        self.data_mat = None            # 输入特征矩阵
        self.label_mat = None           # 标签矩阵
        self.C = 1
        self.toler = 1.0e-6
        self.m = 0                      # 数据行数
        self.alphas = None              # alpha列表
        self.b = 0                      # 偏置
        self.ecache = None              # 误差缓存
        self.K = None                   # 核参数
        self.svs = None
        self.sv_labels = None
        self.sv_indices = None
        self.ktup = ('lin', 0)

    # 计算核函数值
    def _kernel(self, X, A, ktup):  # calc the kernel or transform data to a higher dimensional space
        m, n = np.shape(X)
        K = np.mat(np.zeros((m, 1)))
        if ktup[0].lower() == 'lin':
            # 线性核模型
            K = X * A.T
        elif ktup[0].lower() == 'rbf':
            # 径向核(高斯核)模型
            for j in range(m):
                delta_row = X[j, :] - A
                K[j] = delta_row * delta_row.T
            K = np.exp(K / (-1 * ktup[1] ** 2))
        else:
            raise NameError('不支持的核模型')
        return K

    # 计算第k个样本的误差
    def _calc_ek(self, k):
        fXk = float(np.multiply(self.alphas, self.label_mat).T * self.K[:, k] + self.b)
        Ek = fXk - float(self.label_mat[k])
        return Ek

    # 在[0, m-1]中随机差生一个不等于i的整数
    def _rand_j(self, i, m):
        j = i
        while j == i:
            j = int(random.uniform(0, m))
        return j

    # 在alpha[i]确定后选择alpha[j], 最大化ei - ej
    def _select_j(self, i, ei):
        max_k = -1
        max_delta_e = 0
        ej = 0
        self.ecache[i] = [1, ei]
        # 从ecache中挑选出标记列不为0的有效误差下标
        valid_ecache_list = np.nonzero(self.ecache[:, 0].A)[0]
        if (len(valid_ecache_list)) > 1:
            # 如果存在有效误差
            for k in valid_ecache_list:
                if k == i: continue
                ek = self._calc_ek(k)
                delta_e = abs(ei - ek)
                if delta_e > max_delta_e:
                    max_k = k;
                    max_delta_e = delta_e;
                    ej = ek
            return max_k, ej
        else:
            # 如果不存在有效误差, 此时通常是第一次运行
            j = self._rand_j(i, self.m)
            ej = self._calc_ek(j)
        return j, ej

    # 当alpha列表中有元素发生变化, 更新第k个样本的误差
    def _update_ek(self, k):
        ek = self._calc_ek(k)
        self.ecache[k] = [1, ek]

    # 将alpha值钳制到H—L之间
    def _clip_alpha(self, alpha, H, L):
        if alpha > H:
            alpha = H
        if L > alpha:
            alpha = L
        return alpha

    # 对给定的alpha[i], 选择最佳alpha[j], 进行配对优化
    # 如果优化成功返回1, 否则返回0
    def _inner(self, i):
        ei = self._calc_ek(i)
        # 检查alpha[i]是否违反KKT条件
        if ((self.label_mat[i] * ei < -self.toler) and (self.alphas[i] < self.C)) or \
                ((self.label_mat[i] * ei > self.toler) and (self.alphas[i] > 0)):
            j, ej = self._select_j(i, ei)       # 挑选一个最优的alpha[j]
            old_alpha_i = self.alphas[i].copy()
            old_alpha_j = self.alphas[j].copy()
            if self.label_mat[i] != self.label_mat[j]:
                L = max(0, self.alphas[j] - self.alphas[i])
                H = min(self.C, self.C + self.alphas[j] - self.alphas[i])
            else:
                L = max(0, self.alphas[j] + self.alphas[i] - self.C)
                H = min(self.C, self.alphas[j] + self.alphas[i])
            if L == H:
                print("L==H")
                return 0

            eta = 2.0 * self.K[i, j] - self.K[i, i] - self.K[j, j]  # changed for kernel
            if eta >= 0:
                print("eta>=0")
                return 0

            # 更新alphas[j]和对应的ej
            self.alphas[j] -= self.label_mat[j] * (ei - ej) / eta
            self.alphas[j] = self._clip_alpha(self.alphas[j], H, L)
            self._update_ek(j)
            if abs(self.alphas[j] - old_alpha_j) < 1.0e-5:
                print("j not moving enough")
                return 0

            # 更新alphas[i]和对应的ei
            self.alphas[i] += self.label_mat[j] * self.label_mat[i] * \
                              (old_alpha_j - self.alphas[j])
            self._update_ek(i)

            # 更新偏置b
            b1 = self.b - ei - self.label_mat[i] * (self.alphas[i] - old_alpha_i) * \
                 self.K[i, i] - self.label_mat[j] * (self.alphas[j] - old_alpha_j) * self.K[i, j]
            b2 = self.b - ej - self.label_mat[i] * (self.alphas[i] - old_alpha_i) * \
                 self.K[i, j] - self.label_mat[j] * (self.alphas[j] - old_alpha_j) * self.K[j, j]

            if 0 < self.alphas[i] and self.C > self.alphas[i]:
                # 如果alphas[i]是支持向量
                self.b = b1
            elif 0 < self.alphas[j] and self.C > self.alphas[j]:
                # 如果alphas[j]是支持向量
                self.b = b2
            else:
                self.b = (b1 + b2) / 2.0
            return 1
        else:
            return 0

    def fit(self, data_arr, label_arr, C, toler, maxIter, ktup=('lin', 0)):
        """
        训练支持向量机模型
        :param data_arr:        样本特征向量矩阵
        :param label_arr:       样本标签值列矩阵
        :param C:               软间隔阈值, C越大约束越强
        :param toler:           相等判断时的阈值
        :param maxIter:         最大迭代次数
        :param ktup:            核模型参数
        :return:                返回b和alphas
        """
        self.data_mat = np.mat(data_arr)
        self.label_mat = np.mat(label_arr).T
        self.C = C
        self.toler = toler
        self.m = self.data_mat.shape[0]
        self.alphas = np.mat(np.zeros((self.m, 1)))
        self.b = 0
        self.ecache = np.mat(np.zeros((self.m, 2)))  # first column is valid flag
        self.ktup = ktup
        # 矩阵K保存每个样本与其它样本计算的核函数的值
        self.K = np.mat(np.zeros((self.m, self.m)))
        for i in range(self.m):
            self.K[:, i] = self._kernel(self.data_mat, self.data_mat[i, :], ktup)

        iter = 0
        entire_set = True       # 重新开始一轮训练, 遍历每个alpha[i]
        alpha_pairs_changed_num = 0
        while (iter < maxIter) and ((alpha_pairs_changed_num > 0) or (entire_set)):
            alpha_pairs_changed_num = 0
            if entire_set:
                # 遍历每个alpha[i], 逐一进行优化计算
                for i in range(self.m):
                    alpha_pairs_changed_num += self._inner(i)
                    print("fullSet, iter: %d i:%d, pairs changed %d" %
                          (iter, i, alpha_pairs_changed_num))
                iter += 1
            else:
                # 遍历非边界alpha[i]
                non_bounds = np.nonzero((self.alphas.A > 0) * (self.alphas.A < C))[0]
                for i in non_bounds:
                    alpha_pairs_changed_num += self._inner(i)
                    print("non-bound, iter: %d i:%d, pairs changed %d" %
                          (iter, i, alpha_pairs_changed_num))
                iter += 1
            if entire_set:
                entire_set = False
            elif alpha_pairs_changed_num == 0:
                entire_set = True
            print("iteration number: %d" % iter)

        sv_ind = np.nonzero(self.alphas.A > 0)[0]
        self.svs = self.data_mat[sv_ind]
        self.sv_labels = self.label_mat[sv_ind]
        self.sv_indices = sv_ind
        return self.b, self.alphas

    def predict(self, data):
        ke = self._kernel(self.svs, data, self.ktup)
        pred = ke.T * np.multiply(self.sv_labels, self.alphas[self.sv_indices]) + b
        return pred

    def calc_ws(self):
        data_mat = self.data_mat
        label_mat = self.label_mat
        m, n = data_mat.shape
        w = np.zeros((n, 1))
        for i in range(m):
            w += np.multiply(self.alphas[i] * label_mat[i], data_mat[i, :].T)

        return w


def load_dataset(filename):
    data_arr = []
    label_arr = []
    fr = open(filename)
    for line in fr.readlines():
        strs = re.split('\s+', line.strip())
        data_arr.append([float(strs[0]), float(strs[1])])
        label_arr.append(float(strs[2]))
    return data_arr, label_arr

if __name__ == "__main__":
    data_arr, label_arr = load_dataset('testSetRBF.txt')
    svm = SVM()
    b, alphas = svm.fit(data_arr, label_arr, 1000, 0.0001, 10000, ktup=('rbf', 1))
    b = b.flatten().A[0]
    print(b)
    print(alphas)

    v = []
    for i in range(len(alphas)):
        if alphas[i] > 0.0:
            print(data_arr[i], label_arr[i])
            v.append(data_arr[i])
    v = np.array(v)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    data_mat = np.mat(data_arr)
    ax.scatter(data_mat[:, 0].flatten().A[0], data_mat[:, 1].flatten().A[0], c=label_arr, marker='.')

    w = svm.calc_ws()
    split_boundary_func = lambda x: (-b - w[0][0] * x) / w[1][0]
    xx = np.linspace(2.5, 6, 10)
    yy = split_boundary_func(xx)
    #ax.plot(xx, split_boundary_func(xx), c='red')
    ax.scatter(v[:, 0], v[:, 1], marker='o', color='none', edgecolor='blue', s=200)

    errs = []
    for i in range(data_mat.shape[0]):
        pred = svm.predict(data_mat[i, :])
        if np.sign(pred) != np.sign(label_arr[i]):
            errs.append(data_arr[i])

    if len(errs) > 0:
        errs = np.array(errs)
        ax.scatter(errs[:, 0], errs[:, 1], marker='o', color='none', edgecolor='red', s=100)

    plt.show()
