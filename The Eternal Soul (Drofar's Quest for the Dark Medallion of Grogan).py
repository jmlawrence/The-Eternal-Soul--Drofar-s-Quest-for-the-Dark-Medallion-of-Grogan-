# from Tkinter import *f
import random
import os
from time import sleep
from copy import deepcopy
title_sequence = open("title_sequence.txt", 'r').read()
choose_class = open("choose_your_class.txt", 'r').read()


def main():
    key = False
    killed_enemies = [False, False, False]
    start = ("Keep going")
    stats = []
    health = 20
    max_hp = 20
    xp = 0
    while (start != "quit"):
        print(title_sequence)
        start = input('                                     ')
        space(50)
        user_class = "Z"
        while (user_class.upper() != "A" and user_class.upper() != "B" and user_class.upper() != "C" and user_class.upper() != "D"):
            print(choose_class)
            space(4)
            user_class = input(
                "             A|Warrior                                   B|Mage \n\n                                     ")

            # Warrior stats
            if (user_class.upper() == "A"):
                # [class, strength, magic, gold]
                stats = [1, 5, 5, 50]

            # Mage stats
            if (user_class.upper() == "B"):
                stats = [2, 1, 5, 50]

        space(50)
        '''print("The Eternal Soul burns with the fire of a thousand flames. So the day cometh\n")
        sleep(3)
      
        print("when evil shall rise from the depths of everlasting anguish thrust itself upon\n")
        sleep(3)
      
        print("mankind by the Dark One, Grogan. Long ago in ages past there was a band of\n")
        sleep(3)
  
        print("orcan nomads called the Undeludenubenshlag. They were a fearsome orcs that\n")
        sleep(3)

        print("went about ravaging the lands of Ordania. One day a simple woodsman fed up\n")        
        sleep(3)

        print("with the Undeludenubenshlag set out on a quest for the eventual banishment of\n")
        sleep(3)

        print("all things evil. He sought after the fabled mage named Jephoratalikin \n")
        sleep(3)

        print("he would master the way of the blade and the bow. It was long told that\n")
        sleep(3)

        print("Jephoratalikin had once been general of the great Ondeluption army and knew\n")
        sleep(3)
   
        print("well the way of battle. He was also said to be a master magician without\n")
        sleep(3)
    
        print("the power to level mountains and set fire the the very sky. It is said\n")
        sleep(3)

        print("that the woodsman never found Jephoratalikin, and went mad with rage. He then\n")
        sleep(3)

        print("set off on a new journey, a journey to hnt down and kill the Undeludenubenshlag\n")
        sleep(3)

        print("with nothing more than anger and brute force. The Massacre of The Seven Swans\n")
        sleep(3)

        print("is a well known tale told to small children. It is said that a man, red with\n")
        sleep(3)

        print("rage, stormed a camp of orcs and slaughtered all of them in such a gruesome\n")
        sleep(3)

        print("manner the earth was stained purple with the blood of their collective bodies.\n")
        sleep(3)

        print("The site of this dark tale is known as the violet hill. No one has dared\n")
        sleep(3)

        print("approach this site in over a thousand years. It is said that this is where\n")
        sleep(3)

        print("the Undeludenubenshlag were finally stopped from continuing their tour of\n")
        sleep(3)

        print("pure evil. Though few truly understand what this means. When a man commits\n")
        sleep(3)

        print("murder to stop the perpetuation of pure evil by way of pure evil a force so\n")
        sleep(3)

        print("powerful is formed none dare consider the true meaning of this action. It has\n")
        sleep(3)

        print("only happened but twice in the history of Ordania. Once at the beginning of\n")
        sleep(3)

        print("time and again when the woodsman murdered the Undeludenubenshlag by ways of\n")
        sleep(3)

        print("extreme brutality and vile torture. That was the day Gragan was formed and\n")
        sleep(3)

        print("evil rose from the ashes of despair and reached it's apex at the zenith of true\n")
        sleep(3)

        print("and unashamed horror. Evil now had a face, and boy was it ugly. We now skip\n")
        sleep(3)

        print("forward in time to the days of future past. It is a time of relative peace,\n")
        sleep(3)
 
        print("but the brooding evil of Grogan floats beneath the surface of all things.\n")
        sleep(3)

        print("Many claim evil has returned to the hole from whence it came, but the few,\n")
        sleep(3)

        print("the intelligent still believe that a day shall come when this evil must be\n")
        sleep(3)

        print("banished for good. A young boy, Drofar from the town of Dragonsbane, has just\n")
        sleep(3)

        print("turned 14, the age of legal consent in Ordania and it is today that fate shall\n")
        sleep(3)

        print("reveal her face and his destiny shall be made known. The Eternal Soul burns\n")
        sleep(3)

        print("with the fire of a thousand flames. So the day cometh when one shall rise\n")
        sleep(3)

        print("from the depths of evil's despair and banish it from whence it came!\n")
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        print("          This is Drofar's Quest For The Dark Medallion of Grogan.")
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)
        space(1)
        sleep(3)'''
        space(20)

        enemy_type = ("None")
        printstatements(0, enemy_type, stats[0], stats[1], stats[2],
                        key, killed_enemies, stats[3], health, max_hp, xp)


def space(number):
    print("\n" * number)


def position(p, check_key, __killed_enemies, money):

    duplicate = 0

    letter = input("                                     ")
    if (letter.upper() == "A" and 0 <= p <= 11 and p != 3.1 and p != 1 and p != 5 and p != 3.2 and p != 6.5 and p != 6 and p != 2.5 and p != 3.3 and p != 3.4 and p != 7 and p != 7.1 and p != 7.2 and p != 7.3 and p != 7.4 and p != 7.5 and duplicate == 0):
        p += 1
        duplicate += 1

    elif (letter.upper() == "B" and 0 <= p <= 11 and p != 3.1 and p != 1 and p != 5 and p != 3.2 and p != 6.5 and p != 6 and p != 2.5 and p != 3.3 and p != 3. and p != 7 and p != 7.1 and p != 7.2 and p != 7.3 and p != 7.4 and p != 7.5 and duplicate == 0):
        p -= 1
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                 WHEN IN AT SHOP, IN DRAGONSBANE                   #
        #                                                                   #
        #####################################################################

    elif (letter.upper() == "A" and p == -1 and duplicate == 0):
        p = -1.1
        duplicate += 1

    elif (letter.upper() == "B" and p == -1 and duplicate == 0):
        p = -1.2
        duplicate += 1

    elif (letter.upper() == "B" and p == -1.2 and duplicate == 0):
        p = -1
        duplicate += 1

    elif (letter.upper() == "A" and p == -1.2 and duplicate == 0):
        p = -1.21
        duplicate += 1

    # User selects "Return to main square," when at shop, in Dragonsbane
    elif (letter.upper() == "C" and p == -1 and duplicate == 0):
        p = 0
        duplicate += 1

    # USER WANT TO BUY AN APPLE!
    elif (letter.upper() == "A" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money >= 5 and duplicate == 0):
        p = -1.11
        duplicate += 1

    # USER WANT TO BUY A MEDALLION!
    elif (letter.upper() == "B" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money >= 60 and duplicate == 0):
        p = -1.12
        duplicate += 1

    # USER WANT TO BUY AN HP POTION!
    elif (letter.upper() == "C" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money >= 15 and duplicate == 0):
        p = -1.13
        duplicate += 1

    # USER WANT TO BUY AN EMPTY BOTTLE!
    elif (letter.upper() == "D" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money >= 10 and duplicate == 0):
        p = -1.14
        duplicate += 1

    # USER WANT TO BUY AN APPLE, but are too poor
    elif (letter.upper() == "A" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money < 5 and duplicate == 0):
        p = -1.15
        duplicate += 1

    # USER WANT TO BUY A MEDALLION, but are too poor
    elif (letter.upper() == "B" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money < 60 and duplicate == 0):
        p = -1.15
        duplicate += 1

    # USER WANT TO BUY A HEALTH POTION, but are too poor
    elif (letter.upper() == "C" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money < 15 and duplicate == 0):
        p = -1.15
        duplicate += 1

    # USER WANT TO BUY AN EMPTY BOTTLE, but are too poor
    elif (letter.upper() == "D" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and money < 10 and duplicate == 0):
        p = -1.15
        duplicate += 1

    # USER WANT TO STEP BACK FROM THE COUNTER IN THE SHOP, IN THE SILVER PLATTER, IN DRAGONSBANE
    elif (letter.upper() == "E" and (p == -1.1 or p == -1.11 or p == -1.12 or p == -1.13 or p == -1.14 or p == -1.15) and duplicate == 0):
        p = -1
        duplicate += 1

        #####################################################################
        #                                                                   #
        #          WHEN HEARING ABOUT THE HISTORY OF DRAGONSBANE            #
        #                                                                   #
        #####################################################################

    # User selects "Return to Dragonsbane Proper," while listening to the History of Dragonsbane
    elif (letter.upper() == "A" and p == -.4 and duplicate == 0):
        p = -.41
        duplicate += 1

    # User selects "Return to Dragonsbane Proper," while listening to the History of Dragonsbane
    elif (letter.upper() == "B" and p == -.4 and duplicate == 0):
        p = -.42
        duplicate += 1

    # User selects "Return to Dragonsbane Proper," while listening to the History of Dragonsbane
    elif (letter.upper() == "C" and p == -.4 and duplicate == 0):
        p = 0
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                   WHEN IN DRAGONSBANE'S TAVERN                    #
        #                                                                   #
        #####################################################################

    # User selects "Leave tavern," in the tavern
    elif (letter.upper() == "C" and p == -.2 and duplicate == 0):
        p = 0
        duplicate += 1

    # User selects "Enquire about lodging," while talking to the bartender, in the tavern, Dragonsbane.
    elif (letter.upper() == "Z" and p == -.2 and duplicate == 0):
        p = -.25
        duplicate += 1

    # User selects "Go back to tavern," from the bedroom or from sleeping.
    elif (letter.upper() == "C" and (p == -.25 or p == -.253) and duplicate == 0):
        p = -.2
        duplicate += 1

    # User selects "Sleep 2 hours or a day" from the bedroom, in the tavern, in Dragonsbane.
    elif ((letter.upper() == "A" or letter.upper() == "B") and (p == -.25 or p == -.253) and duplicate == 0):
        p = -.253
        duplicate += 1

    # User selects "Talk to Bartender," in Tavern, in Dragonsbane
    elif (letter.upper() == "A" and p == -.2 and duplicate == 0):
        p = -.23
        duplicate += 1

    # User selects "Any Gossip?" in Tavern, in Dragonsbane
    elif (letter.upper() == "C" and p == -.23 and duplicate == 0):
        p = -.233
        duplicate += 1

    # User selects "Accept Quest", while talking to the bartender, in the Tavern, in Dragonsbane
    elif (letter.upper() == "A" and p == -.233 and duplicate == 0):
        p = -.2331
        duplicate += 1

    # User selects "Walk away", while talking to the bartender, in the Tavern, in Dragonsbane
    elif (letter.upper() == "B" and p == -.233 and duplicate == 0):
        p = -.23
        duplicate += 1

    # User selects "Any Gossip?" in Tavern, in Dragonsbane
    elif (letter.upper() == "C" and p == -.23 and duplicate == 0):
        p = -.233
        duplicate += 1

    # User selects "Step back from bar," at the bar in the tavern, in Dragonsbane
    elif (letter.upper() == "D" and p == -.23 and duplicate == 0):
        p = -.2
        duplicate += 1

    # User selects "Step back from bar," at the bar in the tavern, in Dragonsbane
    elif (letter.upper() == "B" and p == -.2 and duplicate == 0):
        p = -.21
        duplicate += 1

    # User selects "Step back from bar," at the bar in the tavern, in Dragonsbane
    elif (letter.upper() == "A" and p == -.23 and duplicate == 0):
        p = -.231
        duplicate += 1

    # User selects "Buys a brew," at the bar in the tavern, in Dragonsbane
    elif (letter.upper() == "B" and p == -.23 and duplicate == 0):
        p = -.232
        duplicate += 1

    # User selects "I'll take it!," while enquiring about lodging, at the bar, in the tavern, in Dragonsbane
    elif (letter.upper() == "A" and p == -.231 and duplicate == 0):
        p = -.25
        duplicate += 1

    # User selects "Step back from bar," while enquiring about lodging, at the bar, in the tavern, in Dragonsbane
    elif (letter.upper() == "C" and p == -.231 and duplicate == 0):
        p = -.2
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                    WHEN IN DRAGONSBANE PROPER                     #
        #                                                                   #
        #####################################################################

   # #User selects "Go to shop," in Dragonsbane
   # elif (letter.upper() == "B" and p == 0 and duplicate == 0):
   #     p = -.1
   #    duplicate += 1

    # User selects "Visit tavern," in Dragonsbane
    elif (letter.upper() == "C" and p == 0 and duplicate == 0):
        p = -.2
        duplicate += 1

    # User selects "History of Dragonsbane," in Dragonsbane
    elif (letter.upper() == "D" and p == 0 and duplicate == 0):
        p = -.4
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 1                        #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Willowton," on position 1, and the orc is ALIVE
    elif (letter.upper() == "A" and p == 1 and duplicate == 0 and __killed_enemies[0] == False):
        p = 2.5
        duplicate += 1

    # User selects "Go toward Willowton," on position 1, and the orc is DEAD
    elif (letter.upper() == "A" and p == 1 and duplicate == 0 and __killed_enemies[0] == True):
        p = 2
        duplicate += 1

    # User selects "Enter Dragonsbane," on position 1
    elif (letter.upper() == "B" and p == 1 and duplicate == 0):
        p = 0
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 2                        #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Dragonsbane," on position 2, and the orc is DEAD
    # elif (letter.upper() == "B" and p == 2 and duplicate == 0 and __killed_enemies[0] == True):
    #   p = 1
    #    duplicate += 1

        #####################################################################
        #                                                                   #
        #           USER IS ON POSITION 2.5, AFTER FIGHTING ORC             #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Willowton," on position 2.5, after beating Orc
    elif (letter.upper() == "A" and p == 2.5 and duplicate == 0 and __killed_enemies[0] == True):
        p = 3
        duplicate += 1

    # User selects "Go toward Dragonsbane," on position 2.5, after beating Orc
    elif (letter.upper() == "B" and p == 2.5 and duplicate == 0 and __killed_enemies[0] == True):
        p = 1
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 3                        #
        #                                                                   #
        #####################################################################

    # User selects "Go down path," on position 3
    elif (letter.upper() == "C" and p == 3 and duplicate == 0):
        p = 3.1
        duplicate += 1

    # User selects "Go toward Dragonsbane," on position 3, and the orc is DEAD
    elif (letter.upper() == "B" and p == 3 and duplicate == 0 and __killed_enemies[0] == True):
        p = 2
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                  USER IS ON FIRST SIDE PATH                       #
        #                                                                   #
        #####################################################################

    # User selects "Continue down path," on position 3.1
    elif (letter.upper() == "A" and p == 3.1 and duplicate == 0):
        p = 3.2
        duplicate += 1

    # User selects "Go back to road!," on position 3.1
    elif (letter.upper() == "B" and p == 3.1 and duplicate == 0):
        p = 3
        duplicate += 1

    # User selects "Open chest," on position 3.2
    elif (letter.upper() == "A" and p == 3.2 and duplicate == 0 and check_key == False):
        p = 3.3
        duplicate += 1

    # User selects "Open chest," on position 3.2 and have a key!
    elif (letter.upper() == "A" and p == 3.2 and duplicate == 0 and check_key == True):
        p = 3.4
        duplicate += 1

    # User selects "Walk back to path," on position 3.3
    elif (letter.upper() == "B" and p == 3.3 and duplicate == 0):
        p = 3.2
        duplicate += 1

    # User selects "Collect contents," on position 3.4(the chest)
    elif (letter.upper() == "B" and p == 3.4 and duplicate == 0):
        p = 3.5
        duplicate += 1

    # User selects "Walk back to path," on position 3.3
    elif (letter.upper() == "A" and p == 3.4 and duplicate == 0):
        p = 3.2
        duplicate += 1

    # User selects "Walk back to path," on position 3.3
    elif (letter.upper() == "A" and p == 3.4 and duplicate == 0):
        p = 3.2
        duplicate += 1

    # User selects "Walk back to path," on position 3.2
    elif (letter.upper() == "B" and p == 3.2 and duplicate == 0):
        p = 3.1
        duplicate += 1

    # User selects "Walk back to path," on position 3.3
    elif (letter.upper() == "A" and p == 3.1 and duplicate == 0):
        p = 3
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 5                        #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Willowton," on position 5, putting them in a battle
    elif (letter.upper() == "A" and p == 5 and duplicate == 0 and __killed_enemies[1] == False):
        p = 6.5
        duplicate += 1

    # User selects "Go toward Willowton," on position 5, putting them in a battle
    elif (letter.upper() == "A" and p == 5 and duplicate == 0 and __killed_enemies[1] == True):
        p = 6
        duplicate += 1

    # User selects "Go toward Dragonsbane," on position 5, putting them in a battle
    elif (letter.upper() == "B" and p == 5 and duplicate == 0):
        p = 4
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 6                        #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Dragonabane," on position 6, putting them in a battle
    elif (letter.upper() == "B" and p == 6 and duplicate == 0 and __killed_enemies[1] == True):
        p = 5
        duplicate += 1

    # User selects "Go toward Dragonabane," on position 6, putting them in a battle
    elif (letter.upper() == "B" and p == 6 and duplicate == 0 and __killed_enemies[1] == True):
        p = 5
        duplicate += 1

        #####################################################################
        #                                                                   #
        #           USER IS ON POSITION 6.5, AFTER FIGHTING GOBLIN          #
        #                                                                   #
        #####################################################################

    # User selects "Go toward Willowton," on position 6.5, after the battle.
    elif (letter.upper() == "A" and p == 6.5 and duplicate == 0 and __killed_enemies[1] == True):
        p = 7
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                      USER IS ON POSITION 7                        #
        #                                                                   #
        #####################################################################

    # User selects "Explore path," on road segment 7
    elif (letter.upper() == "C" and p == 7 and duplicate == 0):
        p = 7.1
        duplicate += 1

    # User selects "Continue toward Willowton," on road segment 7
    elif (letter.upper() == "A" and p == 7 and duplicate == 0):
        p = 8
        duplicate += 1

    # User selects "Go toward Dragonsbane," on position 5, putting them in a battle
    elif (letter.upper() == "B" and p == 7 and duplicate == 0 and __killed_enemies[1] == True):
        p = 6
        duplicate += 1

        #####################################################################
        #                                                                   #
        #                  USER IS ON SECOND SIDE PATH                      #
        #                                                                   #
        #####################################################################

    # User select "go back to road" on road segment 7.1
    elif (letter.upper() == "B" and p == 7.1 and duplicate == 0):
        p = 7
        duplicate += 1

    # User select "keep going down path" on road segment 7.1
    elif (letter.upper() == "A" and p == 7.1 and duplicate == 0):
        p = 7.2
        duplicate += 1

    # User selects "go back toward road," on road segment 7.2
    elif (letter.upper() == "B" and p == 7.2 and duplicate == 0):
        p = 7.1
        duplicate += 1

    # User selects "go back toward road," on road segment 7.2
    elif (letter.upper() == "B" and p == 7.2 and duplicate == 0):
        p = 7.1
        duplicate += 1

    # User selects "Open chest," on road segment 7.2
    elif (letter.upper() == "A" and p == 7.2 and duplicate == 0 and check_key == False):
        p = 7.3
        duplicate += 1

    # User selects "Go back toward road," on road segment 7.3
    elif (letter.upper() == "A" and p == 7.3 and duplicate == 0):
        p = 7.1
        duplicate += 1

    # User selects "Open Chest," on road segment 7.3, when they already have a key
    elif (letter.upper() == "A" and p == 7.2 and duplicate == 0 and check_key == True):
        p = 7.5
        duplicate += 1

    # User selects "Collect all items," on road segment 7.3
    elif (letter.upper() == "C" and p == 7.3 and duplicate == 0):
        p = 7.4
        duplicate += 1

    else:
        print("                        Broken, needs debugging!")
    return (p)


def printstatements(p, enemy, Class, strength, magic, key_check, killed_enemies, gold, hp, max_hp, xp):
    road_file = ("road1.2.txt")
    road = open(road_file, 'r').read()
    road_file2 = ("road3.2.txt")
    road3 = open(road_file2, 'r').read()
    road_file3 = ("road7.txt")
    road7 = open(road_file3, 'r').read()
    path_file = ("path.txt")
    path = open(path_file, 'r').read()
    chest_closed_file = ("chest_closed.txt")
    chest_closed = open(chest_closed_file, 'r').read()
    chest_locked_file = ("chest_locked.txt")
    chest_locked = open(chest_locked_file, 'r').read()
    chest_open_file = ("chest_open.txt")
    chest_opened = open(chest_open_file, 'r').read()
    key_file = ("key.txt")
    key = open(key_file, 'r').read()

    willowton_file = ("willowton.txt")
    willowton = open(willowton_file, 'r').read()
    tavern_file = ("tavern.txt")
    tavern = open(tavern_file, 'r').read()
    bed_file = ("bed.txt")
    bed = open(bed_file, 'r').read()
    new_sword_file = ("new_sword.txt")
    new_sword = open(new_sword_file, 'r').read()
    bartender_closed_file = ("bartender_closed.txt")
    bartender_closed = open(bartender_closed_file, 'r').read()
    bartender_open_file = ("bartender_open.txt")
    bartender_open = open(bartender_open_file, 'r').read()
    bartender_smile_file = ("bartender_smile.txt")
    bartender_smile = open(bartender_smile_file, 'r').read()

    mug_in_air = open("mug_in_air.txt", 'r').read()
    bafoon_dancing1 = open("bafoon_dancing1.txt", 'r').read()
    bafoon_dancing2 = open("bafoon_dancing2.txt", 'r').read()
    bafoon_mug_in_face = open("bafoon_mug_in_face.txt", 'r').read()

    z_1 = open("z_1.txt", 'r').read()
    z_2 = open("z_2.txt", 'r').read()
    z_3 = open("z_3.txt", 'r').read()
    z_4 = open("z_4.txt", 'r').read()
    z_5 = open("z_5.txt", 'r').read()

    while (p != 200):
        #####################################################################
        #                                                                   #
        #                      USER IS IN DRAGONSBANE                       #
        #                                                                   #
        #####################################################################

        # USER IS IN DRAGONSBANE
        if (p == 0):
            space(50)
            dragonsbane = open("Dragonsbane.txt", 'r').read()
            print(dragonsbane)
            print(" \n               Welcome to Dragonsbane, what do you want to do?\n\n")
            print(
                "    A|Leave town.  B|Go to shop.  C|Visit tavern.  D|History of Dragonsbane. \n")
            enemy = ("orc")
            p = position(p, key_check, killed_enemies, gold)
            print(key)

        #####################################################################
        #                                                                   #
        #         USER IS IN THE SILVER PLATTER STORE IN DRAGONSBANE        #
        #                                                                   #
        #####################################################################

        elif (p == -1):
            space(50)
            shop_dragonsbane = open("shop_dragonsbane.txt", 'r').read()
            print(shop_dragonsbane)
            print('"Hi, welcome to the legendary Silver Platter general store! How can I help you?"\n GOLD ',
                  gold, '                                                             HP ', hp, "/", max_hp)
            print("              A|Buy items. B|Talk to Owner. C|Leave the store.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.1):
            space(50)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            print(dragonsbane_shop_buy)
            space(1)
            print('"Intersted in buying something, eh? Let me know if you like anthing you see!"\n\n GOLD ',
                  gold, '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.2):
            space(50)
            dragonsbane_shop_closed = open("shop_owner_open.txt", 'r').read()
            dragonsbane_shop_open = open("shop_owner_open2.txt", 'r').read()
            print(dragonsbane_shop_closed)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_open)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_closed)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_open)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_closed)
            print('"I just ran out of empty bottles!! If you could grab me some at Willowton\n                     I would give you 20 gold for it!"\n')
            print("                     A|Accept quest. B|Go on your way.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.21):
            space(50)
            dragonsbane_shop_closed = open("shop_owner_open.txt", 'r').read()
            dragonsbane_shop_open = open("shop_owner_open2.txt", 'r').read()
            print(dragonsbane_shop_closed)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_open)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_closed)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_open)
            space(3)
            sleep(.3)
            space(25)
            print(dragonsbane_shop_closed)
            space(3)
            print(
                '       "Oh thank you! Thank you! You are the best. I\'ll be waiting on you!"')
            sleep(4)
            p = -1

        elif (p == -1.11):
            # USER BUYS AN APPLE!
            gold -= 5
            space(50)
            hp = healing(8, max_hp, hp)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            print(dragonsbane_shop_buy)
            space(1)
            print('     "An apple? Tasty and it\'ll help your HP! Anything else that you\'d like?"\n\n GOLD ',
                  gold, '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.12):
            # USER BUYS A MEDALLION!
            gold -= 60
            space(50)
            xp = (xp * 2)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            print(dragonsbane_shop_buy)
            space(1)
            print('            "A medallion it is! This\'ll double your XP!"\n\n GOLD ', gold,
                  '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.13):
            # USER BUYS A POTION!
            gold -= 15
            space(50)
            hp = healing(max_hp, max_hp, hp)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            space(1)
            print(dragonsbane_shop_buy)
            print(' "A potion, eh? You do look sickly ... Anything else that you\'re interested in?"\n\n GOLD ',
                  gold, '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -1.14):
            # USER BUYS A EMPTY BOTTLE!
            #gold -= 10
            space(50)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            print(dragonsbane_shop_buy)
            space(1)
            print('  "Oooh, an empty bottle, eh? Sorry, I just sold my last one to an old man."\n\n GOLD ',
                  gold, '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

            # USER IS TOO POOR!!
        elif (p == -1.15):
            space(50)
            dragonsbane_shop_buy = open("dragonsbane_shop_buy.txt", 'r').read()
            print(dragonsbane_shop_buy)
            space(1)
            print('                 "Sorry, you don\'t have enough money to do that."\n\n GOLD ', gold,
                  '                                                             HP ', hp, "/", max_hp)
            print(
                "A|Apple. B|Medallion. C|HP Potion. D|Empty Bottle E|Step back from counter.")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #            USER IS IN THE GREASY SPOON, IN DRAGONSBANE            #
        #                                                                   #
        #####################################################################

        # USER SELECTS TO GO TO THE GREASY TAVERN, IN DRAGONSBANE
        elif (p == -.2):
            space(50)
            print(tavern)
            space(2)
            print("                       Welcome to the Greasy Spoon Tavern!\n")
            print("           A|Talk to the bartender. B|Start bar fight. C|Leave Tavern")
            p = position(p, key_check, killed_enemies, gold)

        # USERS DECIDES TO START A BAR FIGHT, IN THE GREASY TAVERN, IN DRAGONSBANE
        elif (p == -.21):
            space(50)
            print(
                "      You notice a bafoon near the bar dancing. You throw a mug at him.\n")
            sleep(2.5)
            space(50)
            print(bafoon_dancing1)
            sleep(.3)
            space(50)
            print(bafoon_dancing2)
            sleep(.3)
            space(50)
            print(bafoon_dancing1)
            sleep(.3)
            space(50)
            print(bafoon_dancing2)
            sleep(.3)
            space(50)
            print(mug_in_air)
            sleep(1)
            space(50)
            space(50)
            print(bafoon_dancing1)
            sleep(.3)
            space(50)
            print(bafoon_dancing2)
            sleep(.3)
            space(50)
            print(bafoon_mug_in_face)
            sleep(1)
            enemy = ("bafoon")
            hp_xp = battle(enemy, Class, strength, magic, hp, max_hp, xp)
            hp = hp_xp[0]
            xp = hp_xp[1]
            p = -.2

        # USER CHOOSES TO TALK TO BARTENDER ABOUT GOSSIP IN THE TAVERN IN DRAGONSBANE
        elif (p == -.233):
            space(50)
            print(bartender_closed)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_open)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_closed)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_open)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_closed)
            print(' "There was a rugged traveler in here the other night, telling tall tales \n      about a chest full of treasure on the way to Willowton. Crazy, eh?"\n')
            sleep(6)
            p = -.23

        # USER CHOOSES TO SLEEP IN BED, IN THE GREASY SPOON, IN DRAGONSBANE
        elif (p == -.25):
            space(50)
            print(bed)
            print("                      How long do you want to sleep for?\n")
            print("                 A|One hour. B|One day. C|Return to Tavern")
            p = position(p, key_check, killed_enemies, gold)

        # USER TALKS TO BARTENDER IN THE GREASY SPOON, IN DRAGONSBANE
        elif (p == -.23):
            space(50)
            print(bartender_closed)

            print(
                '\n        "Welcome to the Greasy Spoon, what do you want to talk about?"\n')
            print(
                ' A|Enquire about lodging. B|Buy drink. C|What\'s new? D|Step back from bar.')
            p = position(p, key_check, killed_enemies, gold)

        # USER BUYS A DRINK IN THE GREASY SPOON, IN DRAGONSBANE
        elif (p == -.232):
            greasy_spoon_mug = open("greasy_spoon_mug.txt", 'r').read()
            hp = healing(8, max_hp, hp)
            space(25)
            print(greasy_spoon_mug)
            space(5)
            print(
                "              You gulp down a bold brew. Your health is now ", hp, "!")
            sleep(4)
            space(25)
            p = -.23

        # USER ENQUIRES ABOUT LODGING, WHILE TALKING TO THE BARTENDER, IN THE GREASY SPOON, IN DRAGONSBANE
        elif (p == -.231):
            space(50)
            print(bartender_closed)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_open)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_closed)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_open)
            space(3)
            sleep(.3)
            space(50)
            print(bartender_closed)
            space(3)

            print(
                "\n    We don't have much, but for 5 gold, I've got an extra bed you could use.\n")
            print("          A|I'll take it! B|No thanks. C|Step back from bar.")
            p = position(p, key_check, killed_enemies, gold)

        # USER DECIDES TO TAKE A NAP, IN THE BEDROOM, IN THE GREASY SPOON, IN DRAGONSBANE
        elif (p == -.253):
            #print("              YOUR HP STARTS OUT AS", hp)
            sleep(2)
            hp = healing(10, max_hp, hp)
            #print("         THE HP NOW IS", hp )
            # sleep(2)
            space(25)
            print(z_1)
            sleep(.5)
            space(25)
            print(z_2)
            sleep(.5)
            space(25)
            print(z_3)
            sleep(.5)
            space(25)
            print(z_4)
            sleep(.5)
            space(25)
            print(z_5)
            sleep(.5)
            space(25)
            print(z_1)
            sleep(.5)
            space(25)
            print(z_2)
            sleep(.5)
            space(25)
            print(z_3)
            sleep(.5)
            space(25)
            print(z_4)
            sleep(.5)
            space(25)
            print(z_5)
            sleep(.5)
            space(25)
            print(bed)
            print(
                "          You awake feeling rested and healed! What do you want to do now?\n")
            print(
                "        A|Sleep for another hour B|Sleep for another day C|Return to Tavern")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #      USER TALKS TO OLD MAN ABOUT THE HISTORY OF DRAGONSBANE       #
        #                                                                   #
        #####################################################################

        elif (p == -.4):
            old_man_open = open("old_man_open.txt", 'r').read()
            old_man_closed = open("old_man_closed.txt", 'r').read()
            space(50)
            print(old_man_closed)
            space(1)
            print("               You approach an old man, sitting alone by the tavern")
            print(
                'A|Ask about Dragonsbane B|Anything new in Dragonsbane? C|Return to main square')
            p = position(p, key_check, killed_enemies, gold)

        elif (p == -.41):
            old_man_open = open("old_man_open.txt", 'r').read()
            old_man_closed = open("old_man_closed.txt", 'r').read()
            space(25)
            space(50)
            print(old_man_closed)
            space(2)
            print("                    The old man goes into a long monologue")
            sleep(.3)
            space(50)
            print(old_man_open)
            space(2)
            print("                    The old man goes into a long monologue")
            sleep(.3)
            space(50)
            print(old_man_closed)
            space(2)
            print("                    The old man goes into a long monologue")
            sleep(.3)
            space(50)
            print(old_man_open)
            space(2)
            print("                    The old man goes into a long monologue")
            sleep(.3)
            space(50)
            print(old_man_closed)
            space(2)
            print("                    The old man goes into a long monologue")
            sleep(3)
            space(25)
            print(
                "Dragonsbane is named for the great dragon wars of yesteryear. In that day many\n")
            sleep(3)

            print(
                "warriors gathered here to form a force strong enough to slay the great dragon\n")
            sleep(3)

            print(
                "Monduuren and drive the rest of his family from these lands. It took the men\n")
            sleep(3)

            print(
                "many months to finally rid the land of these beats and many great men fell in\n")
            sleep(3)

            print(
                "the process. But still to this day they are remembered for their actions in\n")
            sleep(3)

            print(
                "defending these great lands and for that reason the town was renamed\n")
            sleep(3)

            print(
                "Dragonsbane. Prior to this the town was known as Beechton, like it\'s mother\n")
            sleep(3)

            print(
                "city Willowton it was named after the many trees surrounding it\'s lush\n")
            sleep(3)

            print(
                "lands. The people of Dragonsbane while simpler and more rugged are no less\n")
            sleep(3)

            print(
                "hard working or brave. In fact many would say that the people of Dragonsbane\n")
            sleep(3)

            print(
                "are the bravest and hardest working in all the land. It is said that when a\n")
            sleep(3)

            print(
                "child of Dragonsbane reaches the age of 14 they are considered and adult and\n")
            sleep(3)

            print(
                "must go out into the world and make their way on their own. Once a child has\n")
            sleep(3)

            print(
                "successfully been hired as an apprentice they have the option to return home to\n")
            sleep(3)

            print(
                "their parents and board with them for 30 centimos a month. The parent may set the\n")
            sleep(3)

            print(
                "amount higher, this is mostly personal preference, but the standard is 30. Often\n")
            sleep(3)

            print(
                "children will instead opt for boarding at one of the many half way houses. This\n")
            sleep(3)

            print(
                "is not considered lowly but rather more honorable. Though if this is done it is\n")
            sleep(3)

            print(
                "expected that the child will also help with the many jobs around the half way\n")
            sleep(3)

            print(
                "house. If the child opts to stay at home for 30 centimos the child may or may\n")
            sleep(3)

            print(
                "not continue household chores, it is again up to the parent. Though it would be\n")
            sleep(3)

            print(
                "considered shameful not to require the child to take charge of butter churning\n")
            sleep(3)

            print(
                "duties. In Dragonsbane butter churning accounts for 73 percent of revenue to the\n")
            sleep(3)

            print(
                "town and therefore it is assumed all children will participate. When a child has\n")
            sleep(3)

            print(
                "taken up the churning duties for their own home or take a rotation shift at a\n")
            sleep(3)

            print(
                "halfway house they are expected to churn out an average of 7 pounds a day. This\n")
            sleep(3)

            print(
                "butter is then distributed through a communal system of sharing and giving. All\n")
            sleep(3)

            print(
                "community members are expected to turn in a number of pounds proportionate to\n")
            sleep(3)

            print(
                "their household size. The halfway houses account for the largest share of butter\n")
            sleep(3)

            print(
                "for the town with an average of 1,120 pounds a week. After it has been\n")
            sleep(3)

            print(
                "redistributed back to the town members they may do with it what they will. Larger\n")
            sleep(3)

            print(
                "households are given larger shares with the largest getting around 300 pounds\n")
            sleep(3)

            print(
                "each. Much of the butter is taken by the town's government and then sold to\n")
            sleep(3)

            print(
                "the neighboring city of Willowton. This deal is usually made by way of a barter\n")
            sleep(3)

            print(
                "system, instead of exchanging goods for centimos the two communities prefer to\n")
            sleep(3)

            print(
                "trade goods. Willowton being the largest provider of goat cheese in all the land\n")
            sleep(3)

            print(
                "are glad to offer their goods in exchange for Dragonsbane. The WIllowtons know\n")
            sleep(3)

            print(
                "nothing of butter or how it's made. There are the few Willowtons who attempt to\n")
            sleep(3)

            print(
                "make their own and while they have found moderate success, and this is mainly due\n")
            sleep(3)

            print(
                "to certain WIllowtons general disdain for all things Dragonsbane and wish to keep\n")
            sleep(3)

            print(
                "all their business inside of Willowton. This is not uncommon, in fact if it were not\n")
            sleep(3)

            print(
                "each communities mutual need for the others goods the two would have little to no\n")
            sleep(3)

            print(
                "interaction. This shared dislike started many years ago when a small sect of\n")
            sleep(3)

            print(
                "Beechton's richest citizens wished for a more exclusive space. They gathered up their\n")
            sleep(3)

            print(
                "things, moved on and started a new city. Shortly after, many other Beechtons (of a\n")
            sleep(3)

            print(
                "lesser economic state) followed suit, and though the Willowtons were not entirely\n")
            sleep(3)

            print(
                "enthused by the idea of middle class Beechtons crowding their city they allowed it\n")
            sleep(3)

            print(
                "for the sake of hurting Beechtons overall economy by the massive exodus to Willowtons\n")
            sleep(3)

            print(
                "much nicer and newer conditions. This is ironic in that though Willowton is much larger\n")
            sleep(3)

            print(
                "and richer it is overrun by many many people of varying economic statuses. Dragonsbane\n")
            sleep(3)

            print(
                "though smaller has carved out quite a niche for itself being the biggest supplier of\n")
            sleep(3)

            print(
                "butter in the realm. Maybe someday they will find peace with Willowton and unite under\n")
            sleep(3)

            print(
                "a banner of friendship. Until then the safety of both communities will be under extreme\n")
            sleep(3)

            print("duress.")
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            space(1)
            sleep(1)
            p = -.4

        elif (p == -.42):
            space(50)
            print(old_man_closed)
            space(1)
            print(
                " Well, I heard that the shop owner, Cindy Loo-Hoo has run out of empty bottles!")
            sleep(.3)
            space(50)
            print(old_man_open)
            space(1)
            print(
                " Well, I heard that the shop owner, Cindy Loo-Hoo has run out of empty bottles!")
            sleep(.3)
            space(50)
            print(old_man_closed)
            space(1)
            print(
                " Well, I heard that the shop owner, Cindy Loo-Hoo has run out of empty bottles!")
            sleep(.3)
            space(50)
            print(old_man_open)
            space(1)
            print(
                " Well, I heard that the shop owner, Cindy Loo-Hoo has run out of empty bottles!")
            sleep(.3)
            space(50)
            print(old_man_closed)
            space(1)
            print(
                " Well, I heard that the shop owner, Cindy Loo-Hoo has run out of empty bottles!")
            sleep(3)

            p = -.4

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 1!                        #
        #                                                                   #
        #####################################################################

        elif (p == 1):
            if (key == True and killed_enemies[2] == False):
                enemy = ("orc")
                hp_xp = battle(enemy, Class, strength, magic, hp, max_hp, xp)
                hp = hp_xp[0]
                xp = hp_xp[1]
                sleep(5)
                killed_enemies[2] = True
                p = position(p, key_check, killed_enemies, gold)
            else:
                space(50)
                print(road)
                print("                              You are on a road!\n")
                print("                A|Go toward Willowton  B|Enter Dragonsbane\n\n")
                p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 2!                        #
        #                                                                   #
        #####################################################################

        elif (p == 2):
            space(50)
            print(road)
            print("                        There appears be nothing here.\n")
            print(
                "                  A|Go toward Willowton  B|Go toward Dragonsbane   \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                   USER IS ON POSITION 2.5!                        #
        #                                                                   #
        #####################################################################

        elif (p == 2.5):
            enemy = ("orc")
            hp_xp = battle(enemy, Class, strength, magic, hp, max_hp, xp)
            hp = hp_xp[0]
            xp = hp_xp[1]
            sleep(5)
            killed_enemies[0] = True
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                    USER IS ON POSITION 3!                         #
        #                                                                   #
        #####################################################################

        elif (p == 3):
            space(50)
            if (key_check == False):
                print(road3)
            else:
                print(road7)
            print("               You are now on road! A path has just appeared\n")
            print(
                "            A|Go toward Willowton  B|Go toward Dragonsbane  C|Explore path \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                 USER IS ON FIRST SIDE PATH                        #
        #                                                                   #
        #####################################################################

        elif (p == 3.1):
            space(50)
            print(path)
            print("                 You are in a dark clearing. You see a chest. \n")
            print("                 A|Step up to chest  B|Return to main road \n\n")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == 3.2):
            space(50)
            print(chest_closed)
            print("                     \n")
            print("                     A|Open chest B|Step back from chest \n\n")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == 3.3):
            space(50)
            print(chest_locked)
            space(4)
            print("                        The chest appears to be locked! \n")
            print("                 \n\n")
            sleep(2)
            p = 3.2

        elif (p == 3.4):
            space(50)
            print(chest_opened)
            print("                          The chest is open! \n")
            print("  \n\n")
            sleep(3)
            p = 3.5

        elif (p == 3.5):
            space(50)
            if (Class == 1):
                print(new_sword)
                space(1)
                print("                       You have found an iron sword! \n\n")
            else:
                wand = open("wand.txt", 'r').read()
                print(wand)
                space(1)
                print("                   You have found a New Willow Wand!")
            xp = (xp * 3)
            sleep(3)
            p = 3.2

        #####################################################################
        #                                                                   #
        #                    USER IS ON POSITION 4!                         #
        #                                                                   #
        #####################################################################

        elif (p == 4):
            space(50)
            print(road)
            print("                      There appears be nothing here.\n")
            print(
                "                  A|Go toward Willowton  B|Go toward Dragonsbane   \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 5!                        #
        #                                                                   #
        #####################################################################

        elif (p == 5):
            space(50)
            print(road)
            print("                        There appears be nothing here.\n")
            print(
                "                  A|Go toward Willowton  B|Go toward Dragonsbane   \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 6!                        #
        #                                                                   #
        #####################################################################

        elif (p == 6):
            space(50)
            print(road)
            print("                        There appears be nothing here.\n")
            print(
                "                  A|Go toward Willowton  B|Go toward Dragonsbane   \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                USER FIGHTS WITH ANDUBWIN GOBLIN                   #
        #                                                                   #
        #####################################################################

        elif (p == 6.5):
            enemy = ("Andubwin Goblin")
            hp_xp = battle(enemy, Class, strength, magic, hp, max_hp, xp)
            hp = hp_xp[0]
            xp = hp_xp[1]
            killed_enemies[1] = True
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 7!                        #
        #                                                                   #
        #####################################################################

        elif (p == 7):
            space(50)
            if (key_check == False):
                print(road7)
            else:
                print(road3)
            print(
                "               You are now on a road. A dark path has just appeared.\n")
            print(
                "         A|Go toward Willowton B|Go toward Dragonsbane C|Explore path\n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                  USER IS ON SECOND SIDE PATH!                     #
        #                                                                   #
        #####################################################################

        elif (p == 7.1):
            space(50)
            print(path)
            print("                 You are in a dark clearing. You see a chest. \n")
            print("                 A|Step up to chest  B|Return to main road \n\n")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == 7.2):
            space(50)
            print(chest_closed)
            print("                     \n")
            print("                     A|Open chest B|Step back from chest \n\n")
            p = position(p, key_check, killed_enemies, gold)

        elif (p == 7.3):
            space(50)
            print(chest_opened)
            print("                                The chest is open! \n")
            print("   \n\n")
            sleep(2)
            p = 7.4

        elif (p == 7.4):
            space(50)
            print(key)
            space(5)
            print("                            You've got a key! \n\n")
            key_check = True
            sleep(3)
            p = 7.2

        elif (p == 7.5):
            chest_open_empty = open("chest_open_empty.txt", 'r').read()
            space(50)
            print(chest_open_empty)
            print("                                The chest is empty! \n")
            print("   \n\n")
            sleep(3)
            p = 7.2

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 8!                        #
        #                                                                   #
        #####################################################################

        elif (p == 8):
            space(50)
            print(road)
            print("                         There appears be nothing here.\n")
            print(
                "      A|Go toward Willowton  B|Go toward Dragonsbane.  C|View inventory \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 9!                        #
        #                                                                   #
        #####################################################################

        elif (p == 9):
            space(50)
            print(road)
            print("                          There appears be nothing here.\n")
            print(
                "      A|Go toward Willowton  B|Go toward Dragonsbane.  C|View inventory \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS ON POSITION 10!                       #
        #                                                                   #
        #####################################################################

        elif (p == 10):
            space(50)
            print(road)
            print("                   Willowton appears to be just a league away.\n")
            print(
                "       A|Enter Willowton.  B|Go toward Dragonsbane.  C|View inventory \n\n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER IS IN WILLOWTON!                         #
        #                                                                   #
        #####################################################################

        elif (p == 11):

            space(50)
            print(willowton)
            print(" \n               Welcome to Willowton, what do you want to do?\n")
            print(
                "  A|Leave town.  B|Go to shop.  C|Sleep at the inn.  D|History of Willowton \n")
            p = position(p, key_check, killed_enemies, gold)

        #####################################################################
        #                                                                   #
        #                     USER WANT TO BE SORTED!                       #
        #                                                                   #
        #####################################################################

        elif (p == -.5):
            #road_file = ("sortinghat2.py")
            #road = open(road_file, 'r').read()
            # open(road)
            os.startfile("sortinghat2.py")
            p = 0

        #####################################################################
        #                                                                   #
        #           USER IS SENT TO A LOCATION THAT DOES NOT EXIST          #
        #                                                                   #
        #####################################################################

        else:
            space(50)
            print("                            NEEDS DEBUGGING \n                         The current position is", p)
            sleep(55555)


def firstsighting(enemy_name, blink):
    n = 0
    if (enemy_name == 1):
        enemy_name = "Orc"
    if (enemy_name.upper() == "ORC"):
        while (n < blink):
            space(100)
            sleep(.3)
            print("                   ######################################## \n                   #                                      # \n                   #      YOU JUST ENCOUNTERED AN " +
                  enemy_name.upper() + "!    # \n                   #                                      # \n                   ######################################## \n\n\n\n\n\n\n")
            n += 1
            sleep(.3)
    elif (enemy_name.upper() == "ANDUBWIN GOBLIN"):
        while (n < blink):
            space(100)
            sleep(.3)
            print("              ############################################# \n              #                                           # \n              # YOU JUST ENCOUNTERED AN " +
                  enemy_name.upper() + "!  # \n              #                                           # \n              ############################################# \n\n\n\n\n\n\n")
            n += 1
            sleep(.3)
    elif (enemy_name.upper() == "BAFOON"):
        while (n < blink):
            space(100)
            sleep(.3)
            print("              ############################################# \n              #                                           # \n              #     YOU JUST ENCOUNTERED AN " +
                  enemy_name.upper() + "! # \n              #                                           # \n              ############################################# \n\n\n\n\n\n\n")
            n += 1
            sleep(.3)


def enemy_animation(enemy, times):
    enemy_file = ("herov" + enemy + ".txt")
    enemy_pic = open(enemy_file, 'r').read()
    enemy_file2 = ("herov" + enemy + "2.txt")
    enemy_pic2 = open(enemy_file2, 'r').read()
    enemy_file3 = ("herov" + enemy + "3.txt")
    enemy_pic3 = open(enemy_file3, 'r').read()
    enemy_file4 = ("herov" + enemy + "4.txt")
    enemy_pic4 = open(enemy_file4, 'r').read()

    counter = 0
    if (enemy.upper() == "ORC" or enemy.upper() == "ANDUBWIN GOBLIN"):
        enemy_file5 = ("herov" + enemy + "5.txt")
        enemy_pic5 = open(enemy_file5, 'r').read()
        while (counter < times):
            space(50)
            print(enemy_pic)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic2)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic3)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic4)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic5)
            space(1)
            sleep(.1)
            counter += 1
    elif (enemy.upper() == "BAFOON"):
        while (counter < times):
            space(25)
            print(enemy_pic)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic2)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic3)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic4)
            space(1)
            sleep(.1)
            counter += 1


