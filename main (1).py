############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
"""We are import random and clear function from python library and import logo from art.py file."""
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck.We choose a card with random function from the card deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    """When we get a blackjack and get 2 len in the card list we return 0 and stopped the function."""
    return 0
  if 11 in cards and sum(cards) > 21:
    """When we get 11 and if cards sum is more than 21 we change 11 with 1 -remove and append function."""
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compare function that we create is help us to get the end of the game.Be carefull with sequence of if/else statements."""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  """Play game function help us to get more cards in the game and restart the game."""
  print(logo)
  """Create two list for computer and user."""
  user_cards =[]
  computer_cards =[]
  """is game over variable help us to restart the game with while function."""
  is_game_over = False

  for _ in range(2):
    """For cycle give us to append cards to variables."""
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    """Call calculator function."""
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        """  When user enter 'y' he get one more card."""
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    """With this while cycle gives a algorithm for computer user to get more cards after user get one card but computer get card when it does not hit the blackjack or the calculation of computer cards <17."""
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    """Print the final hand and call the compare function."""
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


"""The start of the code."""
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
