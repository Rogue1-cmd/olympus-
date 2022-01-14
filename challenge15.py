#Grade point average calculator
print("Welcome to the grade point average calculator")
name = input("Enter name: \n")
n = int(input("How many grades would you like to enter?:\n"))

grades = []

#Using for loop to get any number of grades input
for i in range(n):
    points = int(input("Enter grade; \n"))
    grades.append(points)
grades.sort(reverse = True)
print(grades)   

#Finding grade point average
x = sum(grades)
y = len(grades)
gpa = float(x/y)
gpa = round(gpa, 2)

print(name,"'s Grade summary:\n")
print("Number of grades:",n, "\n" )
print("Highest grade :", grades[0],"\n")
print("Lowest grade: ", grades[n-1],"\n")
print("Average grade:", gpa, "\n")

#Desired perfomance
desired_avg = int(input("What is your desired average? \n"))
k = ((desired_avg*(y+1))- x)
print("You require ",k, "more marks in your next assignment to achieve this")

print("Lets see what your grade could've been if you did better or worse in an assignment.")
nw_grds = grades[:]
ngrd = int(input("what grade would you like to change:\n"))
nw_grds.remove(ngrd)
ngrd2 = int(input("what grade would you like to change it to:\n"))
nw_grds.append(ngrd2)

print("new grades\n",nw_grds)
new_gpa = float(sum(nw_grds)/len(nw_grds))
new_gpa = round(new_gpa, 2)
print("New average = \t")

print(name,"'s desired Grade summary:\n")
print("Number of grades:",n, "\n" )
print("Highest grade :", nw_grds[0],"\n")
print("Lowest grade: ", nw_grds[n-1],"\n")
print("Average grade:", new_gpa, "\n")

diff = (new_gpa - gpa)
diff = round(diff, 2)
print("Your new desired gpa",new_gpa, "is ",diff,"points more than your current", gpa)
print("Your grades are still the same though.\n",grades,"\nTough luck!!!")










