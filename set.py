names = {"Abdullahi", "AtaurRahman", "Ahmad","Abdullahi", "Mustapha", "Dankanjiba"}
Languages = {"Python", "Javascript", "Hausa", "Turkish"}
conbination = {["Justice", "Truth"], "leadership", "loneliness", 234, 42}

len(names) #this to know the length of a list

# names.pop() won't work since this isn't an iterable
# names.remove("Abdullahi") this is used instead
names.add("Aisha") #adds Aisha to the list, adds it anywhere since sets aren't iterable

for name in names:
    print(name) #this works sha