#Fisher-Yates Shuffle Algorithm
import random

num = list(map(int, input("Enter Multiple integer values to shuffle :\n\t").split())) # help out with this!!!!

#num = [34, 45, 78, 90, 12, 3, 5]

print("\n\tOriginal List: ", str(num))

for i in range(len(num)-1, 0, -1):

    j = random.randint(0, i+1) #pick random between 0, i

    num[i], num[j] = num[j], num[i] #swap arr[i] with element at random index

print("\n\tShuffled list:", str(num), "\n")
