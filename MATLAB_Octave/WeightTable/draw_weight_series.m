% CSVファイル読み込み
T = readtable('WeightList.csv');

% 体重変化グラフを表示
plot(T.Date, T.Weight)
title('体重変化グラフ　2021年')
xlabel('日付')
ylabel('体重[kg]')
saveas(gcf, 'WeightGraphSeries.png')

% 体重と体脂肪率を散布図で表示
scatter(T.Weight, T.WeightRatio)
title('体重と体脂肪率の関係')
xlabel('体重[kg]')
ylabel('体脂肪率[%]')
saveas(gcf, 'WeightRatioScatter.png')

% 体重と体脂肪率の相関係数を求める
corrcoef(T.Weight, T.WeightRatio)

% 体重のヒストグラムを表示
histogram(T.Weight)
title('体重のヒストグラム')
xlabel('体重[kg]')
ylabel('頻度')
saveas(gcf, 'WeightHistogram.png')
