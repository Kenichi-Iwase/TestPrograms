# ファイルの書出しと読み込みを行うサンプルスクリプト

# write file in English
st = open("st.txt", "w")
st.write("Hi from Python!")
st.write("\n")
st.write("I have a dream.")
st.close()

# write file in English by using with statement
with open("st2.txt", "w") as f:
    f.write("Hi from Python!")
    f.write("\n")
    f.write("I have a dream.")

# withを使わないパターン
st = open("st_jp.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは！")
st.write("\n")
st.write("今日はいい天気ですね！")
st.close()  # この文が必要になる

# withを使ったパターン
with open("st_jp_2.txt", "w", encoding="utf-8") as f:
    f.write("Pythonからこんにちは！")
    f.write("\n")
    f.write("今日はいい天気ですね！")

# ここからファイルの読み込み
print("Reading text in English")
with open("st.txt", "r") as f:
    print(f.read())

print("日本語で書かれたファイルを読み込む")
with open("st_jp.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ファイルを読み込み、ひとつの要素に追加
# 改行は考慮されない
my_list = []
with open("st.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

# 1行ごとに割り当て、リストの第1要素に格納
my_list1 = []
with open("st.txt", "r") as f:
    my_list1.append(f.read().split("\n"))
print(my_list1)

# 1行ごとにリストの要素に割り当て
my_list2 = []
with open("st.txt", "r") as f:
    my_list2 = f.read().split("\n")
print(my_list2)
