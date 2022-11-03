import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# matplotlib 的 backend的默认渲染器是agg，agg是一个没有图形显示界面的终端，如果要图像正常显示，则需要切换为图形界面显示的终端TkAgg


# 对数几率回归分类器
class LogisticRegression(object):

    def __init__(self, learning_rate=0.1, max_iter=100, seed=None):
        self.seed = seed
        self.lr = learning_rate
        self.max_iter = max_iter
        self.w = None
        self.b = None
        self.x = None
        self.y = None

    # 迭代训练
    def fit(self, x, y):
        np.random.seed(self.seed)
        self.w = np.random.normal(loc=0.0, scale=1.0, size=x.shape[1])
        self.b = np.random.normal(loc=0.0, scale=1.0)
        self.x = x
        self.y = y
        for i in range(self.max_iter):
            self._update_step()
            # print('loss: \t{}'.format(self.loss()))
            # print('score: \t{}'.format(self.score()))
            # print('w: \t{}'.format(self.w))
            # print('b: \t{}'.format(self.b))

    def _sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def _f(self, x, w, b):
        z = x.dot(w) + b
        return self._sigmoid(z)

    def predict_proba(self, x=None):
        if x is None:
            x = self.x
        y_pred = self._f(x, self.w, self.b)
        return y_pred

    def predict(self, x=None):
        if x is None:
            x = self.x
        y_pred_proba = self._f(x, self.w, self.b)
        y_pred = np.array([0 if y_pred_proba[i] < 0.5 else 1 for i in range(len(y_pred_proba))])
        return y_pred

    def score(self, y_true=None, y_pred=None):
        if y_true is None or y_pred is None:
            y_true = self.y
            y_pred = self.predict()
        acc = np.mean([1 if y_true[i] == y_pred[i] else 0 for i in range(len(y_true))])
        return acc

    def loss(self, y_true=None, y_pred_proba=None):
        if y_true is None or y_pred_proba is None:
            y_true = self.y
            y_pred_proba = self.predict_proba()
        return np.mean(-1.0 * (y_true * np.log(y_pred_proba) + (1.0 - y_true) * np.log(1.0 - y_pred_proba)))

    def _calc_gradient(self):
        y_pred = self.predict_proba()
        d_w = (y_pred - self.y).dot(self.x) / len(self.y)
        d_b = np.mean(y_pred - self.y)
        return d_w, d_b

    def _update_step(self):
        d_w, d_b = self._calc_gradient()
        self.w -= self.lr * d_w
        self.b -= self.lr * d_b
        return self.w, self.b


# 生成数据集
def generate_dataset(seed):
    np.random.seed(seed)
    data_size_1 = 300
    x1_1 = np.random.normal(loc=5.0, scale=1.0, size=data_size_1)
    x2_1 = np.random.normal(loc=4.0, scale=1.0, size=data_size_1)
    y_1 = [0] * data_size_1
    data_size_2 = 400
    x1_2 = np.random.normal(loc=10.0, scale=2.0, size=data_size_2)
    x2_2 = np.random.normal(loc=8.0, scale=2.0, size=data_size_2)
    y_2 = [1] * data_size_2
    x1 = np.concatenate((x1_1, x1_2), axis=0)
    x2 = np.concatenate((x2_1, x2_2), axis=0)
    x = np.hstack((x1.reshape(-1, 1), x2.reshape(-1, 1)))
    y = np.concatenate((y_1, y_2), axis=0)
    data_size_all = data_size_1 + data_size_2

    # 随机打乱样本点顺序
    shuffled_index = np.random.permutation(data_size_all)
    x = x[shuffled_index]
    y = y[shuffled_index]
    return x, y


# 将数据集分成训练和测试集
def train_test_split(x, y):
    split_index = int(len(y) * 0.7)
    x_train = x[:split_index]
    y_train = y[:split_index]
    x_test = x[split_index:]
    y_test = y[split_index:]
    return x_train, y_train, x_test, y_test


if __name__ == "__main__":
    # 产生数据集
    x, y = generate_dataset(seed=272)
    x_train, y_train, x_test, y_test = train_test_split(x, y)

    # 数据归一化
    x_train = (x_train - np.min(x_train, axis=0)) / (np.max(x_train, axis=0) - np.min(x_train, axis=0))
    x_test = (x_test - np.min(x_test, axis=0)) / (np.max(x_test, axis=0) - np.min(x_test, axis=0))

    # 训练对数几率回归分类器
    clf = LogisticRegression(learning_rate=0.1, max_iter=500, seed=272)
    clf.fit(x_train, y_train)

    # 拟合分界线
    split_boundary_func = lambda x: (-clf.b - clf.w[0] * x) / clf.w[1]
    xx = np.arange(0.1, 0.6, 0.1)
    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, marker='.')
    plt.plot(xx, split_boundary_func(xx), c='red')
    plt.show()

    # 输出测试集上的损失
    y_test_pred = clf.predict(x_test)
    y_test_pred_proba = clf.predict_proba(x_test)
    print(clf.score(y_test, y_test_pred))
    print(clf.loss(y_test, y_test_pred_proba))
    # print(y_test_pred_proba)