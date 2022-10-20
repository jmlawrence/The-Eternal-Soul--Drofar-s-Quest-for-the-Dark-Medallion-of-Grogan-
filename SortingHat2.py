from time import sleep
import os
import sys
def main():
    final = ("Keep Going!")
    while (final.lower() != "quit"):
        space()
        print("                      #######\n                    ##     ########\n                      #     ##########\n                            ############\n                            #############\n                            ###############\n                          ####################### \n                         ############################ \n                      ###                          ###\n                      ##        THE SORTING HAT      ## \n                      ##            v.0.1            ## \n                       ################################# \n                 ################################################\n \n \n \n")
        sleep(4)
        #space()
        name = input("Welcome to the Sorting Hat! Let's get started! What is your name? ")
        while (name == ""):
            space()
            name = input("                   ######## PLEASE PROVIDE YOUR NAME ######## \n \n What is your name? ")
        space()
        hobbies = input("Hi, what are some of your hobbies? ")
        while (hobbies == ""):
            space()
            hobbies = input("                   ######## THAT'S NOT AN ANSWER ######## \n \n What are some of your hobbies? ")        
        space()
        getstarted = ("Q")
        room = ("")
        print ("So, " + name.title() + " you like " + hobbies.lower() + " ... interesting. \n \nLet's get you 'sorted' out! \n")
        getstarted = input("                       Press 'ENTER' to get started!")
            
        #Question 1
        
        space()
        spidersq = input(" You find yourself attacked by thousands of spiders what would you do? \n \n  A) Run screaming in fear! \n  B) Grab a can of bug spray! \n  C) Remember a spell that turns the spiders in flowers. \n \n Type A, B, or C --> ")
        while (spidersq.upper() != "A" and spidersq.upper() != "B" and spidersq.upper() != "C"):
            space()
            
            spidersq = input("                   ######## '" + spidersq.upper() + "' IS NOT AN OPTION ######## \n \n If you found yourself being attacked by thousands of spiders what would you do? \n \n A) Run screaming in fear! \n B) Grab a can of bug spray! \n C) Remember a spell that turns the spiders in flowers. \n \n Type A, B, or C --> ")
        
        #Question 2
        space()
        stealq = input(" You found out that your best friend had stollen 10,000 barrels of butter beer, what would you do? \n \n  A) Send an owl to the authorities. \n  B) Confront your friend and ask him or her to return the contraband. \n  C) Smile and grab a pint. \n \n Type A, B, or C --> ")
        while (stealq.upper() != "A" and stealq.upper() != "B" and stealq.upper() != "C"):
            space()
            stealq = input("                   ######## '" + stealq.upper() + "' IS NOT AN OPTION ########\n \n If you found out that your best friend had stollen 10,000 barrels of butter beer, what would you do? \n \n A) Send an owl to the authorities. \n B) Talk it through with the friend and ask him or her to return the contraband. \n C) Smile and grab a pint.\n \n Type A, B, or C --> ")    
        
        #Question 3 
        space()
        cheatq = input(" Wow, this test is hard. But, to your left, your genius classmate has all the answers exposed. What do you do? \n \n  A) Laugh to yourself and say, 'What a loser, answer 56 is 'C.' \n  B) Sneak a few glances. \n  C) Cheat. No shame. \n \n Type A, B, or C --> ")
        while (cheatq.upper() != "A" and cheatq.upper() != "B" and cheatq.upper() != "C"):
            space()
            cheatq = input("######## '" + cheatq.upper() + "' IS NOT AN OPTION ########\n \n Wow, this test is hard. But, to your left, your genius classmate has all the answers exposed. What do you do? \n \n A) Laugh to yourself and say, 'What a loser, answer 56 is 'C' \n B) Sneak a glance and afterward confess to the teacher \n C) Cheat. No shame. \n \n Type A, B, or C --> ")    
        
        #Question 4
        space()
        walletq = input(" You find a wallet. It has a few dollars in it, but no identification. What do you do? \n \n  A) Turn it in to the local authorities. \n  B) Take the money, but leave the wallet. \n  C) Look around and take the whole thing. Who'll ever know? \n \n Type A, B, or C --> ")
        while (walletq.upper() != "A" and walletq.upper() != "B" and walletq.upper() != "C"):
            space()
            walletq = input("######## '" + walletq .upper() + "' IS NOT AN OPTION ########\n \n You find a wallet. It has a few dollars in it, but no identification. What do you do? \n \n A) Leave it there. They'll find it later. \n B) Take the money, but leave the wallet. \n C) Look around and take the whole thing. Who'll ever know? \n \n Type A, B, or C --> ")   
        
        #Question 5     
        space()
        houseq = input(" Your friend wants you to check out a scary house, but when you get there it says 'DO NOT ENTER: DANGEROUS!' What do you do? \n \n  A) Leave it, it's too dangerous. \n  B) Ask your friend what to do. \n  C) Friend or not, you're going to check this place out! \n \n Type A, B, or C --> ")
        while (spidersq.upper() != "A" and spidersq.upper() != "B" and spidersq.upper() != "C"):
            space()
            spidersq = input("######## '" + spidersq.upper() + "' IS NOT AN OPTION ########\n \n Your friend wants you to check out a scary house, but when you get there it say 'DO NOT ENTER: DANGEROUS!' What do you do? \n \n A) Leave it, it's too dangerous. \n B) Ask your friend what to do. \n C) Friend or not, you're going to check this place out. \n \n Type A, B, or C --> ") 
            
        #Question 6
        space()
        puzzleq = input(" You are given a diffcult puzzle toy to solve. What do you do? \n \n  A) Throw it on the ground! \n  B) Try for a few minutes, see how hard it is. \n  C) Figure it out, even if you have to spend all night on it. \n \n Type A, B, or C --> ")
        while (puzzleq.upper() != "A" and puzzleq.upper() != "B" and puzzleq.upper() != "C"):
            space()
            spidersq = input("######## '" + puzzleq.upper() + "' IS NOT AN OPTION ########\n \n You are given a diffcult puzzle toy to solve. What do you do? \n \n   A) Throw it on the ground! \n  B) Try for a few minutes, see how hard it is. \n  C) Figure it out, even if you have to spend all night on it. \n \n Type A, B, or C --> ")
            
        #Question 7
        space()
        moneyq = input(" You inherit a million dollars. What do you do? \n \n  A) Go out and spend some of it! \n  B) Talk it through with your friends and family \n  C) Run to the bank and deposit it. \n \n Type A, B, or C --> ")
        while (moneyq.upper() != "A" and moneyq.upper() != "B" and moneyq.upper() != "C"):
            space()
            moneyq = input("######## '" + moneyq.upper() + "' IS NOT AN OPTION ########\n \n You inherit a million dollars. What do you do? \n \n  A) Go out and spend some of it! \n  B) Talk it through with your friends and family \n  C) Run to the bank and deposit it. \n \n Type A, B, or C --> ")
            
        #Question 8
        space()
        prankq = input(" Somebody plays a cruel joke on you. What do you do? \n \n  A) Punch them, there and then! \n  B) Laugh along, but plot revenge. \n  C) Laugh, forgive, and forget. \n \n Type A, B, or C --> ")
        while (prankq.upper() != "A" and prankq.upper() != "B" and prankq.upper() != "C"):
            space()
            prankq = input("######## '" + prankq.upper() + "' IS NOT AN OPTION ########\n \n Somebody plays a cruel joke on you. What do you do? \n \n  A) Punch them, there and then! \n  B) Laugh along, but plot revenge. \n  C) Laugh, forgive, and forget. \n \n Type A, B, or C --> ")
            
        #Question 9
        space()
        bossq = input(" You're late for work for the first time in 10 years. Your boss yells at you. What do you do?  \n \n  A) Yell back! You deserve some respect! \n  B) Listen and be respecful. He is your boss. \n  C) Break down and cry. \n \n Type A, B, or C --> ")
        while (bossq.upper() != "A" and bossq.upper() != "B" and bossq.upper() != "C"):
            space()
            bossq = input("######## '" + bossq.upper() + "' IS NOT AN OPTION ########\n \n You're late for work for the first time in 10 years. Your boss yells at you. What do you do?  \n \n  A) Yell back! You deserve some respect! \n  B) Listen and be respecful. He is your boss. \n  C) Break down and cry. \n \n Type A, B, or C --> ")
            
        #Question 10
        space()
        stressq = input(" You just got home from 12 hours at work. Your friend calls and needs you to help with a flat tire. What do you say?  \n \n  A) 'I'm sorry, but I'm really tired . . .' \n  B) Tell them you'll be there in a jiffy, but take an hour. \n  C) Make your way to the car immediately. \n \n Type A, B, or C --> ")
        while (stressq.upper() != "A" and stressq.upper() != "B" and stressq.upper() != "C"):
            space()
            stressq = input("######## '" + stressq.upper() + "' IS NOT AN OPTION ########\n \n  You just got home from 12 hours at work. Your friend calls and needs you to help with a flat tire. What do you say?  \n \n  A) 'I'm sorry, but I'm really tired . . .' \n  B) Tell them you'll be there in a jiffy, but take an hour. \n  C) Make your way to the car immediately. \n \n Type A, B, or C --> ")
            
            
        counterhouses = counter(spidersq.upper(), stealq.upper(), cheatq.upper(), walletq.upper(), houseq.upper(), puzzleq.upper(), moneyq.upper(), prankq.upper(), bossq.upper(), stressq.upper())
        answer = sorting(counterhouses[0], counterhouses[1],counterhouses[2],counterhouses[3])
        #print (counterhouses[0])
        #print (counterhouses)
        
        space()
        print("Hmmmmm ... ", name.title(), " ... it appears ...") 
        sleep(2)
        print("that you most definitely belong in ... ")
        sleep(4)
        space()
        print("                      ################################### \n                      #                                 # \n                      #          ", answer + "!            # \n                      #                                 # \n                      ################################### \n \n \n \n \n \n \n \n \n \n" )
        final = input("                          Press 'ENTER' to play again. \n                             Type 'Quit' to close. ")
    

