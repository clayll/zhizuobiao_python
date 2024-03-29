import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm


class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype



data = []
with open('./data/event.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
# 变成数组后做转置,删除水平方向第0行(就是日期这列)；1代表日期，0是星期
data = np.delete(np.array(data).T, 1, 0)
encoders, x = [], []
for row in range(len(data)):
    # 判断是不是数字
    if data[row, 0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)

x = np.array(x).T
# print(x.shape)    #5040行 4列
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=5)

model = svm.SVC(kernel='rbf', class_weight='balanced')

print(ms.cross_val_score(model, x, y, cv=3, scoring='f1_weighted').mean())
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)

print((pred_test_y == test_y).sum() / pred_test_y.size)

# 混淆矩阵
print(sm.confusion_matrix(test_y, pred_test_y))

print(sm.classification_report(test_y, pred_test_y))


data = [['Tuesday', '12:30:00', '21', '23']]

data = np.array(data).T

x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))

x = np.array(x).T

pred_y = model.predict(x)

print(encoders[-1].inverse_transform(pred_y))

# 输出最后为['noevent']，无事件
