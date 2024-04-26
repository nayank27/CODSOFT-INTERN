import random
l=["Rock","Paper","Scissor"];
while True:
    Ccount=0
    Ucount=0
    Uc=int(input('''
                    Game start...
                     1 Yes
                     2 No '''))
    if Uc==1:
        for a in range(1,6):
            userInput=int(input('''
                     1.Rock
                     2.Scissor
                     3.Paper'''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Scissor"
            elif userInput==3:
                uchoice="Paper"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                Ucount=Ucount+1
                Ccount=Ccount+1
            elif(uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="ppaer"):
                print("Computer Value", cchoice)
                print("User Value", uchoice)
                print("You Win")
                Ucount=Ucount+1
            else:
                print("Computer Value", cchoice)
                print("User Value", uchoice)
                print("computer Win")
                Ccount = Ccount + 1
        if Ucount==Ccount:
            print("Final Game Draw")
            print("User Score",Ucount)
            print("Computer score",Ccount)
        elif Ucount>Ccount:
            print("Final you win the Game")
            print("User Score", Ucount)
            print("Computer score", Ccount)
        else:
            print("Final computer win the game")
            print("User Score", Ucount)
            print("Computer score", Ccount)

    else:
        break