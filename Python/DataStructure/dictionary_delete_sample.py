# 辞書からキーとバリューのペアを削除するスクリプト

# 辞書定義
books = {
    'Dracula': 'Stoker',
    '1984': 'Orwell',
    'The Trial': 'Kafka'
}

# 削除前の辞書の状態を表示
print(books)

# キーとバリューを削除
del books['The Trial']

# 削除後の辞書の状態を表示
print(books)
