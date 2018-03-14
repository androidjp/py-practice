import numpy as np


def file2matrix(filename):
    with open(filename) as fr:
        arrayOLines = fr.readlines()
        numberOfLines = len(arrayOLines)
        returnMat = np.zeros((numberOfLines, 3))
        classLabelVector = []
        index = 0
        for line in arrayOLines:
            # 相当于 trim()
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index, :] = listFromLine[0:3]
            # get last param (the label)
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
    return returnMat, classLabelVector


def img2vector(filename):
    returnVector = np.zeros((1, 1024))
    with open(filename) as fr:
        # 32x32 img
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVector[0, 32 * i + j] = int(lineStr[j])
    return returnVector
