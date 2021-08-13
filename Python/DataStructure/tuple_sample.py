# タプルのサンプルスクリプト
my_tuple = tuple()
print(my_tuple)

my_tuple = ()
print(my_tuple)

# ひとつの要素のタプルを作成
rndm = ('M. Jackson', 1958, True)
print(rndm)

# タプルの例
x = ('self taught', )
print(x)

# タプルではなく数値演算に使うカッコ
y = (9) + 1
print(y)

dys = ('1984', 'Brave New World', 'Fahrenheit 451')
# 表示は[]を使用
print(dys[0])
print(dys[1])
print(dys[2])
# 代入することはできない
# dys[1] = "1Q84"

# タプル要素に含まれているかをテスト
judge1 = '1984' in dys
print(judge1)
judge2 = '1Q84' in dys
print(judge2)
judge3 = "Handmaid's Tale" not in dys
print(judge3)
judge4 = 'Brave New World' not in dys
print(judge4)
