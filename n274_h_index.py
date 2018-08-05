from collections import Counter

def Hindex(indexList):
    #构建引用次数与文章篇数的映射
    HCounter = Counter(indexList)
    #逆序字典，让引用次数高的引用次数排在前面
    ReversedCounter = sorted(HCounter.iteritems(), reverse = True)
    #分别生成 引用次数列表CounterKeys 和 该引用次数的文章列表CounterValues
    CounterKeys = [i[0] for i in ReversedCounter ]
    CounterValues = [i[1] for i in ReversedCounter]
    #CounterKeys，CounterValues根据索引值一一对应，遍历索引值
    for index in range(0,len(CounterValues)):
        #sum(CounterValues[0:index+1])为大于等于某个索引值——CounterKeys[index]的所有的文章总和
        if CounterKeys[index] <= sum(CounterValues[0:index+1]):
            break
    return CounterKeys[index]