#-*-coding:utf-8-*- 
from math import log
import operator

#创建数据集
def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet, labels

#计算香农熵
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    #为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel=featVec[-1]
        #如果不存在keys，创建key
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    #shannon熵为0
    shannonEnt=0.0
    for key in labelCounts:
        #计算概率
        prob=float(labelCounts[key])/numEntries
        #以2为底求对数
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

#划分数据集
def splitDataSet(dataSet,axis,value):
    #创建新的list对象
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            #互换顺序
            reduceFeatVec=featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        #计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            #计算最好的信息增益
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def majortyCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    #类别完全相同的就停止划分(全yes/no/maybe)
    if classList.count(classList[0])==len(classList):
        return classList[0]
    #（以下两行）遍历完所有特征时返回出现次数最多的
    if len(dataSet[0])==1:
        return majoryCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    # 得到列表包含的所有属性值
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree
