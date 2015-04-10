#-*-coding:utf-8-*- 
from math import log

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
            reduceFeatVec=fecVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
            
