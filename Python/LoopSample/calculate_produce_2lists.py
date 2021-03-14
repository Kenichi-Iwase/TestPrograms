# 2つのリストの積を出力するスクリプト
data1 = [8, 19, 148, 4]
data2 = [9, 1, 33, 83]
products = []
for i in range(0, 4):
  products.append(data1[i] * data2[i])
result = "data1とdata2の積： {}".format(products)
print(result)
