import kNN
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def test():
    group, labels = kNN.createDataSet()
    print group
    print group.shape[0]
    print labels

    print kNN.classify0([0, 0], group, labels, 3)


def test2():
    datingDataMat, datingLabels = kNN.file2matrix('./f150_envelope.csv')
    # print datingLabels, 'lllllllll'
    # print datingDataMat, 'mmmmmmmmm'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
               15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
    plt.show()

def test3():
    datingDataMat, datingLabels = kNN.file2matrix('./f150_envelope.csv')
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    print normMat, 'nnnnnnnnnn'
    print ranges, 'rrrrrrrr'
    print minVals, 'mmmmmmmm'


if __name__ == '__main__':
    # kNN.datingClassTest()
    # kNN.classifyPerson()
    # kNN.img2vector('./test.txt')
    kNN.handwritingClassTest()