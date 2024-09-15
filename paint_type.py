"""
A simple Python program that displays a list of paint types.
Followed by paint resellers.
The program allows a user to enter a paint of choice.
The application confirms if the paint is available or not.
If not, it tells a user the paint is out of stock.
Interesting part: The user gets to select 1 to see a list of resellers.

"""
paint_types = ["Impressionism", "Watercolor", "Oil Painting", "Gouache", "Art Noveau", "Fresco", "Landscape Painting", "Expressionism", "Abstract", "Surrealism", "Realism", "Encaustic", "Digital Art"]
resellers = ["Golden Egg", "White Dove", "Pure Smile"]
print("These are the list of paints", "\n", paint_types)
customer = input("What would you like to buy?: ")
print("This is your item of interest: ","\n", customer)
if customer in paint_types:
    print("The item: ", customer, "is available")
else:
    print("Sorry, we do not currently stock: ", customer)
print("Would you like to view where to find your request?")
item_search = input("Press 1 to view list of resellers: ")
if item_search == "1":
    print("These are the list of resellers ", resellers)
else:
    print("That is an invalid input")

