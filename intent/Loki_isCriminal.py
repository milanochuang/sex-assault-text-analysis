#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for isCriminal

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
def check_attempted(args):
    if args[-1][0:2] == "未遂":
        return 1
    else:
        return 0

DEBUG_isCriminal = True
userDefinedDICT = {"人": ["女", "女子", "之人", "之女子", "證人", "代號00000000A", "代號00000000B", "代號00000000C", "代號00000000D", "代號00000000", "代號0000-0000A", "代號0000-0000B", "代號0000-0000C", "代號0000-0000D", "代號0000-000000", "代號00000000000", "代號0000甲000000", "0000甲000000A"], "罪": ["未遂罪"], "成年": ["成年人"], "甲○○": ["甲男", "乙男", "丙男", "丁男", "戊男", "己男", "庚男", "辛男", "壬男", "癸男", "甲○○", "乙○○", "丙○○", "丁○○", "戊○○", "己○○", "庚○○", "辛○○", "壬○○", "癸○○", "陳○○", "林○○", "王○○", "李○○", "張○○", "黃○○", "吳○○", "劉○○", "蔡○○", "楊○○", "許○○", "鄭○○", "謝○○", "郭○○", "洪○○", "邱○○", "曾○○", "賴○○", "廖○○", "徐○○", "周○○", "葉○○", "蘇○○", "莊○○", "呂○○"], "攜帶兇器": ["侵入住宅", "以藥劑", "對被害人施以凌虐"], "精神障礙": ["心智缺陷", "身體障礙", "未滿十四歲", "少年"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_isCriminal:
        print("[isCriminal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[楊智皓][成年人][故意]對[少年]犯強制性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['under_18'] = 1
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓][攜帶兇器]對[精神障礙][人]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[1]
        resultDICT['victim'].append(args[2])
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓]對[精神障礙][之人]犯[攜帶兇器]強制性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[3]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓]對[精神障礙][之女子]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[1])
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓]對[身體障礙]及[心智缺陷][之人]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[1])
        resultDICT['victim'].append(args[2])
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓]犯[攜帶兇器]強制性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[1]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[楊智皓]犯強制性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○][成年人][故意]對[少年]犯[強制]性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['under_18'] = 1
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○][攜帶兇器]對[精神障礙][人]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[2])
        resultDICT['addition'] = args[1]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○]對[精神障礙][之人]犯[攜帶兇器]強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[1])
        resultDICT['addition'] = args[3]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○]對[精神障礙][之女子]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[1])
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○]對[身體障礙]及[心智缺陷][之人]犯強制性交[罪]":
        # write your code here
        resultDICT['victim'] = []
        resultDICT['criminal'] = args[0]
        resultDICT['victim'].append(args[1])   
        resultDICT['victim'].append(args[2])     
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○]犯[攜帶兇器]強制性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[1]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○]犯[強制]性交[罪]":
        # write your code here
        print(1)
        resultDICT['criminal'] = args[0]
        resultDICT['attempted'] = check_attempted(args)
        pass

    if utterance == "[甲○○][成年人][故意]對[少年]犯[攜帶兇器][強制]性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[1]
        resultDICT['attempted'] = check_attempted(args)
        pass
    if utterance == "[楊智皓][成年人][故意]對[少年]犯[攜帶兇器][強制]性交[罪]":
        # write your code here
        resultDICT['criminal'] = args[0]
        resultDICT['addition'] = args[1]
        resultDICT['attempted'] = check_attempted(args)
        pass
    return resultDICT