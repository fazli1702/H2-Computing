#
# Mission : Hungry Games, Part 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class Fazli_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # Returns the objects at the current location, including other Tributes, but excluding yourself 
        objects_around = self.objects_around()
        # Returns a list of your Tribute’s current inventory
        inventory = self.get_inventory()

        # Returns your Tribute’s current health 
        health = self.get_health()
        # Returns the tuple of weapons currently in your inventory
        weapons = self.get_weapons()
        # Returns the tuple of food currently in your inventory
        food = self.get_food()
        # Returns the tuple of medicines currently in your inventory
        medicine = self.get_medicine()
        # Returns your Tribute’s current hunger
        hunger = self.get_hunger()
        # Returns the list of possible exits at your current location
        exits = self.get_exits()

        """
        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)

        # Otherwise, do nothing
        return None
        
        """


        """
        a. min_damage() of weapons
        b. max_damage() of weapons
        c. weapon_type() of ammos
        d. shots_left() of ranged weapons
        
        
        a. ("ATTACK", LivingThing object, Weapon object) : Attacks LivingThing with Weapon
        b. ("TAKE", Thing object) : Takes Thing and puts it in your inventory. Note that your Tribute can only take Thing if it is in the same Place as the Tribute.
        c. ("EAT", Food object) : Eats the Food in your inventory
        d. ("GO", Direction) : Goes to Direction (one of the values in self.get_exits())
        e. ("LOAD", RangedWeapon object, Ammo object) : Loads Ammo for RangedWeapon
        f. None: Do nothing
        
        """



        #if low health, eat medicine
        if health <= 30:
            if medicine != ():
                return ('EAT', max(medicine))
            #if no medicine, run away
            else:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)

        #if low hunger, eat food
        elif hunger <= 30:
            if food != ():
                return ('EAT', max(food))
            #if no food, run away
            else:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)

        #if inventory empty
        elif inventory == []:
            for item in objects_around:
                
                #if there is tribute in area
                if type(item) is Tribute:
                    #if no weapon
                    if weapons == ():
                        
                        #if enemy no weapon, continue taking items
                        if item.get_weapons == ():
                            pass
                        #else, run away
                        else:
                            index = random.randint(0, len(exits)-1)
                            direction = exits[index]
                            return ("GO", direction)
                        
                    #else, attack with weapon with highest min damage
                    else:
                        weapon = weapons[0].min_damage()
                        weapon_i = 0
                        for i in range(len(weapons)):
                            if weapons[i].min_damage() > weapon:
                                weapon = weapons[i]
                                weapon_i = i
                        return ('ATTACK', item, weapon)


                    
                #if animal, attack animal
                elif type(item) is Animal:
                    if self.weapons != ():
                        return ('ATTACK', item, weapons[0])

                #if ammo, reload ranged weapon
                elif type(item) is Ammo:
                     for weapon in weapons:
                         if type(weapon) is RangedWeapon:
                             return ('LOAD', weapon, item)


                else:
                    return ('TAKE', item)


            else:
                return None
                        


                    
                            
                            
                            








# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = Fazli_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken



##Fazli_AI.next_action(('TAKE', Thing))
##Fazli_AI.next_action(('ATTACK', LivingThing, Weapon))
##Fazli_AI.next_action(('EAT', Food))






# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.task1(Fazli_AI("XX AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

##time_limit = 20    # You may change the time limit if your AI is taking too long
##simulation.task2(Fazli_AI("XX AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.optional_task(XX_AI("XX AI", 100), config, gui=False)
