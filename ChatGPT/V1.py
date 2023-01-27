import random

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_monster(self, monster):
        damage = self.attack - monster.defense
        monster.health -= damage
        print(f"{self.name} deals {damage} damage to {monster.name}")
        if monster.health <= 0:
            print(f"{monster.name} has been defeated!")
            return True
        else:
            return False
        
    def pick_up_item(self, item):
        self.attack += item.attack_bonus
        self.defense += item.defense_bonus
        print(f"{self.name} picked up {item.name} and gained {item.attack_bonus} attack and {item.defense_bonus} defense")

class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def attack_player(self, player):
        damage = self.attack - player.defense
        player.health -= damage
        print(f"{self.name} deals {damage} damage to {player.name}")
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return True
        else:
            return False

class Item:
    def __init__(self, name, attack_bonus, defense_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus


# generate random dungeon layout
dungeon_layout = [[random.choice(["room", "corridor"]) for _ in range(5)] for _ in range(5)]

# create player character
player = Player("Player", 100, 10, 5)

# create monsters
monsters = [Monster("Skeleton", 20, 5, 2), Monster("Zombie", 30,8, 3), Monster("Goblin", 15, 6, 1)]

# create items
items = [Item("Sword", 3, 0), Item("Shield", 0, 2), Item("Potion", 0, 0)]

# player position
player_x, player_y = 0,0

# main game loop
while True:
    # display dungeon layout
    for i, row in enumerate(dungeon_layout):
        for j, elem in enumerate(row):
            if i == player_x and j == player_y:
                print("P", end=" ")
            else:
                print(elem, end=" ")
        print()

    # get player's next move
    move = input("Where would you like to move? (up, down, left, right)")

    # update player's position
    if move == "up":
        player_x -= 1
    elif move == "down":
        player_x += 1
    elif move == "left":
        player_y -= 1
    elif move == "right":
        player_y += 1
    else:
        print("Invalid move")
        continue

    # check if player moved out of bounds
    if player_x < 0 or player_x >= len(dungeon_layout) or player_y < 0 or player_y >= len(dungeon_layout[0]):
        print("You cannot move out of the dungeon!")
        player_x, player_y = max(0, player_x), max(0, player_y)
        player_x, player_y = min(player_x, len(dungeon_layout)-1), min(player_y, len(dungeon_layout[0])-1)
        continue

    # check if player entered a room
    if dungeon_layout[player_x][player_y] == "room":
        print("You have entered a room!")
        # check if room contains a monster
        if random.random() < 0.3:
            current_monster = random.choice(monsters)
            print(f"A wild {current_monster.name} appeared!")
            while True:
                action = input("What would you like to do? (fight, run)")
                if action == "fight":
                    if player.attack_monster(current_monster):
                        # player defeated monster
                        if random.random() < 0.5:
                            # 50% chance of monster dropping an item
                            dropped_item = random.choice(items)
                            print(f"{current_monster.name} dropped {dropped_item.name}")
                            pick_up = input(f"Would you like to pick up {dropped_item.name}? (yes, no)")
                            if pick_up == "yes":
                                player.pick_up_item(dropped_item)
                        break
                elif action == "run":
                    # player runs away
                    if random.random() < 0.3:
                        print("You successfully ran away!")
                        break
                    else:
                        print("You failed to run away.")
                        if player.attack_monster(current_monster):
                            print("You were defeated by the monster.")
                            break
                else:
                    print("Invalid action")
    else:
        # player entered a corridor
        print("You have entered a corridor.")


