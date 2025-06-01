Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0

print("Welcome to Hogwarts, the school of wizardry, I'm the sorting hat!")

print("Now, sit down while I'll be asking you some questions... Answer me with numbers, only!")

q1 = int(input("Do you like Dawn or Dusk? 1) Dawn 2) Dusk? "))

if q1 == 1:
  Gryffindor += 1 
  Ravenclaw += 1
elif q1 == 2:
  Hufflepuff += 1 
  Slytherin += 1
else:
  print("Wrong input!")

print("I can imagine...")

q2 = int(input("Q2) When I’m dead, I want people to remember me as: 1) The Good, 2) The Great, 3) The Wise, 4) The Bold "))

if q2 == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin += 2
elif q2 == 3:
  Ravenclaw += 2
elif q2 == 4:
  Gryffindor += 2
else:
  print("Wrong input!")

print("I see...I see...Now, onto the last one please!")

q3 = int(input("Q3) Which kind of instrument most pleases your ear? 1) The violin, 2) The trumpet, 3) The piano, 4) The drum "))

if q3 == 1:
  Slytherin += 4
elif q3 == 2:
  Hufflepuff += 4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input!")

print("Your score is =", "for Gryffindor: ", Gryffindor, "for Ravenclaw: ", Ravenclaw, "for Hufflepuff: ", Hufflepuff, "and for Slytherin: ", Slytherin)

# Find the house with the highest score
houses = {
    "Gryffindor": Gryffindor,
    "Ravenclaw": Ravenclaw,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin
}

# Get the house name with the maximum score
sorted_house = max(houses, key=houses.get)

print(f"\n🎩 The Sorting Hat has decided... This makes you a {sorted_house}! 🎩")