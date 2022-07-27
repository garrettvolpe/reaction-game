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