def counter (spidersq, stealq, cheatq, walletq, houseq, puzzleq, moneyq, prankq, bossq, stressq):
    slytherin = 0
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    
    #Question 1
    if (spidersq == "A"):
        slytherin += 1
    elif (spidersq == "B"):
        gryffindor += 2
    elif (spidersq == "C"):
        ravenclaw += 1
        hufflepuff += 1
        
    #Question 2
    if (stealq == "A"):
        hufflepuff += 2
    elif (stealq == "B"):
        ravenclaw += 1
    elif (stealq == "C"):
        gryffindor += 1
        slytherin += 2
        
    #Question 3
    if (cheatq == "A"):
        ravenclaw += 2
    elif (cheatq == "B"):
        hufflepuff += 1
    elif (cheatq == "C"):
        gryffindor += 1
        slytherin += 2
        
    #Question 4
    if (walletq == "A"):
        gryffindor += 1
        ravenclaw += 1
    elif (walletq == "B"):
        hufflepuff += 1
    elif (walletq == "C"):
        slytherin += 2
        
    #Question 5
    if (houseq == "A"):
        ravenclaw += 2
    elif (houseq == "B"):
        hufflepuff += 1
    elif (houseq == "C"):
        slytherin += 1
        gryffindor += 2
        
    #Question 6
    if (puzzleq == "A"):
        slytherin += 2
    elif (puzzleq == "B"):
        hufflepuff += 1
        gryffindor += 1
    elif (puzzleq == "C"):
        ravenclaw += 2 
        
    #Question 7
    if (moneyq == "A"):
        slytherin += 1
        gryffindor += 1              
    elif (moneyq == "B"):
        ravenclaw += 1
    elif (moneyq == "C"):
        hufflepuff += 2  
        
    #Question 8
    if (prankq == "A"):
        slytherin += 1
    elif (moneyq == "B"):
        hufflepuff += 1
        gryffindor += 1
    elif (moneyq == "C"):
        ravenclaw += 2
            
    #Question 9
    if (bossq == "A"):
        slytherin += 2
        gryffindor += 1 
    elif (prankq == "B"):
        hufflepuff += 1
    elif (prankq == "C"):
        ravenclaw += 2
        
    #Question 10
    if (stressq == "A"):
        ravenclaw += 1
    elif (bossq == "B"):
        slytherin += 1
    elif (bossq == "C"):
        hufflepuff += 1
        gryffindor += 1 
        
    return (slytherin, gryffindor, ravenclaw, hufflepuff)

def sorting(slytherin, gryffindor, ravenclaw, hufflepuff):
    if (slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff):
        return "Slytherin"
    elif (gryffindor >= ravenclaw and gryffindor >= hufflepuff):
        return "Gryffindor"
    elif (ravenclaw > hufflepuff):
        return "Ravenclaw"
    else:
        return ("BROKEN! These were the numbers: Syltherin ... ", slytherin, "Gryffindor ... ", gryffindor, "Hufflepuff ... ", hufflepuff, "Ravenclaw ...", ravenclaw)
def space():
    print ("\n" * 100)

    
    
main()