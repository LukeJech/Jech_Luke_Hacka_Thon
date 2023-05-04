from classes.deck import Deck
from classes.player import Player

bicycle = Deck()

# War - each opponent starts with half of the deck

player_name = "kii"
player_name = input("Challenger, what is your name? ")
player_info = {
    "name": player_name,
}
player = Player(player_info)

cpu_info = {
    "name": "Ultron",
}
cpu = Player(cpu_info)




# each round player pulls top card from deck and whoever has the higher card wins and takes their card
def play_game():
    round = 1
    delt_hands = bicycle.deal_hands()
    player.hand = delt_hands[0]
    cpu.hand = delt_hands[1]
    while len(player.hand) > 0 and len(cpu.hand) > 0:
        player.play_cards(cpu, round)
        round += 1

    if len(player.hand) > 0:
        print(f"Yay you took down the great and might {cpu.name}")
        player.record["wins"] += 1
        
    else:
        print(f"Sorry it looks like you lost to {cpu.name} this time.")
        player.record["losses"] += 1
    print(f"Your record is now {player.record}")

    play_again = input("Play again?: Y or N Your answer:")
    if play_again.upper() == "Y":
        play_game()

play_game()



# If the players have same value of card, then War begins where each player puts down 3 more cards facedown, then the 4th card determines who wins all the cards in the pot

# Game is over when one player is out of cards and the other player is the winner




