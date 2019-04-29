# -*- encoding: utf-8 -*-
"""
@File    : LDAC.py
@Time    : 2019/4/28 21:11
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
from gensim import corpora,models

class LDA(object):
    def __init__(self):
        self.sentences = None

    def set_sentences(self,sentences):
        self.sentences = sentences

    def analyse(self):
        words_list = []

        for lines in self.sentences:
            lines = lines.replace("\n", "").split()
            words_list.append(lines)

        dictionary = corpora.Dictionary(words_list)
        # 基于词典，使【词】→【稀疏向量】，并将向量放入列表，形成【稀疏向量集】
        corpus = [dictionary.doc2bow(words) for words in words_list]
        # lda模型，num_topics设置主题的个数
        lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=6)
        topic1 = ""
        # 打印所有主题，每个主题显示4个词
        for topic in lda.print_topics(num_words=1):
            topic1 += topic[1]
        return topic1
