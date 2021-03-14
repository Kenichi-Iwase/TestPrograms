# forループとリストのテスト
movies = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for movie in movies:
  print(movie)

# 映画一覧を表示
for i, movie in enumerate(movies):
  result = "No.{} Title:{}".format(i, movie)
  print(result)
