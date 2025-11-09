names = ["Abdullahi", "AtaurRahman", "Ahmad","Abdullahi", "Mustapha", "Dankanjiba"]
Languages = ["Python", "Javascript", "Hausa", "Turkish"]
conbination = [["Justice", "Truth"], "leadership", "loneliness", 234, 42]

len(names) #this to know the length of a list

names.pop() #this removes last element and returns removes element
names.pop(0) #this removes last element at given index
names.remove("Abdullahi") #removes first instance of given element i.e. Abbdullahi in this case
names.append("Aisha") #adds Aisha to the list, makes it last element
names.insert(5, "Aisha") #adds Vedia to the list at index 4

for name in names:
    print(name) #this works