print("Welcome to the cyclone")

height = int(input("What is your height in cm? "))

credits = int(input("Now, how many credits do you have? "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You aren't tall enough!")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else: 
  print("You haven't met either requirement :/ ")