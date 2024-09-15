shopping_list = ["Carrots", "Chocolate", "Mango", "Orange", "Custard", "Plantain"]
print(shopping_list)
new_item = input("Enter a new item: ")
if new_item in shopping_list:
    print("That item is already available")
    print(shopping_list)
    
else:
    shopping_list.append(new_item)
    print("A new entry has been made", shopping_list)
