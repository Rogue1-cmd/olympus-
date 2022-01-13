#Basketball roster program
import time
print("Welcome to the basketball roster")
roster = []
point_guard = input("Enter point guard's name: ").title()
shooting_guard = input("Enter shooing guard's name: ").title()
small_foward = input("Enter small foward's name: ").title()
power_foward = input("Enter power foward's name: ").title()
center = input ("Enter center's name: ").title()

roster.append(str(point_guard))
roster.append(str(shooting_guard))
roster.append(str(small_foward))
roster.append(str(power_foward))
roster.append(str(center))
time.sleep(2)

print("Your starting 5 this season are: \n", ",".join(roster))

injured_player = []
injured_player.append(str(small_foward))
time.sleep(2)
print("\n")
print ("sorry coach", "".join(injured_player), ", is injured")

roster.remove(small_foward)

print("\n ")

print("Your roster currently has", len(roster), "players.")

time.sleep(1)
added_player = input("who will replace injured_player; ").title()
roster.insert(2, added_player)
print("\n")
time.sleep(1)
print("\n Your starting 5 in the upcoming season are")
time.sleep(1)
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t" + roster[0])
print("\t\tShooting Guard:\t\t" + roster[1])
print("\t\tSmall Forward:\t\t" + roster[2])
print("\t\tPower Forward:\t\t" + roster[3])
print("\t\tCenter:\t\t\t" + roster[4])

print("\n Good luck", str(added_player), "you will do great.")

