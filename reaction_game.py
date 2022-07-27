import keyboard
import time
import random
import os


print("""
************************************
Lets get ready to play..............
************************************
******'REACTION_GAME'***************
************************************""")
time.sleep(1.5)
print("""\n\nThe rules are as followed:

A digit will be presented and it is your job to press that key on your keyboard as fast as you can.

You will have 10 rounds before you get your final stats!

Good Luck!\n\n""")

time.sleep(3)

print("are you ready?!?")
are_you_ready = input("Type :(yes)(no)\n")

if are_you_ready == "yes":
    print("ok, lets start")

print("\n\n\n")
time.sleep(1.5)
print("Game will begin in:")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...\n\n\n\n\n\n")
time.sleep(1)

total_times_want_to_play = 10
list_of_scores = []
x=0

def game (num):
    keyboard.is_pressed("n")
    print(num)
    start = time.time()
    while (True):
        try:
            if keyboard.is_pressed(str(num)):
                end = time.time()
                return end-start
                break
        except:
            pass

while x < total_times_want_to_play:
    random_digit = random.randrange(1, 10)
    score = round(game(random_digit),4)
    print("\n\n\n\n\n\n\n\n\n")
    list_of_scores.append(float(str(score)))
    time.sleep(random.randrange(1,3))
    x += 1



average = sum(list_of_scores) / len(list_of_scores)
# print(list_of_scores)
# print(average)
print("""
Results:

Average score is .965 seconds

Your average score was """ + str(average))

if average < .965:
    print("\nCongrats! You are faster than average")
else:
    print("\nYou are too slow......Step your game up!")
