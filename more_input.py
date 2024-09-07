"""
counter = 100
miles = 1000.0
name = "Chloe Adams"

print("The counter is:", counter)
print("The miles range is:", miles)
print("Hello", name)

print(type(counter))
print(type(miles))
print(type(name))


"""
studentName = str(input("Please enter your name: "))
if studentName == "Chloe Adams":
    print("Please kindly go ahead and enter some important details")
    input1 = str(input("Choose a subject: "))
    input2 = str(input("Choose a 2nd subject: "))
    input3 = str(input("Choose a 3rd subject: "))
    print("Hi", studentName)
    print("Your subjects are:")
    print(input1)
    print(input2)
    print(input3)
    

else:
    if studentName != "Chloe Adams":
        print("Please complete a registration form")
