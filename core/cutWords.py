# -*- encoding: utf-8 -*-
"""
@File    : cutWords.py
@Time    : 2019/4/25 18:22
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
# import jieba
# jieba.load_userdict("./res/userdict.txt")
#
# # jieba.add_word('石墨烯')
# # jieba.add_word('凱特琳')
# # jieba.del_word('自定义词')
#
# test_sent = (
# "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
# "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
# "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
# )
# words = jieba.cut(test_sent)
# print('/'.join(words))

from core.TestJieba import TestJieba


if __name__ == "__main__":
    test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
    )
    testjieba = TestJieba(sentence=test_sent)
    testjieba.load_userdict("../res/userdict.txt")
    print(testjieba.cut())