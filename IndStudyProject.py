#board game night

#rock paper scissors
#add prompt where user can choose which game to play
game = print("Which game would you like to play? Rock paper scissors (RPS), Tic Tac Toe, or Spanish Simulator (SS)?")
if game == "RPS":
    while player = False:
    #set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]

#reference: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

#tic tac toe
elif game == "Tic Tac Toe":
    board = [" " for x in range(9)]
    def print_board():
        row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
        row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
        row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()
    def player_move(icon):
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2
        print("Your turn player {}".format(number))
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        else:
            print()
            print("That space is taken!")
    def is_victory(icon):
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
           (board[3] == icon and board[4] == icon and board[5] == icon) or \
           (board[6] == icon and board[7] == icon and board[8] == icon) or \
           (board[0] == icon and board[3] == icon and board[6] == icon) or \
           (board[1] == icon and board[4] == icon and board[7] == icon) or \
           (board[2] == icon and board[5] == icon and board[8] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon) or \
           (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False
    def is_draw():
        if " " not in board:
            return True
        else:
            return False
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
    
    #reference: https://machinelearningprojects.net/tic-tac-toe-game-in-python/

#goal: work on adding a 2048 game as well.

#score = 0 **Want to add a score system after figuring out the whole convo as to not mess up anything (yet)

elif game == "SS":
    '''
    Convo:
    starts with
    what's your name
    where are you from
    what's your favorite color
    ending the conversation
    '''
    print("Welcome to the bilingual language bot!")
    name = input("What's your name? \n")
    print("Hello, " + name + "!")
    
    print("The language we will be reviewing is Spanish!")
    print("Let's start off with the basics. You run into a friend, and want to start a conversation. Which do you say?")
    
    choice1 = str(input("Type '1' for 'Hola, como te llamas?' or type '2' for 'Hola, como te yamas?': \n"))
    if choice1 == "1":
        print("Great! Let's move onto the next part of the conversation.")
        choice2 = str(input("Your new friend tells you that their name is Quin. They also reply with 'Y tu? Como te llamas?' What did Quin ask you?\nDid he say 1: 'And you? How are you?' or did he say 2: 'And you? What's your name? \n"))
        if choice2 == "1":
            print("Wrong. What Quin actually asked was 'And you? What is your name?' It's okay, you'll get the next one!")
        elif choice2 == "2":
            print("Correct! Quin asked you 'And you? What is your name?'")
            choice3 = str(input("You reply with 'me llamo " + name + ". You want to ask Quin where he's from. What do you reply with?\nWould you say 1: 'De donde eres?' or 2:'Donde vive?\n"))
            if choice3 == "1":
                print("Correct! Although number 2 isn't completely incorrect, it translates to 'Where do you live?'. 'De donde eres?' correctly asks someone where they're from.")
            elif choice3 == "2":
                print("")
        else:
            print("Invalid input.")
    elif choice1 == "2":
        print("The answer is actually 1. The correct spelling for saying 'What is your name?' in Spanish is 'Como te LLAMAS'. \n In Spanish, two L's are used to make the 'y' sound in 'llamas'.")
        choice2 = input("ALRIGHT LETS DO ANOTHER EASY PRACTICE!")
        if choice2 == "":
            print("")
        elif choice2 == "":
            print("")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
