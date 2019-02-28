import trees
import treePlotter

def test():
    myDat, labels = trees.createDataSet()
    print myDat
    response = trees.calcShannonEnt(myDat)
    myDat[0][-1] = 'maybe'
    print trees.calcShannonEnt(myDat),'dd'
    return response

def test2():
    myDat, labels = trees.createDataSet()
    res = trees.splitDataSet(myDat, 0, 1)
    res2 = trees.splitDataSet(myDat, 0, 0)
    res3 = trees.splitDataSet(myDat, 1, 1)
    res4 = trees.splitDataSet(myDat, 1, 0)
    return res, '\n', res2, '\n', res3, '\n', res4

def test3():
    myDat, labels = trees.createDataSet()
    res = trees.chooseBestFeatureToSplit(myDat)
    return res

def test4():
    myDat, labels = trees.createDataSet()
    res = trees.createTree(myDat, labels)
    return res



if __name__ == '__main__':
    # print test()
    # print test2()
    # print test3()
    # print test4()
    treePlotter.createPlot()
