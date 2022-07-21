x = {
"chair":500,  "table":300, 34:"python"
}
print(x)

# Value of chair
print(x["chair"])

#length of dictionary x
print(len(x))

# Add one more item into dictionay
x["veg"]=120
print(x)

# Add one more item into dictionay using update key
x.update({12:"django"})
print(x)

# Pop one item into dictionay using update key
x.pop("table")
print(x)

# LIST THE KEY OF DICTIONARY OF X
for i in x:
    print(i)

# LIST THE VLAUE OF DICTIONARY OF X
for i in x.values():
    print(i)

# LIST THE VLAUE&KEY OF DICTIONARY OF X
for i in x.items():
    print(i)

# PRINT THE VLAUE  USING GET[KEY] FUNCTION
numbers={
    1: "one",
    2: "two",
    3: "three"
}
print (numbers.get(1,"key not found"))


# PRINT THE PREDEFINED OUTPUT  USING GET[KEY] FUNCTION
numbers={
    1: "one",
    2: "two",
    3: "three"
}
print (numbers.get(5,"key not found"))
