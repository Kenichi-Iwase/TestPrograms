% 箱ひげ図を描くスクリプト

rng('default')

% 体重リストを読み込む
T2101 = readtable('WeightListJan2021.csv');
T2107 = readtable('WeightListJul2021.csv');
T2108 = readtable('WeightListAug2021.csv');
x = [T2101.Weight; T2107.Weight; T2108.Weight];

% グループの作成
g0 = repmat({'Jan2021'},39,1);
g1 = repmat({'Jul2021'},31,1);
g2 = repmat({'Aug2021'},29,1);
g = [g0; g1; g2];

% 箱ひげ図の表示
boxplot(x,g)

% PNGに保存
saveas(gcf, 'MonthlyWeightBoxplot.png')
