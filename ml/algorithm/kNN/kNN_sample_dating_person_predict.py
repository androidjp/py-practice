import ml.algorithm.kNN.kNN as kNN
import numpy as np
import ml.common.FileUtil as FileUtil

# 例子一：改进约会网站的配对效果

print('===================================')
print('[1. prepare data]')
print('------')

# datingDataMat = (每年获得的飞行常客里程数, 玩视频游戏所占时间百分比, 每周消费的冰淇淋公升数)
# datingLabels = 标签：三类人： 不喜欢的人，魅力一般的人，极具魅力的人
datingDataMat, datingLabels = FileUtil.file2matrix('./../../data/datingTestSet2.txt')

print('===================================')
print('[2. analyse data]')
print('------')

# 创建散点图
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
plt.show()

print('===================================')
print('[3. prepare data [归一化数值]]')
print('------')
from ml.common.AutoNorm import *
# resultDatingDataMat, ranges, minVals = autoNorm(datingDataMat)
# print(resultDatingDataMat)
print('===================================')
print('[4. verify the classifier]')
print('------')

def datingClassTest():
    hoRatio = 0.50  # hold out 10%
    datingDataMat, datingLabels = FileUtil.file2matrix('./../../data/datingTestSet2.txt')  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    # 从 100~1000是训练数据集， 而从1~99 测试数据
    for i in range(numTestVecs):
        classifierResult = kNN.classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount * 100 / float(numTestVecs), '%概率 会出错')
    pass


datingClassTest()


print('===================================')
print('[5. OK, now build the complete predict function]')
print('------')

def classifyPerson():
    resultList = ['I don\'t like him', 'I think he is ordinary', 'Oh, his kind is my love.']
    percentTats = float(input('他玩游戏时间占比：'))
    ffMiles = float(input('他一年飞多少英里：'))
    iceCream = float(input('他一年吃多少雪糕：'))
    datingDataMat, datingLabels = FileUtil.file2matrix('./../../data/datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = kNN.classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print('I give you the result :', resultList[classifierResult - 1])


classifyPerson()
