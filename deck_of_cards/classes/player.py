from . import deck
import random

class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.record = {
            "wins" : 0,
            "losses" : 0
        }
        self.hand = []

    def reveal_hand(self):
        for card in self.hand:
            card.card_info()

    def play_cards(self, cpu, round):
        input(f"\nRound {round} beings!\nHit enter to play your card!")
        print(f"\n{self.name} plays a {self.hand[0].string_val} of {self.hand[0].suit} \n")

        input(f"Time for {cpu.name} to play their card!")
        print(f"\n{cpu.name} plays a {cpu.hand[0].string_val} of {cpu.hand[0].suit} \n")
        card_pot = []
        war = 1
        player_value = self.hand[0].point_val
        cpu_value = cpu.hand[0].point_val

        card_pot.append(self.hand.pop(0))
        card_pot.append(cpu.hand.pop(0))
        
        if player_value > cpu_value:
            print(f"{self.name} wins and takes both cards!")
            for card in card_pot:
                self.hand.append(card)
            input(f"You now have {len(self.hand)} cards in your deck")
        elif cpu_value > player_value:
            print(f"{cpu.name} wins and takes both cards!")
            for card in card_pot:
                cpu.hand.append(card)
            input(f"You now have {len(self.hand)} cards in your deck")
        else: 
            while player_value == cpu_value:
                if len(self.hand) == 0:
                    self.hand = []
                    break
                if len(cpu.hand) == 0:
                    cpu.hand = []
                    break
                input(f"It's time for war round {war}! Press enter to start!")
                war_pot = self.war(cpu)
                card_pot += war_pot
                player_value = self.hand[0].point_val
                cpu_value = cpu.hand[0].point_val
                input(f"\n{self.name} plays a {self.hand[0].string_val} of {self.hand[0].suit} \n")
                input(f"\n{cpu.name} plays a {cpu.hand[0].string_val} of {cpu.hand[0].suit} \n")
                if player_value > cpu_value:
                    input(f"{self.name} wins and takes all the cards! Including...")
                    for card in card_pot:
                        card.card_info()
                        self.hand.append(card)
                    input(f"You now have {len(self.hand)} cards in your deck")
                elif cpu_value > player_value:
                    input(f"{cpu.name} wins and takes all the cards! Including...")
                    for card in card_pot:
                        card.card_info()
                        cpu.hand.append(card)
                    input(f"You now have {len(self.hand)} cards in your deck")
                war += 1

    
    
    def war(self, cpu):
        war_pot = []
        for i in range(3):
            if len(self.hand) == 1 or len(cpu.hand) == 1:
                break
            war_pot.append(self.hand.pop(0))
            war_pot.append(cpu.hand.pop(0))
        return war_pot

