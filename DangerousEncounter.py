import random

def dungeon():
    playerHealth = 40
    opponent = random.choice(["SKELETON", "VAMPIRE", "BEAR", "KNIGHT"])
    if opponent is "BEAR":
        opponentHealth = 25
    if opponent is "SKELETON":
        opponentHealth = 40
    if opponent is "VAMPIRE":
        opponentHealth = 60
    if opponent is "KNIGHT":
        opponentHealth = 75
    userDefend = False
    userBlind = False
    opponentDefend = False
    opponentBlind = False
    run = True
    while run:
        
        userDefend = False
        opponentBlind = False
 
        
        print("A", opponent, "appears before you! Your options in combat are:")
        print("1) Attack")
        print("2) Defend")
        print("3) Blind")
        print("4) RAGE!!")
        
        playerAction = input("Enter the number for the action you want to take.")
        playerAction = int(playerAction)
        
        if playerAction is 1:
            print("You go for an attack on", opponent, "...")
            hit = random.randrange(1, 10)
            if userBlind:
                if hit > 6:
                    print("You whiffed it!", opponent, "is unharmed!")
            else:
                if hit > 8:
                    print("You whiffed it!", opponent, "is unharmed!")
                elif hit is 5:
                    playerDamage = random.randrange(10, 15) * 2
                    print("CRITICAL STRIKE!")
                else:
                    playerDamage = random.randrange(10, 15)
                    if opponentDefend:
                        playerDamage /= 2
                opponentHealth = opponentHealth - playerDamage
                print("You deal", playerDamage, "damage to", opponent)
                
        if playerAction is 2:
            userDefend = True
            print("You defend yourself.")
            
        if playerAction is 3:
            opponentBlind = True
            print("You cast a light that blinds the", opponent, "! Their accuracy is reduced until your next turn.")
            
        if playerAction is 4:
            print("You activate your RAGE against", opponent, "...")
            hit = random.randrange(1, 10)
            if hit > 6:
                print("You whiffed it!", opponent, "is unharmed!")
            elif hit is 5:
                playerDamage = random.randrange(10, 15) * 6
                if opponentDefend:
                    playerDamage /= 2
                opponentHealth = opponentHealth - playerDamage
                print("CRITICAL STRIKE! You deal", playerDamage, "damage to", opponent)
            else:
                playerDamage = random.randrange(10, 15) * 3
                if opponentDefend:
                    playerDamage /= 2
                opponentHealth = opponentHealth - playerDamage
                print("You deal", playerDamage, "damage to", opponent)

        print("You have", playerHealth, "HP remaining.", opponent, "has", opponentHealth, "HP remaining.")

        userBlind = False
        opponentDefend = False

        if opponentHealth <= 0:
            print("Congratulations! You have defeated the", opponent, "!")
            run = False
            
        opponentAction = random.randrange(1, 4)
        if opponentAction is 1:
            print(opponent,"goes for an attack on you...")
            hit = random.randrange(1, 10)
            if opponentBlind:
                if hit > 6:
                    print(opponent, "whiffed it! You are unharmed!")
            else:
                if hit > 8:
                    print(opponent, "whiffed it! You are unharmed!")
                elif hit is 5:
                    opponentDamage = random.randrange(10, 15) * 2
                    print("CRITICAL STRIKE!")
                    if userDefend:
                        opponentDamage /= 2
                else:
                    opponentDamage = random.randrange(10, 15)
                    if userDefend:
                        opponentDamage /= 2
                playerHealth = playerHealth - opponentDamage
                print(opponent, "deals", opponentDamage, "damage to you.")

        if opponentAction is 2:
            opponentDefend = True
            print(opponent, "defends.")
            
        if opponentAction is 3:
            userBlind = True
            print(opponent, "confuses your vision with wild and unpredictable movements.")
            
        if opponentAction is 4:
            print(opponent, "gets angry and flies at you!")
            hit = random.randrange(1, 10)
            if opponentBlind:
                if hit > 6:
                    print(opponent, "whiffed it! You are unharmed!")
            else:
                if hit > 8:
                    print(opponent, "whiffed it! You are unharmed!")
                elif hit is 5:
                    opponentDamage = random.randrange(10, 15) * 6
                    print("CRITICAL STRIKE!")
                    if userDefend:
                        opponentDamage /= 2
                else:
                    opponentDamage = random.randrange(10, 15) * 3
                    if userDefend:
                        opponentDamage /= 2
                playerHealth = playerHealth - opponentDamage
                print(opponent, "deals", opponentDamage, "damage to you.")

        print("You have", playerHealth, "HP remaining.", opponent, "has", opponentHealth, "HP remaining.")

        opponentBlind = False
        userDefend = False

        if playerHealth <= 0:
            print("YOU HAVE BEEN DEFEATED.")
            run = False
        
dungeon()
