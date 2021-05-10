# @TODO: Your code here
pet = {"name":"Mr. Kitty",
        "age":11,
        "hobbies":["sleeping","eating","watching cat tv","hiding","party all the time"],
        "wake":{"Sunday":9,"Monday":8,"Tuesday":9,"Wednesday":7}}

#Print out the following:
#Your pet's name and age.
print(f'My name is {pet["name"]} and I am {pet["age"]}.')

#How many hobbies your pet has.
len(pet["hobbies"])
hobbiesNumber = len(pet["hobbies"])
print(hobbiesNumber)
print(pet["name"] +" has " + str(hobbiesNumber) + " hobbies.")

#What your pet's favorite hobby is.
print(f'{pet["name"]} loves to {pet.get("hobbies")[4:]}.' )

#What time your pet wakes on one of the days of the week.
for hobbies_dict in pet_dict:
        for i in hobbies_dict:
                print(i)

print(pet.get("wake").get("Sunday"))
print(pet.get("wake"))

print (f'{pet["name"]} woke up at {pet.get("wake").get("Sunday")} ready to {pet["hobbies"][4:]}.')