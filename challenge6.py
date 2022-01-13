#Grade Sorter App
import time
print ("Welcome for your trusted grade sorting")

grade = [] # creates empty list called grade
while True:
    user_input= float (input("Enter Grade: \n"))
    if len(grade) == 4: #program accepts 4 user inputs
        break
    else :
        grade.append(user_input)   #adds user input to empty list called grades
time.sleep (2)                      #Execution stops for two seconds(for the fun of it)

sorted_grade = sorted(grade, reverse = True)  #sorting the grades from highest to lowest

print ("Your grades in descending order are: \n", sorted_grade)
print ("The lowest two grades are: \n", sorted_grade[2:])#slicing
print ("Your remaining grades are : \n", sorted_grade[:2])
print ("The highest grade is: \n", sorted_grade[0])




