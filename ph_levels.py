ph = int(input("Between 0-14, what is the pH level? "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
   print("Neutral")