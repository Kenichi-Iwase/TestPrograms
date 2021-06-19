import pandas as pd

# DataFrameオブジェクトを使用してCSVデータを出力する方法

data_frame = pd.read_csv('uriage.csv', encoding='utf-8')

for index, row in data_frame.iterrows():
    # 売上差分を計算
    difference = int(row['当期売上']) - int(row['前期売上'])

    # 小分類と売上差分を出力
    print(f'{index+1}行目：{row["小分類"]} 売上差分：{difference}')
