import time, math, random
from termcolor import colored

attack_power = 1
defence_power = 0
health_amount = 2

goblin_group_1_attack_power = 1
goblin_group_1_defence_power = 1
goblin_group_1_health_amount = 2

goblin_group_2_attack_power = 2
goblin_group_2_defence_power = 2
goblin_group_2_health_amount = 3

goblin_group_3_attack_power = 1
goblin_group_3_defence_power = 0
goblin_group_3_health_amount = 2

mega_goblin_attack_power = 4
mega_goblin_defence_power = 1
mega_goblin_health_amount = 6

start_fight_colored = colored("fight start","red")
armor_buff_gain = colored("you gain +2 defence.","blue")
random_buff = random.choice(["attack_power", "defence_power", "health_amount"])
chapter = 1

while True:
    #chapter_1#
    if chapter == 1:
        print("you've been given a quest to kill a goblin heard in the forest.")
        print("you've also been given two items of your choice from the blacksmith.")
        print("the choices are: zwaard = +1 attack, shield = +1 defence, health fruit = +1 health.")
        eerste_keuze = input("keuze 1: ")
        tweede_keuze = input("keuze 2: ")
        if eerste_keuze == "zwaard" or tweede_keuze == "zwaard":
            attack_power += 1
        elif eerste_keuze == "shield" or tweede_keuze == "shield":
            defence_power += 1
        elif eerste_keuze == "health fruit" or tweede_keuze == "health fruit":
            health_amount += 2
        else:
            print("make a choice on your next run.")
            exit()
        print(f" now with a {eerste_keuze} and a {tweede_keuze} in hand, your ready to enter the forest.")
        #chapter_2#
        chapter = 2
        time.sleep(1)
    elif chapter == 2:
        print("As you enter the forest you see two roads and must chose one.")
        path_choice_1 = input("path 1,path 2 or leaving? ")
        if path_choice_1 == "path 1":
            chapter = 3
            time.sleep(1)
        elif path_choice_1 == "path 2":
            chapter = 4
            time.sleep(1)
        elif path_choice_1 == "leave":
            print("you decide to abandon your quest.")
            exit()
        else:
            print("chose a path on your next run.")
            exit()
        #chapter_3#
    elif chapter == 3:
        print("after walking a while you think you hear something in the bushes before getting jumped by a group of goblins")
        print(start_fight_colored)
        gg1a = goblin_group_1_attack_power - defence_power
        if gg1a <= 0:
            print("you have not taken damage.")
            goblin_group_1_damage = 0
        else:
            goblin_group_1_damage = math.ceil(health_amount / gg1a)

        paa = attack_power - goblin_group_1_defence_power
        player_damage = math.ceil(goblin_group_1_health_amount / paa)

        if player_damage > goblin_group_1_damage:
            print(f"in {player_damage} rounds you'll win.")
            print(f"your health is now {health_amount - goblin_group_1_attack_power}.")
        else:
            print("you have been defeated.")
            print("game over.")
            exit()
        chapter = 5
        time.sleep(1)
        #chapter_4#
    elif chapter == 4:
        print("at some point during your walk on path 2 you find a slightly broken sturdy armor, but still usable")
        print(armor_buff_gain)
        defence_power += 2
        chapter = 5
        time.sleep(1)
        #chapter_5#
    elif chapter == 5:
        print("when you are done on either path 1 or 2 and walked for a bit, you end up in an open field")
        print("you know that the goblincamp is a bit further away, but to get there you'll have to chose one of three paths.")
        path_choice_2 = input("chose one of the three paths leading to the camp or to leave: ")
        if path_choice_2 == "1":
            chapter = 6
            time.sleep(1)
        elif path_choice_2 == "2":
            chapter = 7
            time.sleep(1)
        elif path_choice_2 == "3":
            chapter = 8
            time.sleep(1)
        elif path_choice_2 == "leave":
            print("you decided to abandon your quest")
            exit()
        else:
            print("chose a path on your next run.")
            exit()
        #chapter_6#
    elif chapter == 6:
        print("while you are walking to the camp you walk into an old man.")
        print("he gives you a slight smile and then casts a spell on you before he disapears in a puff of smoke.")
        random_buff_colored = colored(f"you gain more {random_buff}.","blue")
        print(random_buff_colored)
        if random_buff == "attack_power":
            attack_power += 2
        elif random_buff == "defence_power":
            defence_power += 2
        elif random_buff == "health_amount":
            health_amount += 2
        chapter = 9
        time.sleep(1)
        #chapter_7#
    elif chapter == 7:
        print("you for one reason or another gain either more defence or more power.")
        buff_choice = input("want more attack of more defence? ")
        if buff_choice == "attack":
            attack_power += 1
        elif buff_choice == "defence":
            defence_power += 1
        else:
            print("chose an option on your next run.")
            exit()
        chapter = 9
        time.sleep(1)
        #chapter_8#
    elif chapter == 8:
        print("you run into a few goblins who are not happy to see you")
        print(start_fight_colored)
        gg2a = goblin_group_2_attack_power - defence_power
        if gg2a <= 0:
            print("you have not taken damage.")
            goblin_group_2_damage = 0
        else:
            goblin_group_2_damage = math.ceil(health_amount / gg2a)

        paa_2 = attack_power - goblin_group_2_defence_power
        player_damage = math.ceil(goblin_group_2_health_amount / paa_2)

        if player_damage > goblin_group_2_damage:
            print(f"in {player_damage} rounds you'll win.")
            print(f"your health is now {health_amount - goblin_group_2_attack_power}.")
            chapter = 10
            time.sleep(1)
        else:
            print("you have been defeated.")
            print("game over.")
            exit()
        #chapter_9#
    elif chapter == 9:
        print("after the events on your path of choice you end up at the goblincamp.")
        approach = input("chose your approach[stealth, brute force or leave] ")
        if approach == "stealth":
            chapter = 11
            time.sleep(1)
        elif approach == "brute force":
            chapter = 12
            time.sleep(1)
        else:
            print("chose an approach on your next run.")
            exit()
        #chapter_10#
    elif chapter == 10:
        print("after the fight with the goblin group you find the perfect spot to ambush the goblins as well as a longbow giving you +3 attack")
        attack_power += 3
        chapter = 12
        time.sleep(1)
        #chapter_11#
    elif chapter == 11:
        print("you manage to hide from the goblins in the camp, but you run into the mega goblin")
        print(start_fight_colored)
        mga = mega_goblin_attack_power - defence_power
        if mga <= 0:
            print("you have not taken damage.")
            mega_goblin_damage = 0
        else:
            mega_goblin_damage = math.ceil(health_amount / mga)

        paa_3 = attack_power - mega_goblin_defence_power
        player_damage = math.ceil(mega_goblin_health_amount / paa_3)

        if player_damage > mega_goblin_damage:
            print(f"in {player_damage} rounds you'll win.")
            print(f"your health is now {health_amount - mega_goblin_attack_power}.")
            chapter = 12
            time.sleep(1)
        else:
            print("you have been defeated.")
            print("game over.")
            exit()
        #chapter_12#
    elif chapter == 12:
        print("when you go into the goblin camp by either sneaking,brute force or ambushing you find the last group of goblins")
        print(start_fight_colored)
        gg3a = goblin_group_3_attack_power - defence_power
        if gg3a <= 0:
            print("you have not taken damage.")
            goblin_group_3_damage = 0
        else:
            goblin_group_3_damage = math.ceil(health_amount / gg3a)

        paa_4 = attack_power - goblin_group_3_defence_power
        player_damage = math.ceil(goblin_group_3_health_amount / paa_4)

        if player_damage > goblin_group_3_damage:
            print(f"in {player_damage} rounds you'll win.")
            print(f"your health is now {health_amount - goblin_group_3_attack_power}.")
            chapter = 13
            time.sleep(1)
        else:
            print("you have been defeated.")
            print("game over.")
            exit()
        #chapter_13#
    elif chapter == 13:
        print("now that you have killed all the goblins you return to the town and finish the quest.")
        print("THE END")
        exit()