import time
import os
import random

def round_one():
    # round 1
    print("【|】|| 💀")
    time.sleep(1)
    
    print("1 LIVE ROUND 2 BLANKS")
    a = random.randint(1, 3)
    b = random.randint(1, 2)
    c = random.randint(1, 1)
    
    x = input("YOU OR DEALER? Y/D")
    y_hp = 2
    d_hp = 2
    
    # start = self
    if x == "Y":
        if a == 3:
            time.sleep(1)
            print("IT'S LIVE ROUND, YOU HAVE 1 HP")
            time.sleep(1)
            print("DEALER SHOT HIMSELF, IT'S BLANK")
            time.sleep(1)
            print("DEALER SHOT HIMSELF, IT'S BLANK")
            y_hp = 1
        else:
            time.sleep(1)
            print("IT'S BLANK")
            time.sleep(1)
            y = input("YOU OR DEALER? Y/D")
            if y == "Y":
                if b == 2:
                    time.sleep(1)
                    print("IT'S LIVE ROUND, YOU HAVE 1 HP")
                    y_hp = 1
                    time.sleep(1)
                    print("DEALER SHOT HIMSELF, IT'S BLANK")
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("IT'S BLANK")
                    w = input("YOU OR DEALER? Y/D")
                    if w == "Y":
                        if c == 1:
                            time.sleep(1)
                            print("IT'S LIVE ROUND, YOU HAVE 1 HP")
                            y_hp = 1
                    elif w == "D":
                        if c == 1:
                            time.sleep(1)
                            print("IT'S LIVE ROUND, DEALER HAS 1 HP")
                            d_hp = 1
                    else:
                        print("Wrong answer......")
                        time.sleep(1)
                        round_one()
            elif y == "D":
                if b == 2:
                    time.sleep(1)
                    print("IT'S LIVE ROUND, DEALER HAS 1 HP")
                    time.sleep(1)
                    print("DEALER SHOT HIMSELF, IT'S BLANK")
                    d_hp = 1
                else:
                    time.sleep(1)
                    print("IT'S BLANK")
                    time.sleep(1)
                    if c == 1:
                        time.sleep(1)
                        print("DEALER STOT YOU, YOU HAVE 1 HP")
                        y_hp = 1
                        time.sleep(1)
            else:
                print("Wrong answer......")
                time.sleep(1)
                round_one()
                            
    elif x == "D":
        if a == 3:
            time.sleep(1)
            print("IT'S LIVE ROUND, DEALER HAS 1 HP")
            time.sleep(1)
            d_hp = 1
            print("DEALER SHOOTS HIMSELF, IT'S BLANK")
            time.sleep(1)
            print("DEALER SHOOTS HIMSELF, IT'S BLANK")
            time.sleep(1)
        else:
            time.sleep(1)
            print("IT'S BLANK")
            time.sleep(1)
            if b == 2:
                print("DEALER SHOTS YOU, IT'S LIVE ROUND, YOU HAVE 1 HP")
                y_hp = 1
                time.sleep(1)
                print("YOU SHOOT YOURSELF, IT'S BLANK")
                time.sleep(1)

            else:
                time.sleep(1)
                print("DEALER TRIED TO SHOOT YOU, BUT IT'S BLANK")
                time.sleep(1)
                print("YOU SHOT TO DEALER, HE HAS 1 HP")
                time.sleep(1)
    
    else:
        print("Wrong answer......")
        time.sleep(1)
        round_one()
                
    print(f"YOUR HP: {y_hp}, DEALER'S HP: {d_hp}")
    time.sleep(1)
    print("LET'S CONTINUE")
    time.sleep(1)
    print("3 LIVE ROUND, 2 BLANKS")
    
    pa = random.randint(1, 5)
    
    aa = input("YOU OR DEALER? Y/D ")
    
    if aa == "Y":
        if pa == 1:
            time.sleep(1)
            print("IT'S BLANK")
            bb = input("YOU OR DEALER? Y/D")
            if bb == "Y":
                y_hp -= 1 
                if y_hp == 0:
                    print("YOU DEAD")
                    healing()
                else:
                    time.sleep(1)
                    print(f"YOU HAVE {y_hp} HP")
                    time.sleep(1)
                    print("DEALER SHOT YOU")
                    time.sleep(1)
                    print("YOU DEAD")
                    healing()
            elif bb == "D":
                time.sleep(1)
                print("YOU SHOT DEALER, DEALER DEAD")
            else:
                print("Wrong answer......")
                time.sleep(1)
                round_one()
            
        elif pa == 2:
            time.sleep(1)
            print("IT'S BLANK")
            bb = input("YOU OR DEALER? Y/D")
            if bb == "Y":
                y_hp -= 1 
                if y_hp == 0:
                    time.sleep(1)
                    print("YOU DEAD")
                    healing()
                else:
                    print(f"YOU HAVE {y_hp} HP")
                    time.sleep(1)
                    print("DEALER SHOT YOU")
                    time.sleep(1)
                    print("YOU DEAD")
                    healing()
            elif bb == "D":
                d_hp -= 1 
                if d_hp < 1:
                    time.sleep(1)
                    print("DEALER DEAD")
                elif d_hp == 0:
                    print(f"DEALER HAS {y_hp} HP")
                    time.sleep(1)
                    print("DEALER SHOT YOU, BUT IT BLANK")
                    time.sleep(1)
                    print("YOU SHOT DEALER, HE DEAD")
                elif d_hp == 2:
                    print(f"DEALER HAS {y_hp} HP")
                    time.sleep(1)
                    print("DEALER SHOT YOU, BUT IT BLANK")
                    time.sleep(1)
                    print("YOU SHOT DEALER, THAN HE SHOT HIMSELF, HE DEAD")
                    time.sleep(1)
                    
            else:
                print("Wrong answer......")
                time.sleep(1)
                round_one()
                
        else:
            time.sleep(1)
            print("IT'S LIVE ROUND")
            y_hp -= 1
            if y_hp == 0:
                time.sleep(1)
                print("YOU DEAD")
                healing()
            else:
                print(f"YOU HAVE {y_hp} HP")
                time.sleep(1)
                time.sleep(1)
                print("DEALER SHOT YOU")
                print("YOU DEAD")
                healing()

    elif aa == "D":
        if pa == 1:
            time.sleep(1)
            print("IT'S BLANK")
            time.sleep(1)
            print("DEALER SHOT YOU")
            y_hp -= 1
            if y_hp == 0:
                print("YOU DEAD")
                healing()
            else:
                print(f"YOU HAVE {y_hp} HP")
                time.sleep(1)
                print("YOU SHOT DEALER")
                print("DEALER DEAD")
        elif pa == 2:
            time.sleep(1)
            print("IT'S BLANK")
            print("DEALER SHOT YOU")
            if y_hp == 0:
                print("YOU DEAD")
                healing()
            else:
                print(f"YOU HAVE {y_hp} HP")
                time.sleep(1)
                print("YOU SHOT DEALER")
                print("DEALER DEAD")
        else:
            time.sleep(1)
            print("IT'S LIVE ROUND")
            d_hp -= 1
            
            if d_hp == 0:
                print("DEALER DEAD")
            else:
                print(f"DEALER HAS {d_hp} HP")
                print("DEALER TRIED TO SHOT YOU, IT'S BLANK")
                input()
                print("YOU SHOT DEALER")
                input()
                print("DEALER SHOT HIMSELF")
                print("DEALER DEAD")
    
    else:
        print("Wrong answer......")
        time.sleep(1)
        round_one()
    
    print("YOU WIN 1 ROUND")
    time.sleep(1)
    round_two()

