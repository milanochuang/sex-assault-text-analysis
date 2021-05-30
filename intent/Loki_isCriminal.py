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

DEBUG_isCriminal = True
userDefinedDICT = {"人": ["女子", "少年", "少女"], "罪": ["未遂罪"], "少年": ["少女"], "王小明": ["甲男", "乙男", "丙男", "丁男", "戊男", "己男", "庚男", "辛男", "壬男", "癸男", "甲○○", "乙○○", "丙○○", "丁○○", "戊○○", "己○○", "庚○○", "辛○○", "壬○○", "癸○○", "陳○○", "林○○", "王○○", "李○○", "張○○", "黃○○", "吳○○", "劉○○", "蔡○○", "楊○○", "許○○", "鄭○○", "謝○○", "郭○○", "洪○○", "邱○○", "曾○○", "賴○○", "廖○○", "徐○○", "周○○", "葉○○", "蘇○○", "莊○○", "呂○○"], "攜帶兇器": ["侵入住宅", "以藥劑", "對被害人施以凌虐"], "精神障礙": ["心智缺陷", "身體障礙", "未滿十四歲", "未滿十八歲", "未滿14歲", "未滿18歲"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_isCriminal:
        print("[isCriminal] {} ===> {}".format(inputSTR, utterance))

def check_attempted(args):
    if args[-1][0:2] == "未遂":
        return 1
    else:
        return 0

def check_plaintiff_feature(*args):
  status = 0
  for i in args:
    for j in i:
      if '女' in j:
        status = 1
      elif '未滿' in j:
        status = 1
  return status

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT['defendent_feature'] = []
    resultDICT['plaintiff_feature'] = []
    if utterance == "[王小明][攜帶兇器]對[精神障礙]之[人]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[1])
        resultDICT['plaintiff_feature'].append(args[2])
        resultDICT['under_18'] = check_plaintiff_feature(args[2])
        resultDICT['isWoman'] = check_plaintiff_feature(arg[3])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明][攜帶兇器]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[1])
        resultDICT['plaintiff_feature'] = None
        resultDICT['under_18'] = 0
        resultDICT['isWoman'] = None
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]對[精神障礙]之[人]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'].append(args[1])
        resultDICT['under_18'] = check_plaintiff_feature(args[1])
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]對[精神障礙]之[人]犯[攜帶兇器][強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[3])
        resultDICT['plaintiff_feature'].append(args[1])
        resultDICT['under_18'] = check_plaintiff_feature(args[1])
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]對[身體障礙]及[心智缺陷]之[人]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'].append(args[1])
        resultDICT['plaintiff_feature'].append(args[2])
        resultDICT['under_18'] = check_plaintiff_feature(args[1:3])
        resultDICT['isWoman'] = check_plaintiff_feature(args[3])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]成年人[故意]對[少年]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'].append(args[2])
        resultDICT['under_18'] = 1
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]成年人[故意]對[少年]犯[攜帶兇器][強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[3])
        resultDICT['plaintiff_feature'].append(args[2])
        resultDICT['under_18'] = 1
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]成年人[故意]對[未滿十八歲]之[少年]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'].append(args[2])
        resultDICT['under_18'] = 1
        resultDICT['isWoman'] = check_plaintiff_feature(args[3])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]成年人對[未滿十八歲]之[人]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'].append(args[1])
        resultDICT['under_18'] = 1
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]犯[強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = None
        resultDICT['plaintiff_feature'] = None
        resultDICT['under_18'] = 0
        resultDICT['isWoman'] = None
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]犯[攜帶兇器][強制]性交[罪]":
        # write your code here
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[1])
        resultDICT['plaintiff_feature'] = None
        resultDICT['under_18'] = 0
        resultDICT['isWoman'] = None
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]對[精神障礙]之[人][攜帶兇器]犯[強制]性交[罪]":
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'].append(args[3])
        resultDICT['plaintiff_feature'].append(args[1])
        resultDICT['under_18'] = check_plaintiff_feature(args[1])
        resultDICT['isWoman'] = check_plaintiff_feature(args[2])
        resultDICT['attempt'] = check_attempted(args)
        pass

    if utterance == "[王小明]犯二人以上[共同][強制]性交[罪]":
        print(args[0])
        resultDICT['defendent'] = args[0]
        resultDICT['defendent_feature'] = "二人共同犯罪"
        resultDICT['plaintiff_feature'] = None
        resultDICT['under_18'] = None
        resultDICT['isWoman'] = None
        resultDICT['attempt'] = check_attempted(args)
        pass
    if utterance == "[王小明]、[王小明]二人以上[共同][攜帶兇器]犯[強制]性交而凌虐[罪]":
        resultDICT['defendent'] = []
        print(args[0])
        resultDICT['defendent'].append(args[0])
        resultDICT['defendent'].append(args[1])
        resultDICT['defendent_feature'] = "二人共同犯罪"
        resultDICT['plaintiff_feature'] = args[3]
        resultDICT['under_18'] = None
        resultDICT['isWoman'] = None
        resultDICT['attempt'] = check_attempted(args)
        pass
    return resultDICT