#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for isDating

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_isDating = True
userDefinedDICT = {"人": ["女", "女子", "之人", "之女子", "證人", "代號00000000A", "代號00000000B", "代號00000000C", "代號00000000D", "代號00000000", "代號0000-0000A", "代號0000-0000B", "代號0000-0000C", "代號0000-0000D", "代號0000-000000", "代號00000000000", "代號0000甲000000", "0000甲000000A"], "罪": ["未遂罪"], "成年": ["成年人"], "甲○○": ["甲男", "乙男", "丙男", "丁男", "戊男", "己男", "庚男", "辛男", "壬男", "癸男", "甲○○", "乙○○", "丙○○", "丁○○", "戊○○", "己○○", "庚○○", "辛○○", "壬○○", "癸○○", "陳○○", "林○○", "王○○", "李○○", "張○○", "黃○○", "吳○○", "劉○○", "蔡○○", "楊○○", "許○○", "鄭○○", "謝○○", "郭○○", "洪○○", "邱○○", "曾○○", "賴○○", "廖○○", "徐○○", "周○○", "葉○○", "蘇○○", "莊○○", "呂○○"], "攜帶兇器": ["侵入住宅", "以藥劑", "對被害人施以凌虐"], "精神障礙": ["心智缺陷", "身體障礙", "未滿十四歲", "少年"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_isDating:
        print("[isDating] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "並非[男][女朋友]":
        # write your code here
        pass

    if utterance == "以[男][女朋友]":
        # write your code here
        pass

    if utterance == "為[男][女朋友]":
        # write your code here
        pass

    return resultDICT