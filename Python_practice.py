print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
    print(counties[2])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print ("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#get the keys/values of a dictionary
print("get the keys of a dictionary")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

print("Voters")
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#get the key-value pairs of a dictionary: for each key and value in the dictionary, print both
print("get key-value pairs of a dictionary")
for county, voters in counties_dict.items():
    print(county,voters)

print("start here")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

print("print whole dictionary")
for county_dict in voting_data:
    print(county_dict)

print("print dictionary with range")
for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("quiz")
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#for each dictionary in the bigger dictionary, print each dictionary's [value for this key]

#skill drill 'county has _ registered voters
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters:,} registered voters.")

print("last skill drill 3.2.11")
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

