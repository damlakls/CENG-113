#280201082-Nurcan Yıldız
#280201057-Damla Keleş

import random
all_pinsA = []          #We created an empty list to show the scores of player A
total_scoreA = [0]      #This list is to write the total scores of each round for A
all_pinsB = []          #We created an empty list to show the scores of player B
total_scoreB = [0]     #This list is to write the total scores of each round for B
strikeA = 0             #This variable for if strike or spare == 3: spare_score or strike_score functions will execute.
spareA = 0               # 
strikeB = 0
spareB = 0

def is_spareA(a,spareA):            #a is for the round number
    spareA = 3                       #This if first funct. When pins = 10 this part will execute.
    total_scoreA.append(0)     #We had a problem because the list was empty. then we assign the initial value 0 to add on top of it.
    b = total_scoreA[a-1]+10   
    return b and spareA      #we have returned the values of b and spareA for later use

def spare_scoreA(a,pins1,spareA):          # This is the second func. When pins = 10 last round, this func will execute.
    spareA = 0
    total_scoreA.remove(a-1)
    total_scoreA[a-1] = 10 + pins1
    total_scoreA.append(total_scoreA[a-1])
    return total_scoreA[a-1] and spareA

def is_spareB(a,spareB):           #I explained in other function. İt works like that.
    spareB = 3
    total_scoreB.append(0)
    b = total_scoreB[a-1]+10
    return b and spareB               #we have returned the values of b and spareB for later use

def spare_scoreB(a,pins1,spareB):
    spareB =0
    total_scoreB.remove(a-1)
    total_scoreB[a-1] = 10 + pins1
    total_scoreB.append(total_scoreB[a-1])
    return total_scoreB[a-1] and spareB

def is_strikeA(a,strikeA):
    strikeA = 3
    total_scoreA.append(0)
    b = total_scoreA[a-1]+10
    return b and strikeA

def strike_scoreA(a,pins1,pins2,strikeA):
    strikeA = 0
    total_scoreA.pop(a-1)
    total_scoreA[a-1] = 10 + pins1 +pins2
    total_scoreA.insert(a-1,total_scoreA[a-1])
    return total_scoreA[a-1] and strikeA

def is_strikeB(a,strikeB):
    strikeB = 3
    total_scoreB.append(0)
    b = total_scoreB[a-1]+10
    return b and strikeB

def strike_scoreB(a,pins1,pins2,strikeB):
    strikeB = 0
    total_scoreB.remove(a-1)
    total_scoreB[a-1] = 10 + pins1 +pins2
    total_scoreB.append(total_scoreB[a-1])
    return total_scoreB[a-1] and strikeB  

def main():
    player_list=['A','B']                             #we have imported the random module to choose the first player
    first_player=random.choice(player_list)           #now the the first player is determined
    player_list.remove(first_player)                  #the other one is the second player
    second_player=random.choice(player_list)
   
    a = 0
    while a != 10:                                      #this loop will contunie until the round number is 11
        print("Player", first_player,"rolls...")
        pins1 = int(input("Pins: "))
        while pins1 > 10:
            print("invalid")
            pins1 = int(input("Pins: "))
        all_pinsA.append(pins1)                #add pins1 at all_pinsA list.
    
        if pins1 == 10 :               #If pins=10 is_strikeA function will execute.
            is_strikeA(a,strikeA)              
            print(all_pinsA)
            print(total_scoreA)
            
        else:
            pins2 = int(input("Pins: "))
            while pins2 > 10 or (pins1+pins2)>10 :
                print("invalid")                          #Execute an error message.
                pins2 = int(input("Pins: "))
            all_pinsA.append(pins2)               #add the pins2 at all_pinsA list
            if (pins1 + pins2) == 10:
                is_spareA(a,spareA)
            else:
                total_scoreA.append(pins1+pins2+total_scoreA[-1])
            if a == 0 :
                total_scoreA.remove(0)           #Delete the unnecessary first index. It was necessary so that the list is not empty. But not necessary anymore.
            if strikeA == 3:                  #If last round is_strikeA function was executed, this round executes this function. 
                strike_scoreA(a,pins1,pins2,strikeA)           
            if spareA == 3:
                spare_scoreA(a,pins1,spareA)
            if a == 9:
                if pins1 == 10 or (pins1 + pins2) == 10:         #In round 10, if player do a strike or spare, 1 more ball will be allowed to throw.
                    pins3 = int(input("Pins: "))
                    total_scoreA[9] = total_scoreA[9] + pins3

            print(all_pinsA)
            print(total_scoreA)


        print("Player", second_player,"rolls...")
        pins1 = int(input("Pins: "))                      
        while pins1 > 10:
            print("invalid")
            pins1 = int(input("Pins: "))
        all_pinsB.append(pins1)
        if pins1 == 10 :
            is_strikeB(a,strikeB)               
        
        else:
            pins2 = int(input("Pins: "))
            while pins2 > 10 or (pins1+pins2)>10 :
                print("invalid")
                pins2 = int(input("Pins: "))
            all_pinsB.append(pins2)
            if (pins1 + pins2) == 10:
                is_spareB(a,spareB)
            else:
                total_scoreB.append(pins2+pins1+total_scoreB[-1])
            if a == 0 :
                total_scoreB.remove(0)
            if spareB == 3:
                spare_scoreB(a,pins1,spareB)
            if strikeB == 3:
                strike_scoreB(a,pins1,pins2,strikeB)
            if a == 9:
                if pins1 == 10 or (pins1 + pins2) == 10:
                    pins3 = int(input("Pins: "))
                    total_scoreB[9] = total_scoreB[9] + pins3
        print(all_pinsB)
        print(total_scoreB)
        a += 1
    if total_scoreA[9] > total_scoreB[9]:               #this part is to determine the winner of the game
        print("A win")
    elif total_scoreB[9] > total_scoreA[9]:            #Check the last index of total_score lists. Last index is total.
        print("B win")
    elif total_scoreB[9] == total_scoreA[9]:
        print("There is no winner.")

main()                                         #we called the main function