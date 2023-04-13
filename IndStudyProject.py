#score = 0 **Want to add a score system after figuring out the whole convo as to not mess up anything (yet)
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
