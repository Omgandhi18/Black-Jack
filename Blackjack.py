import random
from blackjackart import logo
from os import system 
def screen_clear():
    _=system('cls')
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)
def compare(user_score,comp_score):
    if user_score==comp_score:
        return "DRAW"
    elif comp_score==0:
        return "LOSE, Opponent has Blackjack "
    elif  user_score==0:
        return "WIN with a Blackjack"
    elif user_score>21:
        return "You went Over, You lose"
    elif comp_score>21:
        return "Opponent went over. You win"
    elif user_score>comp_score:
        return "You win"
    else:
        return "You lose" 
def play_game():
    print(logo)
    is_gameover=False
    user_card=[]
    computer_card=[]

    for _ in range(2):
        new_card=deal_card()
        user_card.append(new_card)
        computer_card.append(deal_card())
    while not is_gameover:

        user_score=calculate_score(user_card)
        comp_score=calculate_score(computer_card)
        print(f"{user_card}   {user_score}")
        print(f"{computer_card[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
            is_gameover=True
        else:
            choice=input("Type 'y' to get another card, type 'n' to pass: ")
            if choice=="y":
                user_card.append(deal_card())
            else:
                is_gameover=True
    while comp_score!=0 and comp_score<17:
        computer_card.append(deal_card())
        comp_score=calculate_score(computer_card)
    print(f"Your Final deck: {user_card} ,final score: {user_score}")
    print(f"Opponent Final deck: {computer_card} ,final score: {comp_score}")
    print(compare(user_score,comp_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    screen_clear()
    play_game()

