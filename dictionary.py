myDetails = {
    "name": "AtaurRahman",
    "surname": "Abdullahi", 
    "age": 45,
    1:"lack of direction",
    2:"seeking his passion",
    "settings": {
        "bg-color": "navy blue",
        "showAds": False,
        "paid_subscription": False
    }
}

print(myDetails["name"])
print(myDetails.get("name", "This is to catch errors")) #this prevents crashin the code should the first argument not be available
myDetails["name"] = "Aisha" #This modifies the specified property
myDetails["other_names"] = "Mustapha" #this is added to the dictionary