% CSVファイル読み込み
T = readtable('WeightListAug2021.csv');

% 体重変化グラフを表示
plot(T.Date, T.Weight)
title('体重変化グラフ　8月')
xlabel('日付')
ylabel('体重[kg]')
saveas(gcf, 'WeightGraph.png')

% 体重と体脂肪率を散布図で表示
scatter(T.Weight, T.WeightRatio)
title('体重と体脂肪率の関係')
xlabel('体重[kg]')
ylabel('体脂肪率[%]')
saveas(gcf, 'WeightRatio.png')
