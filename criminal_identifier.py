#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import json
try:
    from intent import Loki_isCriminal
except:
    from .intent import Loki_isCriminal


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "milanochuang@gmail.com"
LOKI_KEY = "OKWq*yYR%1e6&F#fuvjGZyusWXqaHlY"
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # isCriminal
                if lokiRst.getIntent(index, resultIndex) == "isCriminal":
                    resultDICT = Loki_isCriminal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

def change_name(inputSTR):
  pronounLIST = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "丑", "寅", "卯", "辰", "巳", "午", "申", "酉", "戌", "亥"]
  genderLIST = ["男", "女"]
  aliasLIST = ["○○○", "◯◯◯", "○○", "◯◯"]
  pronoun = None
  alias = None
  gender = None
  status = 0
  if bool([pronoun for pronoun in pronounLIST if pronoun in inputSTR]):
    pronoun = [pronoun for pronoun in pronounLIST if pronoun in inputSTR]
    status = 1
    for i in pronoun:
      inputSTR = inputSTR.replace(i, "王", 1)
  if bool([gender for gender in genderLIST if gender in inputSTR]):
    gender = [gender for gender in genderLIST if gender in inputSTR][0]
    inputSTR = inputSTR.replace(gender, "小明", 1)
  if bool([alias for alias in aliasLIST if alias in inputSTR]):
    alias = [alias for alias in aliasLIST if alias in inputSTR][0]
    inputSTR = inputSTR.replace(alias, "小明")
  return inputSTR, status, pronoun, alias, gender

if __name__ == "__main__":
    # isCriminal
    # print("[TEST] isCriminal")
    # inputLIST = ['王小明犯強制性交罪','王小明攜帶兇器犯強制性交罪','王小明犯攜帶兇器強制性交罪','王小明對精神障礙之人犯強制性交罪','王小明成年人故意對少年犯強制性交罪','王小明對精神障礙之人犯攜帶兇器強制性交罪','王小明成年人對未滿十八歲之人犯強制性交罪','王小明攜帶兇器對精神障礙之人犯強制性交罪','王小明對身體障礙及心智缺陷之人犯強制性交罪','王小明成年人故意對少年犯攜帶兇器強制性交罪','王小明成年人故意對未滿十八歲之少年犯強制性交罪']
    # testLoki(inputLIST, ['isCriminal'])
    # print("")

    # 輸入其它句子試看看
    inputSTR = change_name("蘇○○成年人對少年犯乘機猥褻罪，處有期徒刑柒月。曾○○成年人對少年犯強制性交罪，處有期徒刑參年貳月")
    inputLIST = [inputSTR]
    # print(change_name("蘇○○成年人對少年犯乘機猥褻罪，處有期徒刑柒月。曾○○成年人對少年犯強制性交罪，處有期徒刑參年貳月"))
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))