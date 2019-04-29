# -*- encoding: utf-8 -*-
"""
@File    : filter.py
@Time    : 2019/4/28 21:29
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
import json

class Fiter(object):

    def __init__(self):
        self.alist = None
        self.drugs = []
        self.state = {}
        self.states = []
        self.disease = []
        self.org = []
        self.com = []
        self.result = {}

        self.result["drug"] = []
        self.result["state"] = []
        self.result["org"] = []
        self.result["com"] = []
        self.result["disease"] = []

    def set_alist(self,sequnce):
        self.alist = sequnce.split("/")

    def filter(self):
        self.load_key_words()
        for item in self.alist:
            if item in self.drugs and item not in self.result["drug"]:
                self.result["drug"].append(item)
                continue
            if item.replace("市","").replace("县","") in self.states:
                for key in self.state:
                    if item.replace("市","").replace("县","") in self.state[key] and key + "省（市）" + item not in self.result["state"]:
                        self.result["state"].append(key + "省（市）" + item)
                        break
                continue
            if "病" in item and item not in self.result["disease"]:
                self.result["disease"].append(item)
                continue
            if ("企业" in item or "公司" in item) and item not in self.result["com"]:
                self.result["com"].append(item)
                continue
            if "院" in item and item not in self.result["org"]:
                self.result["org"].append(item)
        return self.result


    def load_key_words(self):
        with open("../res/states.json", "r", encoding='utf-8') as f:
            self.state = json.load(f)
        self.states = []
        for value in self.state.values():
            self.states += value
        with open("../res/userdict.txt","r", encoding='utf-8') as f:
            content = f.readlines()
        self.drugs = [item.split(" ")[0] for item in content]