def round_two():
    # round two 
    print("|【||】💀")
    time.sleep(1)
    print("LET'S MAKE IT LITTLE MORE INTERESTING")
    time.sleep(2)
    print("ITEMS:")
    print("🚬 = Gives the user an extra life.")
    print("🍺 = Racks the shotgun and the bullet inside will be discarded.")
    print("🔪 = Shotgun will deal double damage for one turn.")
    print("🔍 = User will see what bullet is in the chamber.")
    print("⛓ = Handcuffs the other person so they miss their next turn.")
    
    items = ["🚬",
             "🍺",
             "🔪",
             "🔍",
             "⛓"]

    yio = random.choice(items)
    yit = random.choice(items)
    
    dio = random.choice(items)
    dit = random.choice(items)
    
    input()
    print(f"YOU HAVE {yio} AND {yit}")
    print(f"DEALER HAS {dio} AND {dit}")
    
    y_hp = 4
    d_hp = 4
    
    print("1 LIVE ROUND 1 BLANK")
    
    o = random.randint(1, 2)
    
    shot = input("YOU, DEALER OR " + yio + yit)
    
    if shot == "🔍":
        if o == 2:
            print("NEXT PATRON IS LIVE ROUND")
            input()
            if yit == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            elif yio == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            else:
                d_hp -= 1
                print("YOU SHOT DEALER")
                
        else:
            print("NEXT PATRON IS BLANK")
            print("YOU SHOT YOURSELF, IT'S BLANK")
            if yit == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            elif yio == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            else:
                d_hp -= 1
                print("YOU SHOT DEALER")
            
            
    elif shot == "🔪":
        if o == 2:
            print("YOU SHOT DEALER, IT'S LIVE ROUND")
            d_hp -= 2
            print(f"DEALER HAS {d_hp} HP")
        else:
            print("IT'S BLANK")
    
    elif shot == "🚬":
        if y_hp == 4:
            print("YOU WASTE THE CIGARETTE ")
        else:
            y_hp += 1 
            print(f"YOU HAVE {y_hp}")
    
    elif shot == "🍺":
        if o == 2:
            print(f"IT WAS BE LIVE ROUND")
        else:
            print("IT WAS BE BLANK")
            if yit == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            elif yio == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            else:
                d_hp -= 1
                print("YOU SHOT DEALER")
            
    elif shot == "⛓" : 
        print("DEALER SKIPS 2 MOVES")
        if yit == "🔪":
            d_hp -= 2
            print("YOU SHOT DEALER")
        elif yio == "🔪":
            d_hp -= 2
            print("YOU SHOT DEALER")
        else:
            d_hp -= 1
            print("YOU SHOT DEALER")
        
    elif shot == "Y":
        if o == 2:
            y_hp -= 1 
            print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
            input()
            print("DEALER SHOT YOU")
            print(f"IT'S BLANK")
        else:
            print("IT'S BLANK")
            if yit == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            elif yio == "🔪":
                d_hp -= 2
                print("YOU SHOT DEALER")
            else:
                d_hp -= 1
                print("YOU SHOT DEALER")
            
    elif shot == "D":
        if o == 2:
            d_hp -= 1 
            print(f"IT'S LIVE ROUND, DEALER'S HP: {y_hp}")
            input()
            print("DEALER SHOT HIMSELF")
            print(f"IT'S BLANK")
        else:
            print("IT'S BLANK")
            if dit == "🔪":
                print("DEALER SHOT YOU WITH KNIFE")
                y_hp -= 2 
                print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
            elif dio == "🔪":
                print("DEALER SHOT YOU WITH KNIFE")
                y_hp -= 2 
                print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
            else:
                print("DEALER SHOT YOU")
                y_hp -= 1
                print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
    else:
        print("IT'S WRONG ANSWER....")
        time.sleep(2)
        round_two()

    print(f"YOUR HP: {y_hp}, DEALER'S HP: {d_hp}")
    print("2 LIVE ROUND, 2 BLANKS")
    
    items = ["🚬",
             "🍺",
             "🔪",
             "🔍",
             "⛓"]

    yio = random.choice(items)
    yit = random.choice(items)
    
    dio = random.choice(items)
    dit = random.choice(items)
    
    input()
    print(f"YOU HAVE {yio} AND {yit}")
    print(f"DEALER HAS {dio} AND {dit}")
    time.sleep(1)
    
    a = random.randint(1, 4)
    b = random.randint(1, 3)
    c = random.randint(1, 2)
    d = random.randint(1, 1)
    
    shoot = input(f"{yio} or {yit}")
    
    if shoot == "🔍":
        if yio != "🔍":
            if yit != "🔍":
                print("YOU DON'T HAVE IT")
            else:
                if "1" or "2" in a:
                    print("NEXT PATRON IS LIVE ROUND")
                    if yio == "🔪":
                        d_hp -= 2
                        print(f"YOU SHOT IN DEALER WITH KNIFE, HE HAS {d_hp}")
                    elif yit == "🔪":
                        d_hp -= 2
                        print(f"YOU SHOT IN DEALER WITH KNIFE, HE HAS {d_hp}")
                    else:
                        d_hp -= 1
                        print(f"YOU SHOT IN DEALER, HE HAS {d_hp}")
                else:
                    print("NEXT PATRON IS BLANK")
        else:
            if "1" or "2" in a:
                print("NEXT PATRON IS LIVE ROUND")
            else:
                print("NEXT PATRON IS BLANK")
                
    elif shoot == "🔪":
        if yio != "🔪":
            if yit != "🔪":
                print("YOU DON'T HAVE IT")

            else:
                if "1" or "2" in a:
                    d_hp -= 2
                    print(f"IT'S LIVE ROUND, YOU SHOT DEALER, HE HAS {d_hp} HP")
                else:
                    print("NEXT PATRON IS BLANK")
        else:
            if "1" or "2" in a:
                d_hp -= 2
                print(f"IT'S LIVE ROUND, YOU SHOT DEALER, HE HAS {d_hp} HP")
            else:
                print("NEXT PATRON IS BLANK")
    
    elif shoot == "🚬":
        if yio != "🚬":
            if yit != "🚬":
                print("YOU DON'T HAVE IT")

            else:
                y_hp += 1 
                print(f"YOU USE THE CIGARETTE, YOUR HP: {y_hp}")
        else:
            y_hp += 1 
            print(f"YOU USE THE CIGARETTE, YOUR HP: {y_hp}")

    
    elif shoot == "🍺":
        if yio != "🍺":
            if yit != "🍺":
                print("YOU DON'T HAVE IT")

            else:
                if "1" or "2" in a:
                    print("IT WAS BE LIVE ROUND")
                else:
                    print("IT WAS BE BLANK")
        else:
            if "1" or "2" in a:
                print("IT WAS BE LIVE ROUND")
            else:
                print("IT WAS BE BLANK")
            
    elif shoot == "⛓" : 
        if yio != "⛓":
            if yit != "⛓":
                print("YOU DON'T HAVE IT")

            else:
                if "1" or "2" in a:
                    if yio == "🔪":
                        d_hp -= 2
                        print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                    elif yit == "🔪":
                        d_hp -= 2
                        print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                    else:
                        d_hp -= 1 
                        print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                    
                    print("YOU CAN TRY ONE MORE TIME")
                    time.sleep(1)
                    if "1" or "2" in a:
                        if yio == "🔪":
                            d_hp -= 2
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                        elif yit == "🔪":
                            d_hp -= 2
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                        else:
                            d_hp -= 1 
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                    else:
                        print("IT'S BLANK")
                else:
                    print("IT WAS BE BLANK")
                    time.sleep(1)
                    print("TRY ONE MORE TIME")
                    time.sleep(1)
                    if "1" or "2" in a:
                        if yio == "🔪":
                            d_hp -= 2
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                        elif yit == "🔪":
                            d_hp -= 2
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                        else:
                            d_hp -= 1 
                            print(f"YOU SHOT DEALER, HE HAS {d_hp}")
                    else:
                        print("YOU AREN'T LUCKY")
        else:
            if "1" or "2" in a:
                print("IT WAS BE LIVE ROUND")
            else:
                print("IT WAS BE BLANK")
                
    print(f"YOU HAVE {y_hp} HP, DEALER HAS {d_hp} HP")
    if d_hp == 0:
        round_three()
    else:
        print("3 LIVE ROUND AND 3 BLANKS")
        time.sleep(1)
        print("NOW WE DON'T HAVE ITEMS, BECAUSE IT DOESN'T NEW LOADING")
        time.sleep(1)
        
        
    a = random.randint(1, 6)
    b = random.randint(1, 5)
    c = random.randint(1, 4)
    d = random.randint(1, 3)
    e = random.randint(1, 2)
    f = random.randint(1, 1)
        
    sh = input("YOU OR DEALER? Y/D ")
        
    if sh == "Y":
        if "1" or "2" or "3" in sh:
            y_hp -= 1 
            print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
            if y_hp == 0:
                print("YOU DEAD")
                healing_two()
            else:
                print("DEALER TRY TO SHOOT YOU, BUT IT'S BLANK")
                time.sleep(1)
                d_hp -= 1
                print(f"YOU SHOT DEALER, HE HAS {d_hp} HP")
                if d_hp == 0:
                    print("DEALER DIED, YOU WIN 2 ROUND")
                else:
                    time.sleep(1)
                    y_hp -= 1
                    print(f"DEALER SHOT YOU, YOU HAVE {y_hp} HP")
                    if y_hp == 0:
                        print("YOU DEAD")
                        healing_two()
                    else:
                        print("YOU SHOT DEALER, DEALER DEAD, YOU WIN 2 ROUND")
                        round_three_words()
        else:
            print("IT'S BLANK")
            print("YOU SHOT DEALER, IT'S LIVE ROUND")
            d_hp = 0
            print("DEALER DIED, YOU WIN 2 ROUND")
            round_three_words()
                
    elif sh == "D":
        print("IT'S LIVE ROUND")
        d_hp -= 1
        if d_hp == 0:
            print("DEALER DIED, YOU WIN 2 ROUND")
        else:
            print("DEALER SHOT HIMSELF, HE DEAD, YOU WIN 2 ROUND")
            round_three_words()
    round_three_words()

        
