import json

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
  with open ('judgement.json') as jsonfile:
    judgementLIST = json.load(jsonfile)
  lawsuitLIST = []
  for lawsuit in judgementLIST:
      lawsuitLIST.append(data_collector(lawsuit))
  df = pd.DataFrame(lawsuitLIST)
  df.to_csv("result.csv")