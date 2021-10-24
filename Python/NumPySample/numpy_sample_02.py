import numpy as np

print('要素へのアクセス')
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print('0行目を表示')
print(X[0])
print('(0,1)の要素')
print(X[0][1])

print('for文で要素ごとにアクセス')
for row in X:
    print(row)

print('Xを1次元の配列へ変換')
X = X.flatten()
print(X)

print('インデックスが0,2,4番目の要素を取得')
print(X[np.array([0, 2, 4])])

print('条件を満たしているかを判定する')
print(X>15)

print('ある条件を満たす要素のみを取り出す')
print(X[X>=15])
