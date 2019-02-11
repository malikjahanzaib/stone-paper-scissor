import random
import time

print("|ROCK||PAPER||SCISSORS|")
r = 'y'
while (r == 'Y' or r == 'y'):
    p = input("choose:\t(r) for rock\t(p) for paper\t(s) for scissor >> ")
    if (p == 'r' or p == 'R'):
        p1 = 1
        pch = 'rock'
    elif (p == 'p' or p == 'P'):
        p1 = 2
        pch = 'paper'
    elif (p == 's' or p == 'S'):
        p1 = 3
        pch = 'scissor'
    else:
        print("sorry, wrong choice entered!")
        continue
    c = random.randrange(1, 4)
    if (c == 1):
        cch = 'rock'
    elif (c == 2):
        cch = 'paper'
    else:
        cch = 'scissor'
    time.sleep(0.5)
    print('you chose: {}\ncomputer chose: {}'.format(pch, cch))
    if ((p1 == 1 and c == 1) or (p1 == 2 and c == 2) or (p1 == 3 and c == 3)):
        print("DRAW!")
    elif ((p1 == 1 and c == 3) or (p1 == 2 and c == 1) or (p1 == 3 and c == 2)):
        print("YOU WIN!")
    else:
        print("COMPUTER WINS!\n")
    r = input("do you want to play again? press 'Y' for yes else press any key to exit: ")

