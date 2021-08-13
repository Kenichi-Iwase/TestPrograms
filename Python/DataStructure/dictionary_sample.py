# Dictionary Sample Script

# dict()関数で初期化
my_dict = dict()
print(my_dict)

# {}で初期化
my_dict = {}
print(my_dict)

# ハッシュ定義
fruits = {
    "Apple": "Red",
    "Banana": "Yellow"
}
print(fruits)

facts = dict()

# バリューを追加
facts["code"] = "fun"
# キーで参照
print(facts["code"])

# バリューを追加
facts["Bill"] = "Gates"
# キーで参照
print(facts["Bill"])

# バリューを追加
facts["founded"] = 1776
# キーで参照
print(facts["founded"])

# キーから値を検索
if "Bill" in facts:
    print("exists")
else:
    print("not exist")

# 最後にハッシュ全体を表示
print(facts)

# キーから値を検索する機能のテスト
bill = {'Bill Gates': 'charitable'}
judge = 'Bill Gates' in bill
print(judge)
