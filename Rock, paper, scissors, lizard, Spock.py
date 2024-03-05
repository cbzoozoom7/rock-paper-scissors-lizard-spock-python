import random
rand = random.randint(0,4)
answer = raw_input("Rock, paper, scissors, lizard, Spock! ")
print ""
if answer.lower() == "rock" or answer.lower() == "r" or answer == "0":
    if rand == 0:
        print "Rock! It's a draw."
    elif rand == 1:
        print "Paper! I win!"
    elif rand == 2:
        print "Scissors! Oh, you win..."
    elif rand == 3:
        print "Lizard! Oh, you win..."
    elif rand == 4:
        print "Spock! I win!"
elif answer.lower() == "paper" or answer.lower() == "p" or answer == "1":
    if rand == 0:
        print "Rock! Oh, you win..."
    elif rand == 1:
        print "Paper! It's a draw."
    elif rand == 2:
        print "Scissors! I win!"
    elif rand == 3:
        print "Lizard! I win!"
    elif rand == 4:
        print "Spock! Oh, you win..."
elif answer.lower() == "scissors" or answer.lower() == "scissor" or answer.lower() == "sc" or answer.lower() == "s" or answer == "2":
    if rand == 0:
        print "Rock! I win!"
    elif rand == 1:
        print "Paper! Oh, you win..."
    elif rand == 2:
        print "Scissors! It's a draw."
    elif rand == 3:
        print "Lizard! Oh, you win..."
    elif rand == 4:
        print "Spock! I win!"
elif answer.lower() == "lizard" or answer.lower() == "l" or answer == "3":
    if rand == 0:
        print "Rock! I win!"
    elif rand == 1:
        print "Paper! Oh, you win..."
    elif rand == 2:
        print "Scissors! I win!"
    elif rand == 3:
        print "Lizard! It's a draw."
    elif rand == 4:
        print "Spock! Oh, you win..."
elif answer.lower() == "spock" or answer.lower() == "sp" or answer == "4":
    if rand == 0:
        print "Rock! Oh, you win..."
    elif rand == 1:
        print "Paper! I win!"
    elif rand == 2:
        print "Scissors! Oh, you win..."
    elif rand == 3:
        print "Lizard! I win!"
    elif rand == 4:
        print "Spock! It's a draw."
else:
    print "Bad input"