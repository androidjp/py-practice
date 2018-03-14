from os import listdir
from numpy import *

from ml.algorithm.kNN import kNN
from ml.common.FileUtil import *


def handwritingClassTest():
    trainingLabels = []
    trainingFileList = listdir('./../../data/digits/trainingDigits')
    fileCount = len(trainingFileList)
    # 二维矩阵，每一行1024的特征
    trainingMatrix = zeros((fileCount, 1024))
    for i in range(fileCount):
        # 拿到每一个文件
        fileNameStr = trainingFileList[i]
        # 根据文件名，拿到标签值
        itemLabel = int(fileNameStr.split('_')[0])
        trainingLabels.append(itemLabel)
        trainingMatrix[i, :] = img2vector('./../../data/digits/trainingDigits/%s' % fileNameStr)
    # 测试数据
    testFileList = listdir('./../../data/digits/testDigits')
    errorCount = 0
    testCount = len(testFileList)
    for i in range(testCount):
        fileNameStr = testFileList[i]
        correctLabel = int(fileNameStr.split('_')[0])
        testDataItem = img2vector('./../../data/digits/testDigits/%s' % fileNameStr)
        classifierResult = kNN.classify0(testDataItem, trainingMatrix, trainingLabels, 3)
        print('分类结果是：', classifierResult, ', 而正确答案是：', correctLabel)
        if classifierResult != correctLabel:
            errorCount += 1
    print('最终错误率：', 100*(errorCount / float(testCount)), '%')


handwritingClassTest()