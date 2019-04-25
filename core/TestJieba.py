# -*- encoding: utf-8 -*-
"""
@File    : TestJieba.py
@Time    : 2019/4/25 20:29
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
import jieba


class TestJieba(object):

    def __init__(self, path=None, sentence=None):
        """
        initialize the sentence , the path of the file stopwords
        and the separator.
        :param sentence: the sentence to be handle
        """
        self.stop_file_path = "../res/stopwords.txt"
        self.separator = "/"
        if path:
            self.sentence = self.read_file(path)
        else:
            self.sentence = sentence

    def set_sentence(self, sentence):
        """
        :param sentence: the sentence to be handle
        :return:
        """
        self.sentence = sentence

    def stop_words_list(self):
        """
        :return: a list of stop words
        """
        stopwords = [line.strip() for line in open(self.stop_file_path, 'r', encoding='utf-8').readlines()]
        return stopwords

    def filter_list(self, sequence):
        """
        to filter the sequence with some stop words.
        :param sequence: the separated sequence.
        :return:
        """
        stopwords = self.stop_words_list()
        outstr = ""
        for word in sequence:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += self.separator
        return outstr

    def cut(self, cut_all=False, HMM=True):
        """
        to call the method cut of jieba.
        :param cut_all: whether  to use the whole model.
        :param HMM: whether to use HMM.
        :return:
        """
        return self.filter_list(jieba.cut(self.sentence, cut_all=cut_all, HMM=HMM))

    def cut_for_search(self):
        """
        to call the method cut_for_search of jieba.
        :return:
        """
        return self.filter_list(jieba.cut_for_search(self.sentence))

    def load_userdict(self, path):
        """
        to call the method load_userdict of jieba.
        :return:
        """
        jieba.load_userdict(path)

    def read_file(self,path):
        """
        to read a file and return the content
        :param path: the path of a file
        :return:
        """
        fp = open(path, "r", encoding='utf8', errors='ignore')
        content = fp.read()
        fp.close()
        return content

