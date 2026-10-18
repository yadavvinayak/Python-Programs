#unordered (indexing not works), unique iteams, mutable (element can be added or removed)
#sets automatically remove duplicate values and use {}
food= {"Pizza", "Burger", "Pasta", "Pizza", "Burger"}
drink= {"Coke", "Pepsi", "Sprite", "Coke"}
print(food)
print(drink)
print(type(food))
food.add("Kunafa")
print(food)
food.remove("Pasta")
print(food)
food.pop()
print(food)
combined= food.union(drink)
print (combined)
empty=set()
print(type(empty))

