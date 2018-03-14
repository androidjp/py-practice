# k-近邻算法
import numpy as np
import operator


# create data source
def createDataSet():
    group = np.array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]], dtype=float)

    labels = ['A', 'A', 'B', 'B']

    return group, labels


# classify function

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    # get distance
    # tile(a, (row,col)) 表示将 a copy row行 col列
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2

    # axis =1 表示列之间相加
    sqDistances = sqDiffMat.sum(axis=1)

    distances = sqDistances ** 0.5

    # argsort()表示值从小到大排序，并最终返回排好序的索引列表
    sortedDisIndicies = distances.argsort()

    classCount = {}
    # choice the most close k points
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # sort

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

