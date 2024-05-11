import random
import numpy as np


class Pokemon:
    def __init__(self, name, hp, pokemon_type, moves):
        self.name = name
        self.hp = hp
        self.type = pokemon_type
        self.moves = moves
        self.type_changed = False
    
    def __str__(self):
        return f"{self.name} - Type: {self.type}, HP: {self.hp}, Moves: {', '.join(self.moves)}"

    def change_type_to_grass(self):
        if not self.type_changed and random.random() < 0.5:
            self.type = "Grass"
            self.type_changed = True
    
    def use_random_move(self):
        return random.choice(self.moves)
    
    def calculate_damage_range(self, attacker_type, defender_type):
        if attacker_type == "Fire" and defender_type == "Water":
            return [46, 46, 47, 47, 48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 54, 54]
        elif attacker_type == "Fire" and defender_type == "Grass":
            return [306, 308, 312, 314, 318, 324, 326, 330, 332, 336, 342, 344, 348, 350, 354, 360]
        elif attacker_type == "Grass" and defender_type == "Water":
            return [306, 308, 312, 314, 318, 324, 326, 330, 332, 336, 342, 344, 348, 350, 354, 360]
        elif attacker_type == "Grass" and defender_type == "Grass":
            return [46, 46, 47, 47, 48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 54, 54]
        elif attacker_type == "Water" and defender_type == "Fire":
            return [306, 308, 312, 322, 323, 324, 326, 330, 332, 336, 342, 344, 348, 350, 354, 360]
        elif attacker_type == "Water" and defender_type == "Grass":
            return [46, 46, 47, 47, 48, 49, 49, 50, 50, 51, 51, 52, 52, 54, 54, 55]
        elif attacker_type == "Ice" and defender_type == "Fire":
            return [46, 46, 47, 47, 48, 49, 49, 50, 50, 51, 51, 52, 52, 54, 54, 55]
        elif attacker_type == "Ice" and defender_type == "Grass":
            return [306, 308, 312, 322, 323, 324, 326, 330, 332, 336, 342, 344, 348, 350, 354, 360]

    def calculate_damage(self, damage_range,attacker_type):
        initial_damage = random.choice(damage_range)
        accuracy_check = random.randint(1, 100)
        
        if (attacker_type == "Fire" and accuracy_check >= 85) or \
        (attacker_type == "Grass" and accuracy_check >= 90) or \
        (attacker_type == "Water" and accuracy_check >= 80) or \
        (attacker_type == "Ice" and accuracy_check >= 70):
            return 0
        
        critical = random.randint(1, 16)
        if critical == 1:
            return initial_damage * 6
        else:
            return initial_damage

def simulate_battle(pokemon1, pokemon2):
    first_attack_type_pokemon1 = None
    first_attack_type_pokemon2 = None

    while pokemon1.hp > 0 and pokemon2.hp > 0:
        if pokemon2.hp > 0:
            pokemon2.change_type_to_grass()
        if pokemon1.hp > 0:
                pokemon1.change_type_to_grass()

        if first_attack_type_pokemon1 is None:
            first_attack_type_pokemon1 = pokemon1.use_random_move()
            Attack_type1 = first_attack_type_pokemon1
        else:
            Attack_type1 = pokemon1.use_random_move()

        if first_attack_type_pokemon2 is None:
            first_attack_type_pokemon2 = pokemon2.use_random_move()
            Attack_type2 = first_attack_type_pokemon2
        else:
            Attack_type2 = pokemon2.use_random_move()

        damage_range = pokemon1.calculate_damage_range(Attack_type1, pokemon2.type)
        damage = pokemon1.calculate_damage(damage_range, Attack_type1)
        if damage > 0:
            pokemon2.hp -= damage
            if pokemon2.hp <= 0:
                break

        if pokemon1.hp > 0:

            damage_range = pokemon2.calculate_damage_range(Attack_type2, pokemon1.type)
            damage = pokemon2.calculate_damage(damage_range, Attack_type2)
            if damage > 0:
                pokemon1.hp -= damage
                if pokemon1.hp <= 0:
                    break

    pokemon1_final_type = pokemon1.type
    pokemon2_final_type = pokemon2.type
    Ganador = 0
    if pokemon1.hp > 0:
        Ganador = 1

    return first_attack_type_pokemon1, pokemon1_final_type,first_attack_type_pokemon2, pokemon2_final_type, Ganador


Blastoise = Pokemon("Blastoise", 321, "Water", ["Water","Ice"])
Arcanine = Pokemon("Arcanine", 321, "Fire", ["Fire","Grass"])

Pokemons = [Blastoise,Arcanine]

def create_confusion_matrix():
    # Initialize confusion matrix dictionary
    confusion_matrix = {}

    # Define the attacking types and typings
    attacking_types_Blastoise = ["Water", "Ice"]
    attacking_types_Arcanine = ["Fire", "Grass"]
    defensive_types_Blastoise = ["Water", "Grass"]
    defensive_types_Arcanine = ["Fire", "Grass"]

    # Initialize confusion matrix with zeros
    for attacking_type_pokemon1 in attacking_types_Blastoise:
        for attacking_type_pokemon2 in attacking_types_Arcanine:
            for defensive_type_pokemon1 in defensive_types_Blastoise:
                for defensive_type_pokemon2 in defensive_types_Arcanine:
                    confusion_matrix[(attacking_type_pokemon1, defensive_type_pokemon1, attacking_type_pokemon2, defensive_type_pokemon2)] = {
                        'total_battles': 0,
                        'win_count': 0,
                        'win_ratio': 0.0
                    }

    return confusion_matrix

Confusion_matrix = create_confusion_matrix()

def Simulation(confusion_matrix,pokemon1,pokemon2):
    # Simulate each battle and get the attacking and defensive types of both Pokémon
    first_attack_type_pokemon1, pokemon1_final_type, first_attack_type_pokemon2, pokemon2_final_type, Ganador = simulate_battle(pokemon1, pokemon2)

    # Update the confusion matrix based on the battle results
    confusion_matrix_key = (first_attack_type_pokemon1, pokemon1_final_type, first_attack_type_pokemon2, pokemon2_final_type)

    confusion_matrix[confusion_matrix_key]['total_battles'] += 1

    if Ganador == 1:
        confusion_matrix[confusion_matrix_key]['win_count'] += 1

    for key, value in confusion_matrix.items():
        if value['total_battles'] > 0:
            value['win_ratio'] = value['win_count'] / value['total_battles']
        else:
            value['win_ratio'] = 0.0
    
    return confusion_matrix

for i in range(10000000):
    Blastoise = Pokemon("Blastoise", 321, "Water", ["Water","Ice"])
    Arcanine = Pokemon("Arcanine", 321, "Fire", ["Fire","Grass"])
    Simulation(Confusion_matrix, Blastoise, Arcanine)

print(Confusion_matrix)
