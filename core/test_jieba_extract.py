# -*- encoding: utf-8 -*-
"""
@File    : test_jieba_extract.py
@Time    : 2019/4/25 19:51
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
import jieba.analyse
import jieba.posseg as pseg
if __name__ == '__main__':
    # 字符串前面加u表示使用unicode编码
    content = u'西安市中国特色社会主义是我们党领导的伟大事业，广东全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'

    # 第一个参数：待提取关键词的文本
    # 第二个参数：返回关键词的数量，重要性从高到低排序
    # 第三个参数：是否同时返回每个关键词的权重
    # 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
    # keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
    # print("+TF-IDF algorithm-----------------")
    # # 访问提取结果
    # for item in keywords:
    #     # 分别为关键词和相应的权重
    #     print(item[0], item[1])

    # 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
    # 即仅提取地名、名词、动名词、动词
    keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns'))
    print("\nTextRank algorithm-----------------")
    # 访问提取结果
    for item in keywords:
        # 分别为关键词和相应的权重
        print(item[0], item[1])
    #
    # words = pseg.cut(content)
    # for word, flag in words:
    #     # 格式化模版并传入参数
    #     print('%s, %s' % (word, flag))
