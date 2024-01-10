#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#
import random
choice="""What would you like to do?
1.Play Rock Scissors Paper
"""
rock_scissors_paper_choice="""
Choose rock scissors or paper
1.Rock
2.Scissors
3.Paper
"""
choice_again="""What would you like to do?
1.Play again
2.Change mode
3.Exit
"""
player1name="you"
player2name="pc"
def rockscissorspaper():
    gamechoice=0
    print("Welcome")
    gamechose=input(choice)
    print("Great!")
    print("Welcome to Rock, Scissors, paper!")
    players=int(input("How many players do we have?(1 or 2)"))
    if (players==1):
        vspc()
    elif (players==2):
        vsplayer()

def vspc():
    playerchoice=int(input(rock_scissors_paper_choice))
    print("Great!")
    pcchoice=random.randint(1,3)
    print("Pc choosed",pcchoice)
    print(whowins(playerchoice,pcchoice))
    again()

   

def vsplayer():
    print("in developnent")
    ROCK = "1"
    SCISSOR = "2"
    PAPER = "3"

def again():
    last_choice=int(input(choice_again))
    if (last_choice==1):
        vspc()
    
    

def whowins(player1,player2):
    result=""
    if (player1==player2):
        result="draw"
    elif (player1-1==player2):
        result=player2name+" wins"
    elif(player1-2==player2):
        result=player1name+" wins"
    elif(player1==player2-1):
        result=player1name+" wins"
    elif(player1==player2-2):
        result=player2name+" wins"
    return result
rockscissorspaper()

