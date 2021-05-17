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
    if '指述' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['指述'] = 1
    if '繪圖' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['繪圖'] = 1
    if '輔導紀錄' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['輔導紀錄'] = 1
    if '同事關係' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['同事關係'] = 1
    if '按摩' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['按摩'] = 1
    if '男女朋友' in lawsuit['judgement_{}'.format(i)]:
      lawsuitDICT['男女朋友'] = 1
    return lawsuitDICT

if __name__ == '__main__':
    lawsuitLIST = []
    for lawsuit in judgementLIST:
        lawsuitLIST.append(data_collector(lawsuit))
    df = pd.DataFrame(lawsuitLIST)
    df.to_csv("result.csv")