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
try:
    from intent import Loki_relationship_check
    from intent import Loki_isDating
    from intent import Loki_isCoworker
    from intent import Loki_isMassage
    from intent import Loki_isCriminal
except:
    from .intent import Loki_relationship_check
    from .intent import Loki_isDating
    from .intent import Loki_isCoworker
    from .intent import Loki_isMassage
    from .intent import Loki_isCriminal


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "milanochuang@gmail.com"
LOKI_KEY = ""
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
                # relationship_check
                if lokiRst.getIntent(index, resultIndex) == "relationship_check":
                    resultDICT = Loki_relationship_check.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # isDating
                if lokiRst.getIntent(index, resultIndex) == "isDating":
                    resultDICT = Loki_isDating.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # isCoworker
                if lokiRst.getIntent(index, resultIndex) == "isCoworker":
                    resultDICT = Loki_isCoworker.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # isMassage
                if lokiRst.getIntent(index, resultIndex) == "isMassage":
                    resultDICT = Loki_isMassage.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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


if __name__ == "__main__":
    # # relationship_check
    # print("[TEST] relationship_check")
    # inputLIST = ['與A女','甲男與被告','甲男與乙證人','羅文彬與被告','羅文彬與乙證人','羅文彬於民國99年間透過網路交友網站結識代號00000000000號之成年女子']
    # testLoki(inputLIST, ['relationship_check'])
    # print("")

    # # isDating
    # print("[TEST] isDating")
    # inputLIST = ['以男女朋友','係男女朋友','為男女朋友','並非男女朋友']
    # testLoki(inputLIST, ['isDating'])
    # print("")

    # # isCoworker
    # print("[TEST] isCoworker")
    # inputLIST = ['同事之關係','僅為同事關係','原為同事關係','僅為普通之工作同事關係']
    # testLoki(inputLIST, ['isCoworker'])
    # print("")

    # # isMassage
    # print("[TEST] isMassage")
    # inputLIST = ['按摩後','預約按摩','幫甲女按摩','跨坐背上按摩']
    # testLoki(inputLIST, ['isMassage'])
    # print("")

    # # isCriminal
    # print("[TEST] isCriminal")
    # inputLIST = ['楊智皓犯強制性交罪','甲○○犯強制性交罪','楊智皓犯攜帶兇器強制性交罪','甲○○犯攜帶兇器強制性交罪','楊智皓對精神障礙之女子犯強制性交罪','楊智皓成年人故意對少年犯強制性交罪','甲○○對精神障礙之女子犯強制性交罪','甲○○成年人故意對少年犯強制性交罪','楊智皓攜帶兇器對精神障礙人犯強制性交罪','甲○○攜帶兇器對精神障礙人犯強制性交罪','楊智皓對精神障礙之人犯攜帶兇器強制性交罪','甲○○對精神障礙之人犯攜帶兇器強制性交罪','楊智皓對身體障礙及心智缺陷之人犯強制性交罪','甲○○對身體障礙及心智缺陷之人犯強制性交罪']
    # testLoki(inputLIST, ['isCriminal'])
    # print("")

    # 輸入其它句子試看看
    inputLIST = ["戊○○成年人故意對少年犯強制性交罪，處有期徒刑參年拾月。"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))