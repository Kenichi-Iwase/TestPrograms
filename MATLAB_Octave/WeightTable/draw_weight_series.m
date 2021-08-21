T = readtable('WeightListAug.csv');
plot(T.Date, T.Weight)
title('体重変化グラフ　8月')
xlabel('日付')
ylabel('体重[kg]')
