import random

GamesList = ["rps", "python knowledge"]
rpsturns = ["rock", "paper", "scissor"]
quitmsg = "--------------------------------------------------------\nDont forget to follow me on Instagram : @soheil.jei :D\nFor lastest version of Scripts check out github : \n--------------------------------------------------------"
humanscore = 0
pcscore = 0

Qlist = ["Who created Python ?", "When was python first invented ?", "how do u define a function in python ?"]
Alist = [
    ["Donald Trump", "Guido van Rossum", "Elon Musk", "Gigachad"],
    ["1996", "1991", "2010", "1972"],
    ["def", "import", "global", "expect"]
]
Tlist = ["guido van rossum", "1991", "def"]



def choosinggame():
    try:
        game_choose = input("What game do you want to play ? rps or python knowledge(type pk for short) : ")
        if str(game_choose.lower()) == "rps":
            playerturn = input("OK now Choose between rock, paper or scissor : ")
            if playerturn in rpsturns:
                rps(Player_turn=playerturn)
            else:
                rps(playerturn)
        elif str(game_choose.lower()) == "python knowledge" or str(game_choose.lower()) == "pk":
            pk()
        elif str(game_choose.lower()) == "quit":
            print(quitmsg)
        else:
            print("Unfortunately we only have 2 games, Lanuch the script on more time and Select the one u like to play\n\n" + quitmsg)
    except KeyboardInterrupt:
        print(quitmsg)



def rps(Player_turn):
    global humanscore
    global pcscore
    player_turn = Player_turn.lower()
    pc_turn = random.choice(rpsturns).lower()
    try:
        if player_turn == pc_turn:
            print("Ur Choice {}\n Pc Choice : {}\n Tie!\n UR Score : {}\n PC Score : {}".format(player_turn, pc_turn,
                                                                                                humanscore, pcscore))

        elif player_turn == "rock" and pc_turn == "paper":
            if humanscore > 0:
                humanscore += 1
                pcscore -= 1
                print(
                    "Ur Choice : {}\n Pc Choice : {}\n U lose mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                            pc_turn,
                                                                                                            humanscore,
                                                                                                            pcscore))
            elif humanscore == 0:
                pcscore += 1
                print(
                    "Ur Choice : {}\n Pc Choice : {}\n U lose mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                            pc_turn,
                                                                                                            humanscore,
                                                                                                            pcscore))
        elif player_turn == "paper" and pc_turn == "rock":
            humanscore += 1
            print("Ur Choice : {}\n Pc Choice : {}\n U Win mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                         pc_turn,
                                                                                                         humanscore,
                                                                                                         pcscore))
        elif player_turn == "paper" and pc_turn == "scissor":
            pcscore += 1
            print("Ur Choice {}\n Pc Choice : {}\n U lose mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                        pc_turn,
                                                                                                        humanscore,
                                                                                                        pcscore))
        elif player_turn == "rock" and pc_turn == "scissor":
            humanscore += 1
            print("Ur Choice : {}\n Pc Choice : {}\n U Win mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                         pc_turn,
                                                                                                         humanscore,
                                                                                                         pcscore))
        elif player_turn == "scissor" and pc_turn == "rock":
            pcscore += 1
            print("Ur Choice {}\n Pc Choice : {}\n U lose mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                        pc_turn,
                                                                                                        humanscore,
                                                                                                        pcscore))
        elif player_turn == "scissor" and pc_turn == "paper":
            humanscore += 1
            print("Ur Choice : {}\n Pc Choice : {}\n U Win mate!\n UR Score : {}\n PC Score : {}".format(player_turn,
                                                                                                         pc_turn,
                                                                                                         humanscore,
                                                                                                         pcscore))
        else:
            rps(input("U have to Choose between rock, paper or scissor : "))

        r = input("\n\nWanna Play again ?(yes/no) : ")
        if r.lower() == "yes":
            choosinggame()
        else:
            print(quitmsg)

    except KeyboardInterrupt:
        print(quitmsg)


def pk():
    global Tlist, Alist, Qlist
    for i in range(0, 3):
        q = input(str(Qlist[i]) + "\n" + str(Alist[i]) + " : ")
        if q in Tlist:
            print("Good J0b kiddo")
        else:
            print("Wrong! Think harder next time mate!")
    print("These are the True answers : " + str(Tlist))
    r = input("\n\nWanna Play again ?(yes/no) : ")
    if r.lower() == "yes":
        choosinggame()
    else:
        print(quitmsg)


choosinggame()