def hero_animation(Class, enemy, times):
    enemy_file = (enemy + "vhero.txt")
    enemy_pic = open(enemy_file, 'r').read()
    enemy_file2 = (enemy + "vhero2.txt")
    enemy_pic2 = open(enemy_file2, 'r').read()
    enemy_file3 = (enemy + "vhero3.txt")
    enemy_pic3 = open(enemy_file3, 'r').read()
    counter = 0
    if (enemy.upper() == "ORC" and Class == 1):
        while (counter < times):
            space(50)
            print(enemy_pic)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic2)
            space(1)
            sleep(.1)
            space(50)
            print(enemy_pic3)
            space(1)
            sleep(.1)
            counter += 1
    elif (enemy.upper() == "BAFOON" and Class == 1):
        enemy_file4 = (enemy + "vhero4.txt")
        enemy_pic4 = open(enemy_file4, 'r').read()
        while (counter < times):
            space(25)
            print(enemy_pic)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic2)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic3)
            space(1)
            sleep(.1)
            space(25)
            print(enemy_pic4)
            space(1)
            sleep(.1)
            counter += 1
    elif (Class == 2):
        mage_1 = open("2herovorc.txt", 'r').read()
        mage_2 = open("2herovorc2.txt", 'r').read()
        mage_3 = open("2herovorc3.txt", 'r').read()
        mage_4 = open("2herovorc4.txt", 'r').read()
        mage_5 = open("2herovorc5.txt", 'r').read()
        mage_6 = open("2herovorc6.txt", 'r').read()
        mage_7 = open("2herovorc7.txt", 'r').read()
        mage_8 = open("2herovorc8.txt", 'r').read()
        mage_9 = open("2herovorc9.txt", 'r').read()
        mage_10 = open("2herovorc10.txt", 'r').read()
        mage_11 = open("2herovorc11.txt", 'r').read()
        mage_12 = open("2herovorc12.txt", 'r').read()
        mage_13 = open("2herovorc13.txt", 'r').read()
        mage_14 = open("2herovorc14.txt", 'r').read()
        mage_15 = open("2herovorc15.txt", 'r').read()
        mage_16 = open("2herovorc16.txt", 'r').read()
        mage_17 = open("2herovorc17.txt", 'r').read()
        mage_18 = open("2herovorc18.txt", 'r').read()
        mage_19 = open("2herovorc19.txt", 'r').read()
        mage_20 = open("2herovorc20.txt", 'r').read()
        mage_21 = open("2herovorc21.txt", 'r').read()

        while (counter < times):
            space(25)
            print(mage_1)
            space(1)
            sleep(.1)
            space(25)
            print(mage_2)
            space(1)
            sleep(.1)
            space(25)
            print(mage_3)
            space(1)
            sleep(.1)
            space(25)
            print(mage_4)
            space(1)
            sleep(.1)
            space(25)
            print(mage_5)
            space(1)
            sleep(.1)
            space(25)
            print(mage_6)
            space(1)
            sleep(.1)
            space(25)
            print(mage_7)
            space(1)
            sleep(.1)
            space(25)
            print(mage_8)
            space(1)
            sleep(.1)
            space(25)
            print(mage_8)
            space(1)
            sleep(.1)
            space(25)
            print(mage_9)
            space(1)
            sleep(.1)
            space(25)
            print(mage_10)
            space(1)
            sleep(.1)
            space(25)
            print(mage_11)
            space(1)
            sleep(.1)
            space(25)
            print(mage_12)
            space(1)
            sleep(.1)
            space(25)
            print(mage_13)
            space(1)
            sleep(.1)
            space(25)
            print(mage_14)
            space(1)
            sleep(.1)
            space(25)
            print(mage_15)
            space(1)
            sleep(.1)
            space(25)
            print(mage_16)
            space(1)
            sleep(.1)
            space(25)
            print(mage_17)
            space(1)
            sleep(.1)
            space(25)
            print(mage_18)
            space(1)
            sleep(.1)
            space(25)
            print(mage_19)
            space(1)
            sleep(.1)
            space(25)
            print(mage_20)
            space(1)
            sleep(.1)
            space(25)
            print(mage_21)
            space(1)
            sleep(.1)
            counter += 1


