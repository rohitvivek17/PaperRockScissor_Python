import random
print("***********************************************")
print("*       * PAPER * ROCK * SCISSOR *            *")
print("***********************************************")
print(" Lets start the game!!.... ")
point=0
ai=0
while(True):
    c=input(" Choose Paper->p  Rock->r  Scissor->s Stop->stop: ")
    if(c=="p"):
        point=10+random.randint(1,3)
        match point:
            case 11:
                print("Human: Paper", "AI: Rock")
                print("Human: win","AI: lost")
                print("________________________________")
            case 12:
                print("Human: Paper", "AI: Scissor")
                print("Human: Lost","AI: Won")
                print("________________________________")
            case 13:
                print("Human: Paper", "AI: Rock")
                print("Match Draw")
                print("________________________________")
    elif(c=="r"):
        print("Rock")
    elif(c=="s"):
        print("Scissor")
    elif(c=="stop"):
         break
print("Program End")



