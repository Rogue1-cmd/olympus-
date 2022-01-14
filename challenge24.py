#Letter frequency analysis app
from collections import Counter

print("welcome to the letter frequency analysis app")
non_letters = ['1','2','3','4','5','6','7','8','9','0',' ','.','?',
'!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t']

key_phrase_1 = input("Enter phrase to be analysed: \n").lower()

for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)    
letter_count = Counter(key_phrase_1)

print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t", key, "\t\t", (value), "\t\t", (percentage), "%")

ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')

#Information for the second key key_phrase_2
key_phrase_2 = input("\n\nEnter phrase to be analysed : ").lower().strip()

#Removing all non letters from key_phrase_2
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')
    total_occurrences = len(key_phrase_2)

#Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)

#Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t", key, "\t\t",(value), "\t\t", (percentage), "%")

#Make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

#Print the list
print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')
    
#WAS BORED!!! COPY PASTED :(    