destinations = ["USA", "India", "Spain", "Germany", "Italy", "Estonia", "Cuba"]
print("These are our current holiday destinations on offer")
travel_plan = input("Where would you like to visit?: ")

if travel_plan in destinations:
    print("Yes! We have decent deals on travels for: ", travel_plan)
else:
    print("We are yet to add: ", travel_plan)

