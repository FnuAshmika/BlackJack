import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Club', 'Diamond', 'Heart', 'Spade']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = 0
        contain_ace = False
        for card in self.hand:
            if card.rank == 'A':
                contain_ace = True
                value += 11

            elif card.rank in ['J', 'Q', 'K']:
                value += 10
                
            else:
                value += int(card.rank)
        if contain_ace == True and value > 21:
            value -= 10
        return value

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        
        

    def game_begins(self):
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Player()
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        print("-" * 25)
        print("Welcome to Blackjack!")
        print("-" * 25)
        print(f"Dealer's hand:[{self.dealer.hand[0].rank}] ")
        print(f"Your hand: [{self.player.hand[0].rank}, {self.player.hand[1].rank}] ")
        if self.player.hand_value() == 21:
            print("BlackJack!!! You Win")
        else:
            while True:
                choice = input("Do you wanna hit or stand? ")
                if choice == 'hit' :
                    self.player.add_card(self.deck.deal())
                    print(f"Your hand: {[card.rank for card in self.player.hand]}")
                    if self.player.hand_value() == 21:
                        print("BlackJack!!! You Win")
                        return
                    if self.player.hand_value() > 21:
                        print("Bust!!! Dealer wins.")
                        return
                elif choice == 'stand' :
                    break
                else:
                    print("Invalid choice. Please enter 'hit' or 'stand'. ")
            print(f"Dealer's hand: {[card.rank for card in self.dealer.hand]}")
            while self.dealer.hand_value() < 17:
                self.dealer.add_card(self.deck.deal())
                print(f"Dealer's hand: {[card.rank for card in self.dealer.hand]}")
            if self.dealer.hand_value()> 21:
                print("Dealer lose!!! You win.")
            elif self.player.hand_value() > self.dealer.hand_value():
                print("You win.")
            elif self.player.hand_value() < self.dealer.hand_value():
                print("Dealer wins.")
            else:
                print("Game Over!!")
        


   
    

while True:
    game = Blackjack()
    game.game_begins()
    choice = input("Do you want to play again? (y/n) ")
    if choice != 'y':
        print("~" * 25)
        print("Thank you for playing!")
        print("~" * 25)
        break
