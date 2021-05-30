import json
from criminal_identifier import runLoki
"""**Notes & Problems**
1. 心理諮商：不一定是告訴人接受心理諮商，也有可能是證人接受心理諮商。
2. 鑑定書專指DNA鑑定處理
3. 告訴人與被告人皆會接受測謊鑑定
4. 驗傷診斷書：純粹判斷證據有無，無疑慮
5. 坦承：被告認罪。指述：告訴人指認描述（需要算詞頻嗎？）
6. 繪圖：純粹判斷證據有無，無疑慮
7. 輔導紀錄：是否有可能被告也有輔導紀錄？Ａ：排除論罪科刑後（不是影響有沒有罪，只會影響刑期）
8. 仍須判斷同事關係、同居關係、按摩，與男女朋友是否為被告與告訴人之間

"""

def arrange_data(judgement):
  plaintiffLIST = ['甲女', 'A女', 'Ａ女', '甲○']
  with open (judgement, "r") as f:
    data = json.load(f)
  
  dataLen = len(data)
  originalName = []
  for i in data:
    for j in range(1, 3):
      if i['judgement_{}'.format(j)] != "":
        originalSentence = i['sentence_{}'.format(j)]
        originalJudgement = i['judgement_{}'.format(j)]
        sentence, status, *original = change_name(i['sentence_{}'.format(j)]) # original = pronoun (list), alias (string), gender (string)
        # print(status, original, original[0])
        if status == 1:
          if original[1] != None:
            firstName = original[1]
          if original[2] != None:
            firstName = original[2]
          for k in range(len(original[0])):
            originalName.append(original[0][k] + firstName)
          print("RunLoki(sentence_{})".format(data.index(i)+1))
          resultDICT_1 = runLoki([sentence], ['isCriminal'])
        else:
          print("RunLoki(originalSentence_{})".format(data.index(i)+1))
          resultDICT_2 = runLoki([originalSentence], ['isCriminal'])
        try:
          i['plaintiff_{}'.format(j)] =[plaintiff for plaintiff in plaintiffLIST if plaintiff in originalJudgement][0]
        except:
          i['plaintiff_{}'.format(j)] = ""
        try:
          # 被告
          print("status:", status)
          if status == 1:
            if '0' in originalSentence: # 被告欄位為000000A類型
              if originalJudgement.partition("下稱")[2][0:2] != i['plaintiff_{}'.format(j)]: # 內文第一個下稱不是原告時
                i['defendent_{}'.format(j)] = originalJudgement.partition("下稱")[2][0:2]
              elif originalJudgement.partition("下稱")[2][0:2] == i['plaintiff_{}'.format(j)]: # 內文第一個下稱是被告時，找下一個下稱
                i['defendent_{}'.format(j)] = originalJudgement.partition("下稱")[2].partition("下稱")[2][0:2]
              elif originalJudgement.partition("呼為")[2][0:2] != i['plaintiff_{}'.format(j)]: # 內文第一個呼為是被告時，找下一個呼為
                i['plaintiff_{}'.format(j)] = '乙女'
                i['defendent_{}'.format(j)] = originalJudgement.partition("呼為")[2][0:2]
          #   elif originalJudgement.partition("呼為")[2][0:2] == i['plaintiff_{}'.format(j)]: # 內文第一個呼為是被告時，找下一個呼為
          #     i['defendent_{}'.format(j)] = originalJudgement.partition("呼為")[2].partition("呼為")[2].partition("呼為")[2][0:2]
            elif '現役軍人' in originalSentence: # 被告為現役軍人
              i['defendent_{}'.format(j)] = originalSentence.partition("現役軍人")[0]
            elif status == 1: # 已改名為王小明，須將被告改回原名
              i['defendent_{}'.format(j)] = originalName[-1]
            elif "○○飯店" in originalSentence:
              i['defendent_{}'.format(j)] = []
              i['defendent_{}'.format(j)].append(i['sentence_{}'.format(j)][11:14])
              i['defendent_{}'.format(j)].append(i['sentence_{}'.format(j)][15:18])
          elif status == 0:
            print(resultDICT_2)
            i['defendent_{}'.format(j)] = resultDICT_2['defendent']
            i['plaintiff_feature'] = resultDICT_2['plaintiff_feature']
            i['defendent_feature'] = resultDICT_2['defendent_feature']
            i['under_18'] = resultDICT_2['under_18']
            i['attempt'] = resultDICT_2['attempt']
            i['isWoman'] = resultDICT_2['isWoman']
            if '撤銷' in originalSentence:
              i['annulment'] = 1
            else:
              i['annulment'] = 0
            print("原告:{}".format(i['plaintiff_{}'.format(j)]), "被告:{}".format(i['defendent_{}'.format(j)]), "是否曾被撤銷:{}".format(i['annulment']), "被害人特點:{}".format(i['plaintiff_feature']), "加害人特點:{}".format(i['defendent_feature']), "未成年:{}".format(i['under_18']), "未遂:{}".format(i['attempt']), "是否為女性:{}".format(i['isWoman']), "\n連結:{}".format(i['url']))
            break
        except:
          pass
        if '撤銷' in originalSentence:
          i['annulment'] = 1
        else:
          i['annulment'] = 0
        # 被害人特點：精神障礙/心智缺陷/身體障礙/未滿十四歲/少年
        i['plaintiff_feature'] = resultDICT_1['plaintiff_feature']
        # 加害人特點：攜帶兇器/侵入住宅/對被害人施以凌虐
        i['defendent_feature'] = resultDICT_1['defendent_feature']
        # 未成年
        i['under_18'] = resultDICT_1['under_18']
        # 是否未遂
        i['attempt'] = resultDICT_1['attempt']
        # 受害者是否為女性
        i['isWoman'] = resultDICT_1['isWoman']
        print("原告:{}".format(i['plaintiff_{}'.format(j)]), "被告:{}".format(i['defendent_{}'.format(j)]), "是否曾被撤銷:{}".format(i['annulment']), "被害人特點:{}".format(i['plaintiff_feature']), "加害人特點:{}".format(i['defendent_feature']), "未成年:{}".format(i['under_18']), "未遂:{}".format(i['attempt']), "是否為女性:{}".format(i['isWoman']), "\n連結:{}".format(i['url']))
      else:
        pass
  return data

