books = ["Learn Python Programming", "MySQL Databases", "HTML & CSS"]
print("These are the list of stored books","\n", books)

book_to_read = input("Hi! What book are you interested to read?: ")
print("Your request says you want to read: ", book_to_read)
if book_to_read in books:
    print("Yes! The book is available")
else:
    print("Sorry, we do not sell that book")
    

