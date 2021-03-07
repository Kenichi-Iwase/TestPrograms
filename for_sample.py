for i in range(10):
  print('Hello, world!')

name = "Ted"
for character in name:
  print(character)

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
  print(show)

movies = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for movie in movies:
  print(movie)

for i in range(25,51):
  print(i)

for i, movie in enumerate(movies):
  result = "No.{} Title:{}".format(i, movie)
  print(result)