def change_name(inputSTR):
  pronounLIST = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "丑", "寅", "卯", "辰", "巳", "午", "申", "酉", "戌", "亥"]
  genderLIST = ["男", "女"]
  aliasLIST = ["○○", "◯◯", "○○○", "◯◯◯"]
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
    inputSTR = inputSTR.replace(alias, "小明", 1)
  return inputSTR, status, pronoun, alias, gender


def data_collector(inputDICT):
  lawsuitDICT = {'ID': "",'Date': '','Guilty': 0, '心理諮商': 0, '鑑定書': 0, '測謊鑑定': 0, '驗傷診斷書': 0, '通話紀錄': 0, '對話紀錄': 0, '坦承': 0, '指述': 0, '繪圖': 0, '輔導紀錄': 0, '同事關係': 0, '同居關係': 0, '按摩': 0, '男女朋友': 0}
  lawsuitDICT['ID'] = inputDICT['ID']
  lawsuitDICT['Guilty'] = inputDICT['guilty']
  lawsuitDICT['Date'] = inputDICT['Date']
  for i in range(1, 3):
    if '心理諮商' in inputDICT['judgement_{}'.format(i)]:
      lawsuitDICT['心理諮商'] = 1
    if '鑑定書' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['鑑定書'] = 1
    if '測謊鑑定' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['測謊鑑定'] = 1
    if '驗傷診斷書' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['驗傷診斷書'] = 1
    if '通話紀錄' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['通話紀錄'] = 1
    if '對話紀錄' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['對話紀錄'] = 1
    if '坦承' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['坦承'] = 1
    if '自承' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['自承'] = 1
    if '指述' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['指述'] = 1
    if '繪圖' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['繪圖'] = 1
    if '輔導紀錄' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['輔導紀錄'] = 1
    if '無其他積極' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['無其他積極'] = 1
    if '所述反覆不一' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['所述反覆不一'] = 1
    if '男女朋友' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['男女朋友'] = 1
    if '按摩' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['按摩'] = 1
    if '同事關係' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['同事關係'] = 1
    if '同居' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['同居'] = 1
    if '同學' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['同學'] = 1
    if '室友' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['室友'] = 1
    return lawsuitDICT

if __name__ == '__main__':
  judgement = arrange_data("judgement.json")
  # with open("judgement_arrange.json", "w", encoding = "utf-8") as f:
  #   json.dump(judgement, f, ensure_ascii = False, indent = 4)
  # print(runLoki(["邱清鑫、陳佳新二人以上共同攜帶兇器犯強制性交而凌虐罪"]))
  # with open ('judgement.json') as jsonfile:
  #   judgementLIST = json.load(jsonfile)
  # lawsuitLIST = []
  # for lawsuit in judgementLIST:
  #     lawsuitLIST.append(data_collector(lawsuit))
  # df = pd.DataFrame(lawsuitLIST)
  # df.to_csv("result.csv")