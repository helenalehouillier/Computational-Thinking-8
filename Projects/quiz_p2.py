#Begining
Christmas_points = 0
Halloween_points = 0

#Middle
answer = input("Would you trick or treat in the rain? A) No B) Yes")
if answer == "A":
    Christmas_points += 1
elif answer == "B":
    Halloween_points += 1

answer = input("Which would you rather have A) Peppermints B) Candy corn")
if answer == "A":
    Christmas_points += 1
elif answer == "B":
    Halloween_points += 1

answer = input("Do you like snow? A) Yes B) No")
if answer == "A":
    Christmas_points += 1
elif answer == "B":
    Halloween_points += 1

answer = input("Which flavor is better A) Peppermint B) Pumpkin spice")
if answer == "A":
    Christmas_points += 1
elif answer == "B":
    Halloween_points += 1

answer = input("Sweet or savory? A) Savory B) Sweet")
if answer == "A":
    Christmas_points += 1
elif answer == "B":
    Halloween_points += 1

#End
if Christmas_points > Halloween_points:
    print("You are a Christmas person")
elif Halloween_points > Christmas_points:
    print("You are a Halloween person")
elif Halloween_points == Christmas_points:
    print("You are a Christmas and Halloween person!")
