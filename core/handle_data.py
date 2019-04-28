# -*- encoding: utf-8 -*-
"""
@File    : handle_data.py
@Time    : 2019/4/26 18:31
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
import json
# def filter(str):
#     outstr = ""
#     for word in str:
#             if not word.isdigit():
#                 outstr += word
#     return outstr.replace("地级市","").replace("县级市", "").replace("—","").replace("，","").replace("\n","")
#
if __name__ == "__main__":
    states = {}
    content = ' 供货紧张  供应中断  缺货  停产  缺药  一药难求  供货不足  库存数量  断供  买不到  性命攸关  储备药  供货跟不上  药贩子  救命稻草  物以稀为贵  价格飙升  现在已涨到  严重偏低  断货  捆绑销售  暴涨缺货  采购困难  可替代  涨幅  涨价  救命药  缺少  困境  药品不能满足  暴涨  药荒  临床紧缺药品  供应短缺  急抢救用的短缺药  垄断原料药  买不到  短缺药品  困局  短缺  进不到药  不进货  难觅踪影  临床短缺药  临床急需药品  无法正常供应  难以买到  很难在药店里买到  不能正常供应  供不应求  廉价药短缺  医院没药  缺失'
    # with open('../res/provincestates.txt', 'r',encoding='utf-8') as f:
    #     lists = f.readlines()
    # for item in lists:
    #     key = filter(item.split("：")[0])
    #     states[key] = [key]
    #     for value in item.split("：")[1].split("、"):
    #         if value != "\n":
    #             states[key].append(filter(value))
    # son_str = json.dumps(states,ensure_ascii=False)
    states["key"] = []
    for item in content.split(" "):
        states["key"].append(item)
    son_str = json.dumps(states,ensure_ascii=False)
    with open("../res/key.json","w+",encoding='utf-8') as f:
        f.write(son_str)
# if __name__ == "__main__":
#     with open("../res/states.json","r",encoding='utf-8') as f:
#             state = json.load(f)
#     states = []
#     for value in state.values():
#         states += value
#     print(states)
    # for item in states:
    #     print(item + ":" + ",".join(states[item]))