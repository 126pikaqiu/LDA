# -*- encoding: utf-8 -*-
"""
@File    : extract_state.py
@Time    : 2019/4/27 10:14
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
import json
import jieba
def get_distance(loc1,loc2):
    distance1 = 10000000
    for item1 in loc1:
        for item2 in loc2:
            if distance1 > abs(item1-item2):
                distance1 = abs(item2-item1)
    return distance1

if __name__ == "__main__":
    location1 = {}
    location2 = {}
    with open("../res/states.json", "r", encoding='utf-8') as f:
        state = json.load(f)
    states = []
    for value in state.values():
        states += value

    with open("../res/key.json", "r", encoding='utf-8') as f:
        key = json.load(f)
    keys = []
    for value in key.values():
        keys += value

    with open("../res/testsentences.txt", "r", encoding='utf-8') as fp:
        content = fp.read()
    alist = jieba.cut(content)
    for item in alist:
        print(item)
    # for item in alist:
    #     f_item = item.replace("市", "").replace("县", "")
    #     if f_item in states:
    #         if f_item not in location1:
    #             location1[f_item] = []
    #             start = 0
    #         else:
    #             start = location1[f_item][-1]
    #         location1[f_item].append(content.find(f_item, start))
    #     if f_item in keys:
    #         if f_item not in location2 or len(location2[f_item]) == 0:
    #             location2[f_item] = []
    #             start = 0
    #         else:
    #             start = location2[f_item][-1]
    #         if content.find(f_item, start) != 0:
    #             location2[f_item].append(content.find(f_item, start))
    # distance = {}
    # for key1 in location1:
    #     distance[key1] = 100000
    #     for value2 in location2.values():
    #         if distance[key1] > get_distance(location1[key1],value2):
    #             distance[key1] = get_distance(location1[key1],value2)
    # # print(min(distance,key=distance.get))
    # print(distance)
