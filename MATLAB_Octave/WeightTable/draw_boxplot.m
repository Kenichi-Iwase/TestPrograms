% 箱ひげ図を描くスクリプト

rng('default')

% 体重リストを読み込む
T2101 = readtable('WeightListJan2021.csv');
T2106 = readtable('WeightListJun2021.csv');
T2107 = readtable('WeightListJul2021.csv');
T2108 = readtable('WeightListAug2021.csv');
T2109 = readtable('WeightListSep2021.csv');
x = [T2101.Weight; T2106.Weight; T2107.Weight; T2108.Weight; T2109.Weight];

% グループの作成
% 2番目の引数には対象データの行数を記入（都度更新必要）
g2101 = repmat({'Jan2021'},39,1);
g2106 = repmat({'Jun2021'},30,1);
g2107 = repmat({'Jul2021'},31,1);
g2108 = repmat({'Aug2021'},31,1);
g2109 = repmat({'Sep2021'},12,1);
g = [g2101; g2106; g2107; g2108; g2109];

% 箱ひげ図の表示
boxplot(x,g)
title('月ごとの体重')
xlabel('年月')
ylabel('体重[kg]')

% PNGに保存
saveas(gcf, 'MonthlyWeightBoxplot.png')