def health(hero, enemy):

    h10_e10 = open("hero_10_enemy_10.txt", 'r').read()
    h10_e9 = open("hero_10_enemy_9.txt", 'r').read()
    h10_e8 = open("hero_10_enemy_8.txt", 'r').read()
    h10_e7 = open("hero_10_enemy_7.txt", 'r').read()
    h10_e6 = open("hero_10_enemy_6.txt", 'r').read()
    h10_e5 = open("hero_10_enemy_5.txt", 'r').read()
    h10_e4 = open("hero_10_enemy_4.txt", 'r').read()
    h10_e3 = open("hero_10_enemy_3.txt", 'r').read()
    h10_e2 = open("hero_10_enemy_2.txt", 'r').read()
    h10_e1 = open("hero_10_enemy_1.txt", 'r').read()
    h10_e0 = open("hero_10_enemy_0.txt", 'r').read()
    h9_e10 = open("hero_9_enemy_10.txt", 'r').read()
    h9_e9 = open("hero_9_enemy_9.txt", 'r').read()
    h9_e8 = open("hero_9_enemy_8.txt", 'r').read()
    h9_e7 = open("hero_9_enemy_7.txt", 'r').read()
    h9_e6 = open("hero_9_enemy_6.txt", 'r').read()
    h9_e5 = open("hero_9_enemy_5.txt", 'r').read()
    h9_e4 = open("hero_9_enemy_4.txt", 'r').read()
    h9_e3 = open("hero_9_enemy_3.txt", 'r').read()
    h9_e2 = open("hero_9_enemy_2.txt", 'r').read()
    h9_e1 = open("hero_9_enemy_1.txt", 'r').read()
    h9_e0 = open("hero_9_enemy_0.txt", 'r').read()
    h8_e10 = open("hero_8_enemy_10.txt", 'r').read()
    h8_e9 = open("hero_8_enemy_9.txt", 'r').read()
    h8_e8 = open("hero_8_enemy_8.txt", 'r').read()
    h8_e7 = open("hero_8_enemy_7.txt", 'r').read()
    h8_e6 = open("hero_8_enemy_6.txt", 'r').read()
    h8_e5 = open("hero_8_enemy_5.txt", 'r').read()
    h8_e4 = open("hero_8_enemy_4.txt", 'r').read()
    h8_e3 = open("hero_8_enemy_3.txt", 'r').read()
    h8_e2 = open("hero_8_enemy_2.txt", 'r').read()
    h8_e1 = open("hero_8_enemy_1.txt", 'r').read()
    h8_e0 = open("hero_8_enemy_0.txt", 'r').read()
    h7_e10 = open("hero_7_enemy_10.txt", 'r').read()
    h7_e9 = open("hero_7_enemy_9.txt", 'r').read()
    h7_e8 = open("hero_7_enemy_8.txt", 'r').read()
    h7_e7 = open("hero_7_enemy_7.txt", 'r').read()
    h7_e6 = open("hero_7_enemy_6.txt", 'r').read()
    h7_e5 = open("hero_7_enemy_5.txt", 'r').read()
    h7_e4 = open("hero_7_enemy_4.txt", 'r').read()
    h7_e3 = open("hero_7_enemy_3.txt", 'r').read()
    h7_e2 = open("hero_7_enemy_2.txt", 'r').read()
    h7_e1 = open("hero_7_enemy_1.txt", 'r').read()
    h7_e0 = open("hero_7_enemy_0.txt", 'r').read()
    h6_e10 = open("hero_6_enemy_10.txt", 'r').read()
    h6_e9 = open("hero_6_enemy_9.txt", 'r').read()
    h6_e8 = open("hero_6_enemy_8.txt", 'r').read()
    h6_e7 = open("hero_6_enemy_7.txt", 'r').read()
    h6_e6 = open("hero_6_enemy_6.txt", 'r').read()
    h6_e5 = open("hero_6_enemy_5.txt", 'r').read()
    h6_e4 = open("hero_6_enemy_4.txt", 'r').read()
    h6_e3 = open("hero_6_enemy_3.txt", 'r').read()
    h6_e2 = open("hero_6_enemy_2.txt", 'r').read()
    h6_e1 = open("hero_6_enemy_1.txt", 'r').read()
    h6_e0 = open("hero_6_enemy_0.txt", 'r').read()
    h5_e10 = open("hero_5_enemy_10.txt", 'r').read()
    h5_e9 = open("hero_5_enemy_9.txt", 'r').read()
    h5_e8 = open("hero_5_enemy_8.txt", 'r').read()
    h5_e7 = open("hero_5_enemy_7.txt", 'r').read()
    h5_e6 = open("hero_5_enemy_6.txt", 'r').read()
    h5_e5 = open("hero_5_enemy_5.txt", 'r').read()
    h5_e4 = open("hero_5_enemy_4.txt", 'r').read()
    h5_e3 = open("hero_5_enemy_3.txt", 'r').read()
    h5_e2 = open("hero_5_enemy_2.txt", 'r').read()
    h5_e1 = open("hero_5_enemy_1.txt", 'r').read()
    h5_e0 = open("hero_5_enemy_0.txt", 'r').read()
    h4_e10 = open("hero_4_enemy_10.txt", 'r').read()
    h4_e9 = open("hero_4_enemy_9.txt", 'r').read()
    h4_e8 = open("hero_4_enemy_8.txt", 'r').read()
    h4_e7 = open("hero_4_enemy_7.txt", 'r').read()
    h4_e6 = open("hero_4_enemy_6.txt", 'r').read()
    h4_e5 = open("hero_4_enemy_5.txt", 'r').read()
    h4_e4 = open("hero_4_enemy_4.txt", 'r').read()
    h4_e3 = open("hero_4_enemy_3.txt", 'r').read()
    h4_e2 = open("hero_4_enemy_2.txt", 'r').read()
    h4_e1 = open("hero_4_enemy_1.txt", 'r').read()
    h4_e0 = open("hero_4_enemy_0.txt", 'r').read()
    h3_e10 = open("hero_3_enemy_10.txt", 'r').read()
    h3_e9 = open("hero_3_enemy_9.txt", 'r').read()
    h3_e8 = open("hero_3_enemy_8.txt", 'r').read()
    h3_e7 = open("hero_3_enemy_7.txt", 'r').read()
    h3_e6 = open("hero_3_enemy_6.txt", 'r').read()
    h3_e5 = open("hero_3_enemy_5.txt", 'r').read()
    h3_e4 = open("hero_3_enemy_4.txt", 'r').read()
    h3_e3 = open("hero_3_enemy_3.txt", 'r').read()
    h3_e2 = open("hero_3_enemy_2.txt", 'r').read()
    h3_e1 = open("hero_3_enemy_1.txt", 'r').read()
    h3_e0 = open("hero_3_enemy_0.txt", 'r').read()
    h2_e10 = open("hero_2_enemy_10.txt", 'r').read()
    h2_e9 = open("hero_2_enemy_9.txt", 'r').read()
    h2_e8 = open("hero_2_enemy_8.txt", 'r').read()
    h2_e7 = open("hero_2_enemy_7.txt", 'r').read()
    h2_e6 = open("hero_2_enemy_6.txt", 'r').read()
    h2_e5 = open("hero_2_enemy_5.txt", 'r').read()
    h2_e4 = open("hero_2_enemy_4.txt", 'r').read()
    h2_e3 = open("hero_2_enemy_3.txt", 'r').read()
    h2_e2 = open("hero_2_enemy_2.txt", 'r').read()
    h2_e1 = open("hero_2_enemy_1.txt", 'r').read()
    h2_e0 = open("hero_2_enemy_0.txt", 'r').read()
    h1_e10 = open("hero_1_enemy_10.txt", 'r').read()
    h1_e9 = open("hero_1_enemy_9.txt", 'r').read()
    h1_e8 = open("hero_1_enemy_8.txt", 'r').read()
    h1_e7 = open("hero_1_enemy_7.txt", 'r').read()
    h1_e6 = open("hero_1_enemy_6.txt", 'r').read()
    h1_e5 = open("hero_1_enemy_5.txt", 'r').read()
    h1_e4 = open("hero_1_enemy_4.txt", 'r').read()
    h1_e3 = open("hero_1_enemy_3.txt", 'r').read()
    h1_e2 = open("hero_1_enemy_2.txt", 'r').read()
    h1_e1 = open("hero_1_enemy_1.txt", 'r').read()
    h1_e0 = open("hero_1_enemy_0.txt", 'r').read()
    h0_e0 = open("hero_0_enemy_0.txt", 'r').read()

    if (hero == 100 and enemy == 100):
        print(h10_e10)
    elif (hero == 100 and enemy >= 90 and enemy < 100):
        print(h10_e9)
    elif (hero == 100 and enemy >= 80 and enemy < 90):
        print(h10_e8)
    elif (hero == 100 and enemy >= 70 and enemy < 80):
        print(h10_e7)
    elif (hero == 100 and enemy >= 60 and enemy < 70):
        print(h10_e6)
    elif (hero == 100 and enemy >= 50 and enemy < 60):
        print(h10_e5)
    elif (hero == 100 and enemy >= 40 and enemy < 50):
        print(h10_e4)
    elif (hero == 100 and enemy >= 30 and enemy < 40):
        print(h10_e3)
    elif (hero == 100 and enemy >= 20 and enemy < 30):
        print(h10_e2)
    elif (hero == 100 and enemy >= 10 and enemy < 20):
        print(h10_e1)
    elif (hero == 100 and enemy < 10):
        print(h10_e0)

    elif (hero >= 90 and hero < 100 and enemy == 100):
        print(h9_e10)
    elif (hero >= 90 and hero < 100 and enemy >= 90 and enemy < 100):
        print(h9_e9)
    elif (hero >= 90 and hero < 100 and enemy >= 80 and enemy < 90):
        print(h9_e8)
    elif (hero >= 90 and hero < 100 and enemy >= 70 and enemy < 80):
        print(h9_e7)
    elif (hero >= 90 and hero < 100 and enemy >= 60 and enemy < 70):
        print(h9_e6)
    elif (hero >= 90 and hero < 100 and enemy >= 50 and enemy < 60):
        print(h9_e5)
    elif (hero >= 90 and hero < 100 and enemy >= 40 and enemy < 50):
        print(h9_e4)
    elif (hero >= 90 and hero < 100 and enemy >= 30 and enemy < 40):
        print(h9_e3)
    elif (hero >= 90 and hero < 100 and enemy >= 20 and enemy < 30):
        print(h9_e2)
    elif (hero >= 90 and hero < 100 and enemy >= 10 and enemy < 20):
        print(h9_e1)
    elif (hero >= 90 and hero < 100 and enemy < 10):
        print(h9_e0)

    elif (hero >= 80 and hero < 90 and enemy == 100):
        print(h8_e10)
    elif (hero >= 80 and hero < 90 and enemy >= 90 and enemy < 100):
        print(h8_e9)
    elif (hero >= 80 and hero < 90 and enemy >= 80 and enemy < 90):
        print(h8_e8)
    elif (hero >= 80 and hero < 90 and enemy >= 70 and enemy < 80):
        print(h8_e7)
    elif (hero >= 80 and hero < 90 and enemy >= 60 and enemy < 70):
        print(h8_e6)
    elif (hero >= 80 and hero < 90 and enemy >= 50 and enemy < 60):
        print(h8_e5)
    elif (hero >= 80 and hero < 90 and enemy >= 40 and enemy < 50):
        print(h8_e4)
    elif (hero >= 80 and hero < 90 and enemy >= 30 and enemy < 40):
        print(h8_e3)
    elif (hero >= 80 and hero < 90 and enemy >= 20 and enemy < 30):
        print(h8_e2)
    elif (hero >= 80 and hero < 90 and enemy >= 10 and enemy < 20):
        print(h8_e1)
    elif (hero >= 80 and hero < 90 and enemy < 10):
        print(h8_e0)

    elif (hero >= 70 and hero < 80 and enemy == 100):
        print(h7_e10)
    elif (hero >= 70 and hero < 80 and enemy >= 90 and enemy < 100):
        print(h7_e9)
    elif (hero >= 70 and hero < 80 and enemy >= 80 and enemy < 90):
        print(h7_e8)
    elif (hero >= 70 and hero < 80 and enemy >= 70 and enemy < 80):
        print(h7_e7)
    elif (hero >= 70 and hero < 80 and enemy >= 60 and enemy < 70):
        print(h7_e6)
    elif (hero >= 70 and hero < 80 and enemy >= 50 and enemy < 60):
        print(h7_e5)
    elif (hero >= 70 and hero < 80 and enemy >= 40 and enemy < 50):
        print(h7_e4)
    elif (hero >= 70 and hero < 80 and enemy >= 30 and enemy < 40):
        print(h7_e3)
    elif (hero >= 70 and hero < 80 and enemy >= 20 and enemy < 30):
        print(h7_e2)
    elif (hero >= 70 and hero < 80 and enemy >= 10 and enemy < 20):
        print(h7_e1)
    elif (hero >= 70 and hero < 80 and enemy < 10):
        print(h7_e0)

    elif (hero >= 60 and hero < 70 and enemy == 100):
        print(h6_e10)
    elif (hero >= 60 and hero < 70 and enemy >= 90 and enemy < 100):
        print(h6_e9)
    elif (hero >= 60 and hero < 70 and enemy >= 80 and enemy < 90):
        print(h6_e8)
    elif (hero >= 60 and hero < 70 and enemy >= 70 and enemy < 80):
        print(h6_e7)
    elif (hero >= 60 and hero < 70 and enemy >= 60 and enemy < 70):
        print(h6_e6)
    elif (hero >= 60 and hero < 70 and enemy >= 50 and enemy < 60):
        print(h6_e5)
    elif (hero >= 60 and hero < 70 and enemy >= 40 and enemy < 50):
        print(h6_e4)
    elif (hero >= 60 and hero < 70 and enemy >= 30 and enemy < 40):
        print(h6_e3)
    elif (hero >= 60 and hero < 70 and enemy >= 20 and enemy < 30):
        print(h6_e2)
    elif (hero >= 60 and hero < 70 and enemy >= 10 and enemy < 20):
        print(h6_e1)
    elif (hero >= 60 and hero < 70 and enemy < 10):
        print(h6_e0)

    elif (hero >= 50 and hero < 60 and enemy == 100):
        print(h5_e10)
    elif (hero >= 50 and hero < 60 and enemy >= 90 and enemy < 100):
        print(h5_e9)
    elif (hero >= 50 and hero < 60 and enemy >= 80 and enemy < 90):
        print(h5_e8)
    elif (hero >= 50 and hero < 60 and enemy >= 70 and enemy < 80):
        print(h5_e7)
    elif (hero >= 50 and hero < 60 and enemy >= 60 and enemy < 70):
        print(h5_e6)
    elif (hero >= 50 and hero < 60 and enemy >= 50 and enemy < 60):
        print(h5_e5)
    elif (hero >= 50 and hero < 60 and enemy >= 40 and enemy < 50):
        print(h5_e4)
    elif (hero >= 50 and hero < 60 and enemy >= 30 and enemy < 40):
        print(h5_e3)
    elif (hero >= 50 and hero < 60 and enemy >= 20 and enemy < 30):
        print(h5_e2)
    elif (hero >= 50 and hero < 60 and enemy >= 10 and enemy < 20):
        print(h5_e1)
    elif (hero >= 50 and hero < 60 and enemy < 10):
        print(h5_e0)

    elif (hero >= 40 and hero < 50 and enemy == 100):
        print(h4_e10)
    elif (hero >= 40 and hero < 50 and enemy >= 90 and enemy < 100):
        print(h4_e9)
    elif (hero >= 40 and hero < 50 and enemy >= 80 and enemy < 90):
        print(h4_e8)
    elif (hero >= 40 and hero < 50 and enemy >= 70 and enemy < 80):
        print(h4_e7)
    elif (hero >= 40 and hero < 50 and enemy >= 60 and enemy < 70):
        print(h4_e6)
    elif (hero >= 40 and hero < 50 and enemy >= 50 and enemy < 60):
        print(h4_e5)
    elif (hero >= 40 and hero < 50 and enemy >= 40 and enemy < 50):
        print(h4_e4)
    elif (hero >= 40 and hero < 50 and enemy >= 30 and enemy < 40):
        print(h4_e3)
    elif (hero >= 40 and hero < 50 and enemy >= 20 and enemy < 30):
        print(h4_e2)
    elif (hero >= 40 and hero < 50 and enemy >= 10 and enemy < 20):
        print(h4_e1)
    elif (hero >= 40 and hero < 50 and enemy < 10):
        print(h4_e0)

    elif (hero >= 30 and hero < 40 and enemy == 100):
        print(h3_e10)
    elif (hero >= 30 and hero < 40 and enemy >= 90 and enemy < 100):
        print(h3_e9)
    elif (hero >= 30 and hero < 40 and enemy >= 80 and enemy < 90):
        print(h3_e8)
    elif (hero >= 30 and hero < 40 and enemy >= 70 and enemy < 80):
        print(h3_e7)
    elif (hero >= 30 and hero < 40 and enemy >= 60 and enemy < 70):
        print(h3_e6)
    elif (hero >= 30 and hero < 40 and enemy >= 50 and enemy < 60):
        print(h3_e5)
    elif (hero >= 30 and hero < 40 and enemy >= 40 and enemy < 50):
        print(h3_e4)
    elif (hero >= 30 and hero < 40 and enemy >= 30 and enemy < 40):
        print(h3_e3)
    elif (hero >= 30 and hero < 40 and enemy >= 20 and enemy < 30):
        print(h3_e2)
    elif (hero >= 30 and hero < 40 and enemy >= 10 and enemy < 20):
        print(h3_e1)
    elif (hero >= 30 and hero < 40 and enemy < 10):
        print(h3_e0)

    elif (hero >= 20 and hero < 30 and enemy == 100):
        print(h2_e10)
    elif (hero >= 20 and hero < 30 and enemy >= 90 and enemy < 100):
        print(h2_e9)
    elif (hero >= 20 and hero < 30 and enemy >= 80 and enemy < 90):
        print(h2_e8)
    elif (hero >= 20 and hero < 30 and enemy >= 70 and enemy < 80):
        print(h2_e7)
    elif (hero >= 20 and hero < 30 and enemy >= 60 and enemy < 70):
        print(h2_e6)
    elif (hero >= 20 and hero < 30 and enemy >= 50 and enemy < 60):
        print(h2_e5)
    elif (hero >= 20 and hero < 30 and enemy >= 40 and enemy < 50):
        print(h2_e4)
    elif (hero >= 20 and hero < 30 and enemy >= 30 and enemy < 40):
        print(h2_e3)
    elif (hero >= 20 and hero < 30 and enemy >= 20 and enemy < 30):
        print(h2_e2)
    elif (hero >= 20 and hero < 30 and enemy >= 10 and enemy < 20):
        print(h2_e1)
    elif (hero >= 20 and hero < 30 and enemy < 10):
        print(h2_e0)

    elif (hero >= 10 and hero < 20 and enemy == 100):
        print(h1_e10)
    elif (hero >= 10 and hero < 20 and enemy >= 90 and enemy < 100):
        print(h1_e9)
    elif (hero >= 10 and hero < 20 and enemy >= 80 and enemy < 90):
        print(h1_e8)
    elif (hero >= 10 and hero < 20 and enemy >= 70 and enemy < 80):
        print(h1_e7)
    elif (hero >= 10 and hero < 20 and enemy >= 60 and enemy < 70):
        print(h1_e6)
    elif (hero >= 10 and hero < 20 and enemy >= 50 and enemy < 60):
        print(h1_e5)
    elif (hero >= 10 and hero < 20 and enemy >= 40 and enemy < 50):
        print(h1_e4)
    elif (hero >= 10 and hero < 20 and enemy >= 30 and enemy < 40):
        print(h1_e3)
    elif (hero >= 10 and hero < 20 and enemy >= 20 and enemy < 30):
        print(h1_e2)
    elif (hero >= 10 and hero < 20 and enemy >= 10 and enemy < 20):
        print(h1_e1)
    elif (hero >= 10 and hero < 20 and enemy < 10):
        print(h1_e0)

    else:
        print("                      Needs debugging!")


