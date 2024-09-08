userSelect = input("> Please select an iPhone model: ")
iphone = {
        "model" : "iPhone",
        "announced" : "Jan 9 2007",
        "released" : "June 29 2007"
        }
iphone3G = {
        "model" : "iPhone 3G",
        "announced" : "June 9 2008",
        "released" : "June 11 2008"
        }
iphone4 = {
        "model" : "iPhone 3GS",
        "announced" : "June 8 2009",
        "released" : "June 19 2009"
    }
iphone4s = {
        "model" : "iPhone4s",
        "announced" : "June 7 2010",
        "released" : "June 24 2010"
    }
iphone5 = {
        "model" : "iPhone 5",
        "announced" : "September 10 2013",
        "released" : "September 12 2012"

    }

if userSelect == "iphone3G":
    print(iphone3G)
else:
    print("Try again")
