#Thesaurus app
import random
import time
Thesaurus = {"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
              "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
              "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
              "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],}

print("Welcome to your thesaurus app. \nHere are the available words:")
words = Thesaurus.keys()

for words in Thesaurus.keys():
    print("\t-",words)

search = input("Enter word you'd like to get the synonym for:\n").lower().strip()
if search in Thesaurus:
    out = random.choice(Thesaurus[search])
    print("\nThe synonym is :",out.title())
else:
    print("Not found!!")    

full = input("\nwould you like to see the whole thesaurus? (y/n):\n").title()
if (full == "Y"):
    for key, values in Thesaurus.items():
        print("\n",key, ":")
        for value in values:
            print("\t-", value)
      
else:
    time.sleep(2)
    print("\n\nOkay bye")





















