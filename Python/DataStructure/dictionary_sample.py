# Dictionary Sample Script

fruits = {
    "Apple": "Red",
    "Banana": "Yellow"
}
print(fruits)

facts = dict()
facts["code"] = "fun"
print(facts["code"])
facts["Bill"] = "Gates"
print(facts["Bill"])
facts["founded"] = 1776
print(facts["founded"])
if "Bill" in facts:
    print("exists")
else:
    print("not exist")
