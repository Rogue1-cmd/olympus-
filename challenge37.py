#Casino Blackjack App
import random
import time


class Card:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit
    
    def display_card(self):
        print("\t",self.rank, "of", self.suit)
    

class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"K": 10,"Q": 10,"A":11}    
        
        for suit in self.suits:
            for rank, value in self.ranks.items():
                card = Card(rank,value,suit)
                self.cards.append(card)
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card
            

class Player:
    def __init__(self):
        self.hand = [] #Holds players cards
        self.hand_value = 0 
        self.playing_hand = True
    
    def draw_hand (self, deck):
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)
    
    def display_hand(self): #Display player's hand
        print("\nPlayers Hand: \t")
        for card in self.hand:
            card.display_card()
            time.sleep(1)
        
    def hit(self, deck): #new card for player
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        self.hand_value = 0
        self.ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value

            if card.rank == "A":
                self.ace_in_hand = True
                
        if self.hand_value > 21:
            self.hand_value -= 10
        
        print ("Value: ", self.hand_value)

    def update_hand(self, deck):
        if self.hand_value < 21:
            prompt = input("\nWould you like to hit (y/n): ").lower()
            time.sleep(1)
            if prompt.startswith("y"):
                self.hit(deck)
            else:
                self.playing_hand = False
        else :
            self.playing_hand = False
        

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for i in range(2): 
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        input("\nPress enter to reveal dealers card: \n")
        for card in self.hand:
            card.display_card()
            time.sleep(1) #theatre

    def hit(self, deck):
        self.get_hand_value()

        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
            
        print("\nCards in dealers hand: ", len(self.hand))

    def get_hand_value(self):
        self.hand_value = 0
        self.ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value
            if card.value == "A":
                self.ace_in_hand = True

        if self.hand_value > 21 and self.ace_in_hand:
            self.hand_value -= 10
        
        print (self.hand_value)


class Game:
    def __init__(self, amount):
        self.amount = int(amount)
        self.bet = 20
        self.winner = ""


    def set_bet(self): #gets user's bet for hand
        betting = True
        while betting:
            bet = int(input("\nEnter bet: \t"))
            time.sleep(1)
            if self.bet < 20:
                bet = 20 #in case bet amount is less than minimum

            elif bet > self.amount: #bet placed is more than money available
                print("\nYou cannot afford the bet.")
                betting = False 

            else: #set bet
                self.bet = bet
                betting = False

    def scoring(self, p_value, d_value):
        # 21
        if p_value == 21:
            print("\nPlayer has blackjack. You Win !!!")
            self.winner = "p"

        elif d_value == 21:
            print("\nDealer has blackjack. You lost !!!")
            self.winner = "d"
        #over 21
        elif p_value > 21:
            print("\nPlayer went over 21 !!!\n")
            self.winner = "p"

        elif d_value > 21:
            print("\nDealer went over 21 !!!\n")
            self.winner = "d"

        else:
            if p_value > d_value:
                print("\nPlayer: ",p_value,"\n","Dealer: ", d_value)
                self.winner = "p"

            elif d_value > p_value:
                print("\nDealer: ",d_value,"\n","Player: ", p_value)
                self.winner = "d"

            else :
                print("\nIt was a tie.\nDealer: ", d_value,"\n","Player: ", p_value)
                self.winner = "tie"

    def payout(self):
        #Win
        if self.winner == "p":
            self.amount += self.bet
        #Lost    
        elif self.winner == "d":
            self.amount -= self.bet
        
    def display_money(self):
        print("Amount: ", self.amount)

    def display_money_and_bet(self):
        print("\n\tBet: ", self.bet)
        print("\tTotal Amount: ", self.amount)
        time.sleep(1)

#Main Code
print("\n\t---Welcome to Casino Blackjack---")
print("\nThe minimum bet you can place is $20")
amount = int(input("\nHow much money will you be playing with? \n\t"))

game = Game(amount)
playing = True
while playing:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    game.display_money_and_bet()
    #dealers first card
    print("\nDealer has a ", dealer.hand[0].rank," of ", dealer.hand[0].suit)

    while player.playing_hand:
        player.display_hand()#show hand
        player.get_hand_value()#calculate values
        player.update_hand(game_deck)#hit or stay?

    #round for dealer
    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.amount < 20:
        playing = False
        print("You have ran out of money. Bye.")





        