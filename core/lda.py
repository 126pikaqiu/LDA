# -*- encoding: utf-8 -*-

"""
@File    : lda.py
@Time    : 2019/4/25 20:59
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""

# from gensim import corpora, models
# import jieba.posseg as jp, jieba
from core.LDAC import LDA
import json
from core.TestJieba import TestJieba
from core.filter import Fiter
if __name__ == "__main__":
    # 文本集
    outfilename = "../res/testsentences.txt"
    userdict = "../res/testsentences.txt"
    with open(outfilename, 'r', encoding='UTF-8') as fp:
        content = fp.read()
    with open("../res/key.json", "r", encoding='utf-8') as f:
        key = json.load(f)
    keys = []
    for value in key.values():
                keys += value
    lines = ""
    for line in content.split("\n"):
        for sentence in line.split("。"):
            for one in keys:
                if sentence.find(one) != -1:
                    lines += sentence + "。"
                    break

    lda = LDA()
    lda.set_sentences([lines])
    topic = lda.analyse()
    jieba_u = TestJieba(sentence=topic)
    jieba_u.load_userdict(userdict)
    alist = jieba_u.cut()
    print(alist)
    filter_u = Fiter()
    filter_u.set_alist(alist)
    print(filter_u.filter())