def progress(value, total, i=0, j=0):
    percents = 100*value/total
    print("defibrillator switching off...")
    print('[{}{}] {}%\n'.format(('█'*int(percents//10)),'░'*(10-int(percents//10)), percents))
    
    
def round_three_words():
    time.sleep(2)
    print("\n \n \n")
    print("| ||【💀】")
    time.sleep(1)
    print("NO MORE DEFIBRILLATORS, NO MORE BLOOD TRANSFUSIONS, \nNOW IT'S JUST YOU AND ME, WE ARE DANCING \nON THE EDGE OF DEATH AND LIFE")
    time.sleep(1)
    print("\nlogin...")
    time.sleep(1)
    print("Successful")
    input()
    for i in range(1000):
        progress(i,1000) 
        time.sleep(0.01)
        
    print("Successful")
    input()
    round_three()
    
def round_three():
    y_hp = 6
    d_hp = 6
    
    txt = 'FOUR ITEMS EACH \n'
    for i in txt:
        time.sleep(0.05)
        print(i, end='', flush=True)
    
    
    items = ["🚬",
             "🍺",
             "🔪",
             "🔍",
             "⛓"]
    
    ai = random.choice(items) 
    bi = random.choice(items) 
    ci = random.choice(items) 
    di = random.choice(items) 
    
    da = random.choice(items) 
    db = random.choice(items) 
    dc = random.choice(items) 
    dd = random.choice(items) 
    
    input()
    
    items_list = f'YOUR ITEMS: {ai}, {bi}, {ci}, {di}.'
    for i in items_list:
        time.sleep(0.03)
        print(i, end='', flush=True)
        
    input()
    
    items_list_dealer = f"DEALER'S ITEMS: {da}, {db}, {dc}, {dd}."
    for i in items_list_dealer:
        time.sleep(0.03)
        print(i, end='', flush=True)
    
    input()
    
    patrons = '1 LIVE ROUND, 2 BLANKS. \n'
    for i in patrons:
        time.sleep(0.03)
        print(i, end='', flush=True)
    
    
    know = 'YOU KNOW THE DRILL. \n'
    for i in know:
        time.sleep(0.01)
        print(i, end='', flush=True)  
        
    patron_one = random.randint(1, 3)
    patron_two = random.randint(1, 2)
    patron_three = random.randint(1, 1)
    
    shot = input(f"USE ITEMS: {ai}, {bi}, {ci} OR {di}?")
    
    pilist = [ai, bi, ci, di]
    dilist = [da, db, dc, dd]
    
    if shot == "🔍":
        if "🔍" not in pilist:
            print("YOU DON'T HAVE THIS ITEM")
            time.sleep(1)
            round_three()
        else:
            if patron_one == 1:
                time.sleep(1)
                print("NEXT PATRON IS LIVE ROUND")
            else:
                time.sleep(1)
                print("NEXT PATRON IS BLANK")
                
    elif shot == "🔪":
        if "🔪" not in pilist:
            print("YOU DON'T HAVE THIS ITEM")
            time.sleep(1)
            round_three()
        else:
            if patron_one == 1:
                time.sleep(1)
                d_hp -= 2
            else:
                return "unsuccess"
                
    elif shot == "🚬":
        if "🚬" not in pilist:
            print("YOU DON'T HAVE THIS ITEM")
            time.sleep(1)
            round_three()
        else:
            if y_hp < 4:
                y_hp += 1 
                print(f"YOU HAVE {y_hp} HP")
            else:
                print("YOU WASTE A CIGARETTE")
    
    elif shot == "🍺":
        if "🍺" not in pilist:
            print("YOU DON'T HAVE THIS ITEM")
            time.sleep(1)
            round_three()
        else:
            if patron_one == 1:
                time.sleep(1)
                print("IT WAS BE LIVE ROUND")
            else:
                print("IT WAS BE BLANK")
    
    elif shot == "⛓":
        if "⛓" not in pilist:
            print("YOU DON'T HAVE THIS ITEM")
            time.sleep(1)
            round_three()
        else:
            print("DEALER SKIPS TWO MOVES")
    
    shoot = input("YOU OR DEALER? Y/D ")
    
    if shoot == "D":
        if shot == "⛓":
            if patron_one == "1":
                if "🔪" in pilist:
                    d_hp -= 2
                    time.sleep(1)
                    print(f"YOU SHOT DEALER WITH KNIFE, DEALER HAS {d_hp} HP")
                else:
                    d_hp -= 1 
                    time.sleep(1)
                    print(f"YOU SHOT DEALER, DEALER HAS {d_hp} HP")
            else:
                time.sleep(1)
                print("TRY ONE MORE TIME, IT'S BLANK")
                
                time.sleep(1)
                if patron_two == "1":
                    if "🔪" in pilist:
                        d_hp -= 2
                        time.sleep(1)
                        print(f"YOU SHOT DEALER WITH KNIFE, DEALER HAS {d_hp} HP")
                    else:
                        d_hp -= 1 
                        time.sleep(1)
                        print(f"YOU SHOT DEALER, DEALER HAS {d_hp} HP")
                else:
                    print("IT'S BLANK")
                    if "🔪" in dilist: 
                        y_hp -= 2
                        time.sleep(1)
                        print(f"DEALER SHOT YOU WITH KNIFE, YOU HAVE {y_hp} HP")
                    else:
                        y_hp -= 1
                        time.sleep(1)
                        print(f"DEALER SHOT YOU, YOU HAVE {y_hp} HP")   
                        
    elif shoot == "Y":
        if patron_one == 1:
            y_hp -= 1 
            print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
            time.sleep(1)
            print("YOU SHOT YOURSELF, IT'S BLANK")
            time.sleep(1)
            print("DEALER SHOT HIMSELF, IT'S BLANK")
        else:
            print("IT'S BLANK")
            shot_two = input("YOU OR DEALER? Y/D ")
            if shot_two == "Y":
                if patron_two == 1:
                    print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
                    time.sleep(1)
                    print("YOU SHOT YOURSELF, IT'S BLANK")
                    time.sleep(1)
                else:
                    print("IT'S BLANK")
                    shot_three = input("YOU OR DEALER? Y/D ")
                    if shot_three == "Y":
                        if patron_two == 1:
                            y_hp -= 1
                            print(f"IT'S LIVE ROUND, YOUR HP: {y_hp}")
                            time.sleep(1)
                        else:
                            print("IT'S BLANK")
                    elif shot_three == "D":
                        if "🔪" in pilist:
                            if patron_two == 1:
                                d_hp -= 2
                                time.sleep(1)
                                print(f"IT'S LIVE ROUND, DEALER'S HP {d_hp}")
                                time.sleep(1)
                                print("DEALER SHOT HIMSELF, IT'S BLANK")
                            else:
                                print("IT'S BLANK")
                        else:
                            if patron_two == 1:
                                d_hp -= 1
                                time.sleep(1)
                                print(f"IT'S LIVE ROUND, DEALER'S HP {d_hp}")
                                time.sleep(1)
                                print("DEALER SHOT HIMSELF, IT'S BLANK")
                            else:
                                print("IT'S BLANK")

                    
            elif shot == "🍺":
                shoot_two = input("YOU OR DEALER? Y/D ")
                if shoot_two == "Y":
                    if patron_two == 1:
                        y_hp -= 1
                        time.sleep(1)
                        print(f"IT'S LIVE ROUND, YOUR HP {y_hp}")
                        time.sleep(1)
                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                    else:
                        print("IT'S BLANK")
                        time.sleep()
                        d_hp -= 1 
                        print(f"YOU SHOT DEALER, IT'S LIVE ROUND, DEALER'S HP: {d_hp}")
            
            else:
                sh = input("YOU OR DEALER? Y/D ")
                if sh == "Y":
                    if patron_one == "1":
                        y_hp -= 1
                        print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                        time.sleep(1)
                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                        time.sleep(1)
                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                    else:
                        print("IT'S BLANK")
                        sh_two = input("YOU OR DEALER? Y/D ")
                        if sh_two == "Y":
                            if patron_two == "1":
                                y_hp -= 1
                                print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                time.sleep(1)
                                print("DEALER SHOT HIMSELF, IT'S BLANK")
                            else:
                                print("IT'S BLANK")
                                sh_three = input("YOU OR DEALER? Y/D ")
                                    
                                if sh_three == "Y":
                                    if patron_three == "1":
                                        y_hp -= 1
                                        print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                        time.sleep(1)
                                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
                                            
                                elif sh_three == "D":
                                    if patron_three == "1":
                                        d_hp -= 1
                                        print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                        time.sleep(1)
                                        print("YOU SHOT YOURSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
            
                        
                        elif sh_two == "D":
                            if patron_two == "1":
                                d_hp -= 1
                                print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                time.sleep(1)
                                print("YOU SHOT YOURSELF, IT'S BLANK")
                            else:
                                if sh_three == "Y":
                                    if patron_three == "1":
                                        y_hp -= 1
                                        print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                        time.sleep(1)
                                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
                                            
                                elif sh_three == "D":
                                    if patron_three == "1":
                                        d_hp -= 1
                                        print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                        time.sleep(1)
                                        print("YOU SHOT YOURSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
                                            
                elif sh == "D":
                    if patron_one == "1":
                        d_hp -= 1
                        print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                        time.sleep(1)
                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                        time.sleep(1)
                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                    else:
                        print("IT'S BLANK")
                        sh_two = input("YOU OR DEALER? Y/D ")
                        if sh_two == "Y":
                            if patron_two == "1":
                                y_hp -= 1
                                print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                time.sleep(1)
                                print("DEALER SHOT HIMSELF, IT'S BLANK")
                            else:
                                print("IT'S BLANK")
                                sh_three = input("YOU OR DEALER? Y/D ")
                                    
                                if sh_three == "Y":
                                    if patron_three == "1":
                                        y_hp -= 1
                                        print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                        time.sleep(1)
                                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
                                            
                                elif sh_three == "D":
                                    if patron_three == "1":
                                        d_hp -= 1
                                        print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                        time.sleep(1)
                                        print("YOU SHOT YOURSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
            
                        
                        elif sh_two == "D":
                            if patron_two == "1":
                                d_hp -= 1
                                print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                time.sleep(1)
                                print("YOU SHOT YOURSELF, IT'S BLANK")
                            else:
                                sh_t = input("YOU OR DEALER? Y/D ")
                                if sh_t == "Y":
                                    if patron_three == "1":
                                        y_hp -= 1
                                        print(f"IT'S LIVE ROUND, YOU HAVE {y_hp} HP")
                                        time.sleep(1)
                                        print("DEALER SHOT HIMSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")
                                            
                                elif sh_t == "D":
                                    if patron_three == "1":
                                        d_hp -= 1
                                        print(f"IT'S LIVE ROUND, DEALER HAS {d_hp} HP")
                                        time.sleep(1)
                                        print("YOU SHOT YOURSELF, IT'S BLANK")
                                    else:
                                        print("IT'S BLANK")  
                                        
    d_hp = 4
    
    input()
    print(f"YOUR HP: {y_hp}, DEALER'S HP: {d_hp}")
    nextt = "LET'S CONTINUE \n"
    for i in nextt:
        time.sleep(0.05)
        print(i, end='', flush=True)
    
    patronsss = "5 LIVE ROUND, 1 BLANK \n"
    for i in patronsss:
        time.sleep(0.05)
        print(i, end='', flush=True)
    input()
    
    end = input("YOU OR DEALER? Y/D ")
  
        
    if end == "D":
        print("IT'S BLANK")
        time.sleep(1)
        print("DEALER PUT HANDCUFFS ON YOU")
        time.sleep(1)
        y_hp -= 2
        print(f"DEALER SHOT YOU WITH KNIFE, YOUR HP: {y_hp}")
        time.sleep(2)
        y_hp -= 2
        print(f"DEALER SHOT YOU WITH KNIFE, YOUR HP: {y_hp}")
        time.sleep(3)
        
        bad_end = "ARE YOU READY?"
        for i in bad_end:
            time.sleep(0.05)
            print(i, end='', flush=True)
        
        input()
        print("THE DEFIBRILLATOR WIRE WAS CUT\n")
        time.sleep(2)
        d_hp -= 1
        print(f"YOU SHOT DEALER, HIS HP: {d_hp}\n")
        time.sleep(1)
        print("GOOD BYE...")
        time.sleep(3)
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        time.sleep(1)
        exit()

    elif end == "Y":
        print("IT'S BLANK")
        time.sleep(1)
        print("YOU PUT HANDCUFFS ON DEALER")
        time.sleep(1)
        d_hp -= 2
        print(f"YOU SHOT DEALER WITH KNIFE, HIS HP: {d_hp}")
        time.sleep(2)
        good_end = "ARE YOU READY?"
        for i in good_end:
            time.sleep(0.01)
            print(i, end='', flush=True)
            
        input()
        print("THE DEFIBRILLATOR WIRE WAS CUT\n")
        time.sleep(2)
        print("Good bye, Dealer...")
        last_dealer_words = "THANKS FOR GAME..."
        for i in last_dealer_words:
            time.sleep(0.1)
            print(i, end='', flush=True)
        time.sleep(1)
        print("\nDEALER DEAD \n \n \n")
        
        time.sleep(2)
        cash = random.randint(90000, 100000)
        congratulations = f"CONGRATULATIONS, {name_waiver}!"
        for i in congratulations:
            time.sleep(0.05)
            print(i, end='', flush=True)
            
        time.sleep(0.08)
        print(" You have completed this game, so you:\n")
        time.sleep(0.08)
        print("Sigma ... 100%\n")
        time.sleep(0.08)
        print("Gigachad ... 100%\n")
        time.sleep(0.08)
            
        print(f"TOTAL CASH: {cash}$\n")
        time.sleep(1)
        print("Game developer Maksolotle, thaks you :)")
        input()
        exit()
        
def healing():
    time.sleep(2)
    print(f"Wake up, {name_waiver}! You are alive! Let's continue")
    time.sleep(1)
    print("WELCOME BACK")
    round_one()
    
    
def healing_two():
    time.sleep(2)
    print(f"Wake up, {name_waiver}! You are alive! Let's continue")
    time.sleep(1)
    print("WELCOME BACK")
    round_two()
    
    
def name():
    print("SIGN THE WAIVER")
    time.sleep(1)
    print("\n   GENERAL RELEASE \n    OF LIABILITY \n ")
    print(" 1.||||||||||||||||| \n 2.||||||||||||||||| \n 3.||||||||||||||||| \n 4.||||||||||||||||| \n")
    
    global name_waiver
    name_waiver = input("ENTER NAME:")
    
    round_one()
    
    
def start():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print("𝘼𝙁𝙍𝘼𝙄𝘿?")
    print("YOU MUST TO WRITE RIGHTLY, IT NEED TO BE WITH CAPITAL LETTERS!!!")
    time.sleep(1); a = input("Open door? Y/N")
    
    if a == "Y":
        time.sleep(1)
        name()

    elif a == "N":
        print("Soon....")
        time.sleep(1)
        start()
    
    else:
        print("Wrong answer............")
        time.sleep(1)
        start()
        
        
start()
# round_one()
# round_two()
# round_three()