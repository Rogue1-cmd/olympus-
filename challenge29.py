#Guess my word app
import random
print("Erm.... Welcome...?")
game_dict = {
     "Movies":["fast and furious","django unchained","harry potter", "alice in wonderland", "clash of the titans", "jackass", "love and other drugs","eternal sunshine of a spotless mind","memento","rampage","sherlock holmes","pulpfiction","life of pi","love",],
     "Sports":["football","bowling","ice hockey","surfing","karate","horse racing","snowboarding","skateboarding","cycling","archerysoccer","basketball","tennis","baseball","golf","running","volleyball","badminton","swimming","boxing","table tennis"],
     "Footballers":["saka","martinelli","ramsdale", "aubameyang", "lacazette", "sanchez", "ozil", "partey","white", "henry","gnabry","weah", "smithrowe", "tierney", "xhaka", "bellerin", "gabriel", "tavares", "lokonga", "patino", " fabregas", "podolski", "wright","iwobi"],
     "Countries":["kenya", "uganda", "tanzania", "rwanda", "somalia", "ethiopia", "burundi", "south africa", "mali", "algeria", "nigeria", "gambia", "senegal", "congo", "zimbabwe", "zanzibar", "mozambique", "morocco", "sweden", "france", "england", "ireland", "finland", "russia"], 
     "African_Leaders":["jaramogi", "nkuruma", "mboya", "mandela", "moi", "kenyatta", "nyerere", "lumumba", "ouko", "murumbi", "raila", "taylor", "rawlings", "tewodoros", "mugabe"]}

game_keys = []     

for item in game_dict.keys():
    game_keys.append(item)

for i in game_keys:
    print("\t - ", i)

active = True
while active:
    ran_int = random.randint(0, len(game_keys)-1) #generating a random index for game_category
    game_category = game_keys[ran_int]
    ran_int2 = random.randint(0, len(game_dict[game_category])-1) #generating a random index for game_word
    game_word = game_dict[game_category][ran_int2]

    blank_word = []
    for letter in game_category:
        blank_word.append("-")
  

    print("Guess a ", len(game_word), "letter word from the category: ", game_category )
    guess = ""
    guess_count = 0

    while guess != game_word:
        print("\n\t\t", "".join(blank_word))
        user_input = input("Enter Guess: \t").lower()
        guess_count += 1
        if user_input == game_word:
            print("\nYou guessed right.", "You guessed the right answer in ", guess_count,"tries.")
            break
        else:
            print("\nIncorrect guess. Lemme reveal a letter to help.")
     
            #printing out a random letter of gameword for user     
            active2 = True
            while active2 :
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-" :
                    blank_word[letter_index] = game_word[letter_index]
                    active2 = False

    prompt = input("\nWould you like to try again? (y/n): \t").lower()        
    if prompt != "y":
        active = False 
        print("Okay, bye.")             


