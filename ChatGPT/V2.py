import random

level = 1
class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_monster(self, monster):
        damage = self.attack - monster.defense
        monster.health -= damage
        print(f"{self.name} deals {damage} damage to {monster.name}. {monster.name}'s health is now {monster.health}.")
        if monster.health <= 0:
            print(f"{monster.name} has been defeated!")
            return True
        else:
            return False

    def pick_up_item(self, item):
        self.attack += item.attack_bonus
        self.defense += item.defense_bonus
        print(f"{self.name} picked up {item.name} and gained {item.attack_bonus} attack and {item.defense_bonus} defense.")
        if item.name == "Potion":
            self.health += item.health_bonus
            print(f"{self.name}'s health is now {self.health}.")


class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = self.attack - player.defense
        player.health -= damage
        print(
            f"{self.name} deals {damage} damage to {player.name}. {player.name}'s health is now {player.health}.")
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return True
        else:
            return False


class Item:
    def __init__(self, name, attack_bonus, defense_bonus, health_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.health_bonus = health_bonus


class Room:
    def __init__(self):
        self.type = "regular"


class StartRoom(Room):
    def __init__(self):
        self.type = "start"


class EndRoom(Room):
    def __init__(self):
        self.type = "end"


class TreasureRoom(Room):
    def __init__(self):
        self.type = "treasure"


class MonsterRoom(Room):
    def __init__(self):
        self.type = "monster"


class Dungeon:
    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.level = level
        self.player_position = [0, 0]
        self.dungeon_layout = self.generate_map()

    def generate_map(self):
        def __init__(self, width, height, level):
            self.width = width
            self.height = height
            self.level = level
            self.dungeon_layout = []
            self.generate_map()
            layout = [[Room() for j in range(self.width)]
                      for i in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    if i == 0 and j == 0:
                        layout[i][j] = StartRoom()
                    elif i == self.height - 1 and j == self.width - 1:
                        layout[i][j] = EndRoom()
                    else:
                        layout[i][j] = random
            for i in range(10):
                row = []
                for j in range(10):
                    if i == 0 or i == 9 or j == 0 or j == 9:
                        row.append("wall")
                    elif i % 2 == 0 and j % 2 == 0:
                        row.append("wall")
                    else:
                        if random.random() < 0.3:
                            row.append("room")
                        else:
                            row.append("corridor")
                    self.dungeon_layout.append(row)
                # place items and monsters in rooms
                for i, row in enumerate(self.dungeon_layout):
                    for j, elem in enumerate(row):
                        if elem == "room":
                            if random.random() < 0.3:
                                self.dungeon_layout[i][j] = Room(
                                    "treasure", [random.choice(items)], [])
                            elif random.random() < 0.5:
                                self.dungeon_layout[i][j] = Room(
                                    "battle", [], [random.choice(monsters)])
                            else:
                                self.dungeon_layout[i][j] = Room(
                                    "empty", [], [])
                self.player_position = [
                    random.randint(1, 8), random.randint(1, 8)]
                self.dungeon_layout.append(row)
                return self.dungeon_layout

    def print_map(self, player_position):
        if not self.dungeon_layout:
            return
        for i, row in enumerate(self.dungeon_layout):
            for j, elem in enumerate(row):
                if i == player_position[0] and j == player_position[1]:
                    print("P", end=" ")
                else:
                    print(elem[0], end=" ")
            print()


items = [Item("Sword", 5, 3, 0), Item(
    "Shield", 0, 5, 0), Item("Potion", 0, 0, 10)]
monsters = [Monster("Goblin", 20, 5, 2), Monster(
    "Orc", 30, 8, 4), Monster("Dragon", 50, 10, 8)]

player = Player("Player", 100, 10, 5)
dungeon = Dungeon(random.randint(5, 15), random.randint(5, 15), level)
dungeon.generate_map()
dungeon.print_map(dungeon.player_position)

while player.health > 0:
    print("You are in a",
          dungeon.dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].type, "Room.")
    if dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].type == "battle":
        print("You are being attacked by a",
              dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].monsters[0].name + "!")
        while dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].monsters[0].health > 0:
            player.attack_monster(
                dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].monsters[0])
            if dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].monsters[0].health <= 0:
                del dungeon_layout[dungeon.player_position[0]
                                   ][dungeon.player_position[1]].monsters[0]
                break
            else:
                if player.attack_monster(dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].monsters[0]):
                    print("You have been defeated.")
                    exit()
    elif dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].type == "treasure":
        print("You have found some treasure!")
        for item in dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].items:
            print("You obtained a", item.name, "with attack bonus of",
                  item.attack_bonus, "and defense bonus of", item.defense_bonus)
            player.inventory.append(item)
        dungeon_layout[dungeon.player_position[0]
                       ][dungeon.player_position[1]].items = []
        print("What direction would you like to move? (north, south, east, west)")
        move = input()
        if move == "north":
            if dungeon.player_position[0] > 0:
                dungeon.player_position[0] -= 1
            elif move == "south":
                if dungeon.player_position[0] < len(dungeon_layout) - 1:
                    dungeon.player_position[0] += 1
            elif move == "east":
                if dungeon.player_position[1] < len(dungeon_layout[0]) - 1:
                    dungeon.player_position[1] += 1
            elif move == "west":
                if dungeon.player_position[1] > 0:
                    dungeon.player_position[1] -= 1
            else:
                print("Invalid move.")
            print("You are now in room", dungeon.player_position)
            print("You have", player.health, "health remaining.")
        elif dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].type == "boss":
            print("You have encountered the boss!",
                  dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].boss.name)
            while dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].boss.health > 0:
                player.attack_monster(
                    dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].boss)
                if dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].boss.health <= 0:
                    print("You have defeated the boss!")
                    exit()
                else:
                    if player.attack_monster(dungeon_layout[dungeon.player_position[0]][dungeon.player_position[1]].boss):
                        print("You have been defeated.")
                        exit()
