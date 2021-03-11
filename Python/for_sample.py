# for loop test
for i in range(10):
  print('Hello, world!')

# 文字単位で表示するスクリプト
name = "Ted"
for character in name:
  print(character)

# リストのテスト
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
  print(show)

# forループとリストのテスト
movies = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for movie in movies:
  print(movie)

# range関数で範囲指定
for i in range(25,51):
  print(i)

# 映画一覧を表示
for i, movie in enumerate(movies):
  result = "No.{} Title:{}".format(i, movie)
  print(result)

# 2つのリストの積を出力するスクリプト
data1 = [8, 19, 148, 4]
data2 = [9, 1, 33, 83]
products = []
for i in range(0, 4):
  products.append(data1[i] * data2[i])
result = "data1とdata2の積： {}".format(products)
print(result)