def max_hp_filter(hp, max_health):
    new_hp = ((hp / max_health) * 100)

    return (new_hp)


def healing(increase_amount, max_hp, hp):
    hp_difference = (max_hp - hp)
    if (hp <= (max_hp - (increase_amount))):
        hp += increase_amount
    elif (hp < max_hp and hp > (max_hp - (increase_amount))):
        hp = hp + hp_difference

    return hp


def battle(enemy, Class, strength, magic, player_hp, max_health, xp):
    #print("THE STARTING XP IS . . .", xp)
    # sleep(2)

    if (Class == 1):
        enemy_file = (enemy + "vhero.txt")
        enemy_pic = open(enemy_file, 'r').read()
    elif (Class == 2):
        enemy_pic = open("2herovorc.txt", 'r').read()

    #hero_pic = open(enemy, 'r').read()
    firstsighting(enemy, 3)
    Magic = magic
    space(50)

############################################

    # Enemy HP based on XP
    if (xp < 200):
        enemy_hp = 65
    elif (xp >= 200):
        enemy_hp = ((xp * 8)/7)

############################################

    # Enemy strength based on XP
    if (xp == 0):
        enemy_strength = .3
    else:
        enemy_strength = (round(xp / 100))

############################################

    max_enemy_hp = enemy_hp
    bq = "none"
    bar_fight_victory1_file = ("bar_fight_victory1.txt")
    bar_fight_victory1 = open(bar_fight_victory1_file, 'r').read()
    bar_fight_victory2_file = ("bar_fight_victory2.txt")
    bar_fight_victory2 = open(bar_fight_victory2_file, 'r').read()

    #road_file = ("road1.2.txt")
    #road = open(road_file, 'r').read()
    #road_file2 = ("road3.2.txt")
    #road3 = open(road_file2, 'r').read()

    while (enemy_hp > 0 and player_hp > 0 and bq.upper() != "B"):
        player_attack = round(random.randint(6, 10) * strength)
        player_defend = round(random.randint(1, 4) * strength)
        enemy_attack = round(random.randint(12, 40) * enemy_strength)
        player_attack2 = round(random.randint(6, 10) * strength)
        player_defend2 = round(random.randint(1, 4) * strength)
        enemy_attack2 = round(random.randint(12, 40) * enemy_strength)
        enemy_defend = round(random.randint(4, 20) * enemy_strength)

        if (Class == 1 or Class == 2):
            print(enemy_pic)
            health(max_hp_filter(player_hp, max_health),
                   max_hp_filter(enemy_hp, max_enemy_hp))
            print("     HP: ", player_hp, "/", max_health,
                  "                                                 HP: ", enemy_hp, "/", max_enemy_hp)
            bq = input(
                "\n                      A|Attack  B|Flee   C|Defend\n                                  ")
            if (bq.upper() == "A" and enemy_hp > 0 and player_hp > 0):
                enemy_hp -= player_attack
                if (enemy_hp > 0 and player_hp > 0):
                    space(50)
                    hero_animation(Class, enemy, 1)
                    print("    You strike a blow! You caused", player_attack, "points of damage against the " +
                          enemy + "\n                 The " + enemy + "'s health is now", enemy_hp)
            elif (bq.upper() == "C" and enemy_hp > 0 and player_hp > 0):
                player_hp += player_defend
                space(50)
                print(enemy_pic)
                health(max_hp_filter(player_hp, max_health),
                       max_hp_filter(enemy_hp, max_enemy_hp))
                print("     HP: ", player_hp, "/", max_health,
                      "                                             HP: ", enemy_hp, "/", max_enemy_hp)
                print("     Like a coward, you bring up your sheild \n                ",
                      player_defend, "points of damage against the " + enemy)
            if (enemy_hp > 0 and player_hp > 0):
                sleep(3)
                space(50)
                player_hp -= round(enemy_attack)
                if (enemy_hp > 0 and player_hp > 0):
                    space(50)
                    enemy_animation(enemy, 1)
                    print("          The " + enemy + " swings at you, causing", enemy_attack,
                          "points of damage! \n                      Your health is now", player_hp)
                    sleep(3)
                    space(50)
                    print(enemy_pic)
                    health(max_hp_filter(player_hp, max_health),
                           max_hp_filter(enemy_hp, max_enemy_hp))
                    print("     HP: ", player_hp, "/", max_health,
                          "                                                  HP: ", enemy_hp, "/", max_enemy_hp)
                    bq = input(
                        "\n                      A|Attack  B|Flee   C|Defend\n                                 ")
            if (bq.upper() == "A" and enemy_hp > 0 and player_hp > 0):
                enemy_hp -= player_attack2
                if (enemy_hp > 0 and player_hp > 0):
                    space(50)
                    hero_animation(Class, enemy, 1)
                    print("   You strike a blow! You caused", player_attack2, "points of damage against the " +
                          enemy + " \n           The " + enemy + "'s health is now", enemy_hp, "\n")
            elif (bq.upper() == "C" and enemy_hp > 0 and player_hp > 0):
                player_hp += player_defend2
                space(50)
                print(enemy_pic)
                health(max_hp_filter(player_hp, max_health),
                       max_hp_filter(enemy_hp, max_enemy_hp))
                print("     HP: ", player_hp, "/", max_health,
                      "                                                    HP: ", enemy_hp, "/", max_enemy_hp)
                print("               Like a coward, you bring up your sheild", player_defend2,
                      "\n                      points of damage against the " + enemy)

            if (enemy_hp > 0 and player_hp > 0):
                sleep(3)
                space(50)
                enemy_hp += enemy_defend
                print("              The " + enemy + " brings up it's blade.  \n                  ",
                      enemy_defend, "point(s) of defense!")
                space(50)

        if (enemy.upper() == "ORC" or enemy.upper() == "ANDUBWIN GOBLIN"):
            if (player_hp <= 0):
                space(100)
                start = input(
                    "                       SORRY YOU LOSE \n \n \n            Press 'ENTER' to play again \n \n \n               Type 'quit' to close.")
            elif (enemy_hp <= 0):
                xp = (xp + 25)
                space(100)
                print("               You bend down to cut the throat off of the " + enemy + ". \n \n\n\n                     You gained 25 XP! Your XP is now",
                      xp, " \n\n             A|Go toward Willowton  B|Go toward Dragonsbane.\n\n                                    ")
        elif (enemy.upper() == "BAFOON" and (player_hp >= 0)):
            xp = (xp + 15)
            space(25)
            print(bar_fight_victory1)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            space(25)
            print(bar_fight_victory2)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            space(25)
            print(bar_fight_victory1)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            space(25)
            print(bar_fight_victory2)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            print(bar_fight_victory1)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            space(25)
            print(bar_fight_victory2)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(.5)
            print(bar_fight_victory1)
            space(1)
            print(
                "    The bafoon shamefully walks away, never to dance so idiotically again.")
            sleep(3)
        elif (bq.upper() == "B"):
            print("                              You flee the scene!")

    return (player_hp, xp)


main()
